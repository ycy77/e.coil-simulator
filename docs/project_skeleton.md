# 工程骨架

E.coil 采用数据和逻辑分离的结构。后续补充 EcoCyc、RegulonDB、复合物、转运、表型时，优先追加数据文件和规则注册表，不改核心仿真代码。

## 目录

```text
data/
  normalized/                 # 实体、边、通路标准表
  registry/                   # 由边和人工规则生成的唯一真值规则注册表
  regulationDB/               # 原始 RegulonDB 下载文件

configs/
  edge_weights.yaml           # 时序 GraphRAG 检索权重和关系类型配置
  simulation.yaml             # 仿真参数
  model.qwen35_9b.yaml        # vLLM/Qwen 配置

ecoil_sim/
  actions/                    # LLM action -> 标准 AgentState
  graph/                      # 只读静态图谱加载和子图抽取
  registry/                   # rule registry 加载和候选规则查询
  state/                      # 时序状态和历史
  retrieval/                  # 时序 GraphRAG 检索与上下文筛选
  rules/                      # 确定性规则引擎
  agents/                     # prompt 构建
  llm/                        # vLLM 并发客户端
  sim/                        # 主仿真循环
  storage/                    # round/agent 历史写入
  report/                     # 复盘接口

scripts/
  build_rule_registry.py      # edges.csv -> data/registry/native_rules.jsonl
  inspect_retrieval.py        # 检查扰动后的候选召回
  start_vllm.sh               # 启动 Qwen/vLLM，默认 1 GPU，可指定多 GPU
  test_offline_iteration.py   # 不启动 vLLM 的迭代测试

runs/
  <run_id>/                   # 每次仿真输出

main.py                       # CLI 入口
```

## 数据流

```text
data/normalized/entities.csv
data/normalized/edges.csv
data/normalized/pathways.csv
        ↓
scripts/build_rule_registry.py
        ↓
data/registry/native_rules.jsonl
        ↓
StaticGraph + RuleRegistry
        ↓
TemporalGraphRAG 召回候选 Agent 和规则
        ↓
PromptBuilder 构造局部 prompt
        ↓
LLM / RuleBasedMockLLM / NullLLMClient
        ↓
ActionInterpreter 把 action 归类为标准状态
        ↓
TemporalState + SimulationStore
```

## action 到状态的归类

LLM 不直接输出自由文本状态，而是输出 schema 约束的动作：

```text
change_activity
mark_inhibited
change_abundance
produce
consume
bind
unbind
...
```

`ecoil_sim/actions/interpreter.py` 再根据实体类型和 `allowed_states` 归类：

```text
gene + change_activity down     -> repressed
gene + change_activity up       -> expressed / overexpressed
protein + mark_inhibited        -> inhibited
protein + change_activity up    -> active
small_molecule + produce        -> abundance_label up
small_molecule + consume        -> abundance_label down
```

归类后的标准状态会写入 `TemporalState`。下一轮时序 GraphRAG 再从这些 `changed=True` 的 Agent 出发召回邻居，实现迭代传播。

## 时序 GraphRAG score

当前 `TemporalGraphRAG` 不再只是 1-hop 边权重，而是：

```text
score =
  edge_weight
  * (0.7 ** rounds_unchanged)
  * state_change_magnitude
  + recent_changes_in_last_3_rounds * 0.3
```

其中：

- `rounds_unchanged`: 候选 Agent 连续未变化轮数。
- `recent_changes_in_last_3_rounds`: 候选 Agent 最近 3 轮变化次数。
- `state_change_magnitude`: 扰动源本轮状态变化幅度，来自 `configs/edge_weights.yaml` 的 `state_distance`。

仿真传播默认保持逐轮 1-hop，避免跳过中间实体；多跳链由多轮状态变化自然形成。

## complex 和 transport 框架

structural complex 会由代码自动聚合：

```text
critical_components 全部 active -> active
任一 critical_component inhibited -> impaired
任一 critical_component degraded -> disrupted
```

当前全量数据里的 complex 组成还不完整，所以这套逻辑先作为框架等待 EcoCyc/Complex Portal 数据补入。

regulatory complex 不自动决定状态，继续走 LLM 决策；Prompt 会提供：

```text
complex_type
components
critical_components
assembly_condition
```

transport 当前采用保守截断：如果 transporter 自身变成 `inhibited/degraded/disrupted`，`transports` 边不再继续唤醒下游候选。空间转运的真实位置变化等空间层补齐后再写入状态。

离线验证迭代链：

```bash
python3 main.py --entity protein.P03023 --state active --rounds 3 --mock-llm
```

这会用确定性 mock action 测试链路，不启动 vLLM。

## 自然语言扰动

第一版自然语言扰动解析是保守的 deterministic parser：

```bash
python3 main.py --perturbation "敲除 lacI" --rounds 2 --mock-llm
python3 main.py --perturbation "抑制 LacI" --rounds 2 --mock-llm
```

它只做两件事：

- 识别通用扰动动词：敲除、突变、过表达、抑制、激活、升高、降低等。
- 在全量 `entities.csv` 中匹配原生实体 ID、name、alias。

它不会发明外源药物靶点。比如“加入氨苄青霉素”如果没有原生实体或候选靶点匹配，会进入 `unresolved_perturbations`，后续交给 LLM perturbation parser 或人工特例规则处理。

扰动解析现在按三层设计：

```text
1. data/perturbations/perturbation_knowledge.yaml
   只读知识库，命中关键词后直接输出结构化扰动。

2. 全量图谱搜索
   在 entities.csv 的 entity_id/name/aliases/annotation/pathways 中检索，
   只匹配图谱中已存在的原生实体。

3. LLMPerturbationParser 接口
   接收候选实体和功能注释，让 LLM 判断直接靶点和 effect。
   当前不默认启用，等 vLLM 可用后接入。
```

输出扰动会写入 Agent history 的 metadata：

```text
source
confidence
raw_input
perturbation_layer
```

`perturbation_knowledge.yaml` 的持久化条目使用 `source: database`。如果某次仿真需要 LLM 根据候选实体临时判断靶点，则标注为 `source: llm_inference`，只保存在本次 session 历史中，不回写知识库。

## GPU 与 Agent 并发预算

默认配置：

```text
default_gpus: 1
agents_per_gpu: 50
```

因此默认每轮最多唤醒 50 个 Agent。启动/运行时可以指定 GPU 数：

```bash
python3 main.py --perturbation "抑制 LacI" --use-llm --gpus 4
```

此时调度预算为：

```text
max_active_agents = gpus * agents_per_gpu = 4 * 50 = 200
```

真实 vLLM 启动：

```bash
scripts/start_vllm.sh --gpus 1 --devices 0
scripts/start_vllm.sh --gpus 4 --devices 0,1,2,3
```

注意：`50 agents/GPU` 是默认调度假设，不是硬件保证值。真实可承载并发取决于 GPU 显存、prompt 长度、输出长度、prefix caching 命中率和 vLLM 参数。后续压测后只需要修改 `configs/simulation.yaml` 的 `agents_per_gpu`。

## 后续补数据的方式

新增数据源时只做两件事：

1. 写解析脚本，把原始数据转成 `entities.csv`、`edges.csv`、`pathways.csv` 或新的 `data/registry/*.jsonl`。
2. 如果新增关系类型，在 `configs/edge_weights.yaml` 加权重和默认规则类型。

核心仿真代码不需要知道数据来自 UniProt、KEGG、EcoCyc 还是 RegulonDB。
