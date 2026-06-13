# 时序 GraphRAG 与批量回合仿真计划

## 目标

第一版 E.coil 不直接做全细胞精细模拟，而是先做一个可运行的“知识图谱驱动的分子回合模拟器”。

参考 MiroFish 的思想：

```text
种子材料 -> 图谱世界 -> Agent 配置 -> 回合演化 -> 时序记忆 -> 报告解释
```

迁移到 E.coil：

```text
生物数据库 -> 细胞知识图谱 -> 分子 Agent -> 分子状态回合演化 -> 时序图历史 -> ReportAgent
```

时序 GraphRAG 在这里不是用来发明生化规则，而是作为“检索与传播调度层”：从静态知识图谱和动态状态历史中检索最相关的邻居、通路、历史轮次和证据，再把压缩后的上下文交给 LLM 精判。

## 核心原则

- 图谱关系仍然来自 `entities.csv`、`edges.csv`、`pathways.csv`，LLM 和 GraphRAG 都不能新增生化边。
- LLM 只处理复杂语义判断，例如“这个邻居状态变化是否真的影响我”。
- GraphRAG 只做候选筛选、证据检索、上下文压缩和传播范围控制，不直接决定生化状态。
- 简单规则由代码执行，例如 knock_out、structural complex 状态聚合、无变化休眠。
- 每轮只调用活跃 Agent，避免 1.3 万实体全部请求 LLM。

## 第一版系统分层

### 1. StaticGraph 层

输入：

- `data/normalized/entities.csv`
- `data/normalized/edges.csv`
- `data/normalized/pathways.csv`

输出：

- entity 索引。
- typed edge 索引。
- 每个 Agent 的邻居列表。
- 可抽取子图，例如 `lac_operon`、`cell_wall`、`ribosome`。

### 2. TemporalState 层

每一轮保存离散状态：

```text
round
entity_id
state
abundance_label
changed
reason
changed_neighbors
```

同时生成时序特征：

```text
当前状态 one-hot
上一轮是否变化
最近 k 轮变化次数
邻居变化数量
边类型统计
实体类型
空间分区
```

这些特征进入时序 GraphRAG 检索器或轻量规则调度器。

### 3. Temporal GraphRAG 检索调度层

初期不要把 GraphRAG 做得太重。建议先做可解释的检索排序：

第一步：基于图谱和历史的候选召回。

```text
changed_entity
  -> 1-hop/2-hop typed neighbors
  -> same pathway neighbors
  -> recently changed neighbors
  -> same operon / same reaction / same complex neighbors
```

第二步：证据打分和上下文压缩。

```text
edge_type_weight
  * (0.7 ** rounds_unchanged)
  * state_change_magnitude
  + recent_changes_in_last_3_rounds * 0.3
  -> retrieval_score
```

用于选择本轮候选 Agent，并为每个 Agent 拼出短上下文：

```text
Agent static note
top changed neighbors
top relevant edges
top recent history snippets
allowed states
```

当前仿真传播保持逐轮 1-hop：上一轮改变的 Agent 只唤醒相邻候选，候选真正改变后再进入下一轮继续传播。这样不会跳过中间生物实体，也便于 ReportAgent 重建 A→B→C 的因果链。

第三步：积累模拟历史后，可以再训练轻量排序模型。

训练目标可以是：

- 预测下一轮哪些 Agent 会变化。
- 预测某条边是否会传导。
- 预测是否需要 LLM 精判。

这一步是优化项，不是第一版必须条件。

### 4. RuleEngine 层

代码直接处理确定性规则：

- 用户显式扰动，例如 gene knockout。
- structural complex 的状态聚合。
- 没有变化邻居的 Agent 休眠。
- 不允许状态的回滚和校验。
- 图谱边界校验。

### 5. LLMDecision 层

只处理被唤醒的复杂 Agent。

输入：

- Agent 功能注释。
- 当前状态。
- 发生变化的邻居。
- 与邻居的关系类型。
- 最近历史。
- 允许输出状态。

输出必须是 JSON：

```json
{
  "entity_id": "protein.P03023",
  "next_state": "inhibited",
  "confidence": "medium",
  "affected_by": ["small_molecule.C00243"],
  "reason": "..."
}
```

输出后必须经过 schema 校验和图谱规则校验。

### 6. BatchScheduler 层

每轮流程：

```text
1. 收集 changed agents
2. 沿图谱找 1-hop/2-hop 候选
3. RuleEngine 先处理确定性变化
4. Temporal GraphRAG / retrieval_score 排序候选并压缩上下文
5. 只对 top-k 或超过阈值的 Agent 构造 prompt
6. 并发请求 vLLM
7. 校验输出并写入下一轮状态
8. 保存 round snapshot 和 agent history
```

## vLLM 批量推理方案

