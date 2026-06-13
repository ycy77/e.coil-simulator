# 仿真循环

## 输入

一次仿真的输入包括：

- 用户扰动
- 本次使用的知识图谱快照
- Agent 初始状态
- 固定仿真轮数

## 扰动解析

外源扰动不预先进入实体表。实验开始时，用户用自然语言输入扰动，系统先做图谱预筛，再由 LLM 精判。

流程：

```text
自然语言扰动
  -> 关键词、同义词、通路名检索
  -> 召回相关实体、通路、功能注释
  -> LLM 判断直接受影响的原生实体
  -> 生成初始状态变更列表
```

例子：

```text
"加入青霉素"
  -> 候选：PBP、细胞壁合成、肽聚糖相关实体
  -> LLM 精判：哪些 PBP 或细胞壁合成实体直接 inhibited
  -> 写入 round_0 初始扰动
```

## 单轮流程

每一轮可以保持很简单：

```text
changed_agents = 上一轮发生状态变化的 Agent
候选 Agent = TemporalGraphRAG(changed_agents, static_graph, temporal_history)
for each candidate agent:
    构造局部 Prompt
    LLM 输出 action
    ActionInterpreter 把 action 归类为标准状态
    写入 TemporalState 和 agent history

保存 round snapshot
如果本轮没有任何状态变化，累计 stable_rounds
如果连续 stable_rounds 达到阈值，只在阶段报告中标注稳态
```

因此 E.coil 可以像 MiroFish 一样迭代运行。区别是 MiroFish 的事件会改变社会环境和角色记忆；E.coil 的 action 会改变分子 Agent 的标准状态，状态变化再沿生物图谱触发下一轮候选 Agent。

候选召回的 score 使用时序特征：

```text
edge_weight
* 跨轮衰减
* 状态变化幅度
+ 近 3 轮变化频率奖励
```

## Prompt 包含什么

单个 Agent 的决策 Prompt 只给局部信息：

- 你是谁。
- 你的功能注释。
- 你所在通路。
- 你当前状态。
- 你的邻居及其状态。
- 哪些邻居状态在上一轮发生了变化。
- 你能使用的状态词汇。
- 你必须基于图谱关系判断。

不要给全细胞全部状态，否则模型容易编出跨图谱关系。

## 输出格式

LLM 不直接输出自由状态，而是输出 action：

```json
{
  "actions": [
    {
      "action_type": "change_activity",
      "rule_id": "native.represses.protein.P03023.gene.b0344.RDBECOLITFC00223",
      "targets": ["gene.b0344"],
      "direction": "down",
      "strength": 1,
      "reason": "LacI is active and has a candidate represses rule targeting lacZ."
    }
  ]
}
```

系统再把 action 归类为标准状态：

```text
gene + change_activity down -> repressed
protein + mark_inhibited -> inhibited
small_molecule + produce -> abundance_label up
```

如果邻居变化与自己功能无关：

```json
{
  "actions": []
}
```

## 状态写入

每次写入同时保存两份：

1. Agent 视角：这个 Agent 自己的完整经历。
2. Round 视角：这一轮所有 Agent 的状态快照。

建议目录：

```text
simulation_store/
  meta.json
  graph.json
  agents/
    lacI.json
    lacZ.json
  rounds/
    round_0.json
    round_1.json
  stage_reports/
    round_0.json
    round_1.json
```

## 阶段报告

每轮结束后写入一个轻量阶段报告：

```text
stage_reports/round_N.json
  本轮新增变化的 Agent
  本轮传导边
  候选 Agent 数量
  当前状态计数
  是否检测到稳态
```

阶段报告不做复杂生物学总结，也不调用大模型。它的作用是让长轮次仿真可以边跑边看过程。

## 报告与响应模式对照

推理结束后的主输出是 ReportAgent 的全局生物学报告，而不是强制给系统贴一个表型标签。ReportAgent 读取所有 Agent 的状态历史后，重建扰动从哪里开始、沿哪些边传导、哪些分子发生了意外响应、最终稳定在什么状态。

`data/phenotypes/phenotype_db.yaml` 只作为可选的“已知响应模式对照库”。它的作用类似一个参考答案表：如果最终状态组合接近某种已知响应，报告里可以提示“本次结果像 beta-lactam cell-wall response”，并给出匹配了哪些字段。

例子：

```text
if protein.P02918 == inhibited
and protein.P02919 == inhibited
and protein.P0AD65 == inhibited
and protein.P0AD68 == inhibited:
    response_pattern ~= beta_lactam_cell_wall_response
```

这个对照不会反过来影响仿真，也不是硬规则。没有匹配也完全正常，ReportAgent 仍然会输出状态轨迹、因果链和潜在异常事件。

## 迭代控制

第一版使用固定轮数作为主控制。

细胞更像动态稳态，不应把“无变化”当成必须停止的收敛条件；某些调控回路还可能出现真实振荡。因此：

- 固定运行 N 轮。
- 连续 N 轮无变化只标注为 `steady_state.detected=true`。
- 即使检测到稳态，也继续运行到最大轮数。
- 全部轮次结束后，再由 ReportAgent 生成总报告。

不需要一开始就设计复杂调度器。