`primary world/run_llm_sim.sh` 只是启动 `sandbox/main.py`。真正的 LLM 请求在 `sandbox/agents/llm_client.py`。

当前 `primary world` 的客户端有一个重要问题：

```text
BatchLLMClient 使用 ThreadPoolExecutor
但 _single_request 里用 lock 包住了整个 HTTP POST
所以请求实际上容易被串行化
```

vLLM OpenAI-compatible server 本身支持 continuous batching。我们应该做的是：

- 保持 vLLM server 热加载 Qwen3.5-9B。
- 启动 vLLM 时开启 `--enable-prefix-caching`。
- 客户端用 `httpx.AsyncClient` + `asyncio.gather` 并发发请求。
- 用 `Semaphore` 控制并发数，例如 16/32。
- 不在 HTTP POST 外层加全局锁。
- 每轮把活跃 Agent prompts 一次性交给 batch client。
- 失败请求重试，不让整轮回退。

可选方案：

- Server 模式：推荐。兼容 OpenAI API，易调试，vLLM 自动 continuous batching。
- Offline 模式：使用 `vllm.LLM.generate(prompts)` 直接批量生成。吞吐可能更高，但模拟器和模型必须在同一个 Python/GPU 环境里，工程耦合更重。

### Prefix caching 使用方式

vLLM 的 automatic prefix caching 可以复用多个请求共享前缀的 KV cache，主要节省 prefill 阶段开销。它适合 E.coil，因为每个 Agent 决策请求有大量共享内容：

```text
system prompt
输出 JSON schema
全局规则约束
状态词表
边类型说明
```

prompt 应该拆成稳定前缀和动态后缀：

```text
[稳定前缀]
  system rule
  JSON schema
  allowed states
  relation vocabulary

[动态后缀]
  current agent annotation
  retrieved neighbors
  recent temporal history
  current round question
```

注意：

- 只有字面 token 完全相同的前缀才能高效命中缓存。
- Agent 独有的功能注释如果放在 system prompt 前面，会破坏共享前缀。
- prefix caching 减少 prefill，不减少 decode；如果输出很长，收益会下降。
- “节省约 30% KV cache / 并发 70-80”需要用本机 GPU、prompt 长度、max_tokens 和并发数压测确认，不能写成固定保证。

## Qwen3.5-9B 配置

模型路径沿用：

```text
/home/zkyd/data1/ycy/P_world/Qwen3.5-9B/Qwen/Qwen3_5-9B
```

chat template 沿用：

```text
/home/zkyd/data1/ycy/P_world/primary world/qwen35_no_thinking.jinja
```

第一版推荐参数：

```text
temperature: 0.2
top_p: 0.8
decision_max_tokens: 256
enable_thinking: false
response_format: json_schema
prefix_caching: true
```

## 里程碑

### M0: 项目骨架

产出：

- `ecoil_sim/graph/static_graph.py`
- `ecoil_sim/state/temporal_state.py`
- `ecoil_sim/llm/vllm_client.py`
- `ecoil_sim/sim/scheduler.py`
- `ecoil_sim/report/report_agent.py`

成功标准：

- 能加载 normalized CSV。
- 能抽取指定 seed entity 的子图。
- 能保存 round snapshot。

### M1: lac operon 回合闭环

产出：

- 从全量图谱抽取 lac 相关子图。
- 支持自然语言扰动解析的简化版本。
- 支持 5-10 轮仿真。
- 支持 ReportAgent 回答“为什么 lacZ 变化”。

成功标准：

- 输入 lactose/glucose/lacI knockout 组合，能产生可解释状态演化。

### M2: 批量 LLM 调度

产出：

- 真正异步并发的 vLLM client。
- 每轮只对 active agents 发请求。
- 每条响应独立校验、独立重试。

成功标准：

- 16-64 个 Agent prompt 可以并发提交给 vLLM。
- 单个失败不导致整轮失败。

### M3: 时序 GraphRAG 调度

产出：

- GraphRAG 检索排序器。
- retrieval_score。
- 每个 Agent 的短证据上下文。
- top-k 唤醒策略。

成功标准：

- 扰动后不再简单扩散所有邻居，而是按图谱关系、历史变化和通路证据检索候选。

### M4: 小模块扩展

候选模块：

- lac operon
- central carbon metabolism
- cell wall synthesis
- ribosome / translation
- SOS response

成功标准：

- 可以从全量图谱抽取多个模块并分别运行小实验。

## 近期最推荐执行顺序

1. 先做 `StaticGraph` 和子图抽取。
2. 再做 `TemporalState` 和 round/history 存储。
3. 再接 Qwen3.5-9B 的异步 batch client。
4. 先用 lac operon 跑通 5 轮。
5. 最后加入时序 GraphRAG 检索调度器。

这个顺序比较稳：先让细胞世界能动起来，再让它动得更聪明。
