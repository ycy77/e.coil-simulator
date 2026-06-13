# 实施路线

## Phase 0: 时序图回合仿真骨架

目标：先把 MiroFish 式“图谱世界 + 回合仿真 + 时序记忆”迁移到 E.coil。

需要完成：

- 实现 `StaticGraph`，加载 `entities.csv`、`edges.csv`、`pathways.csv`。
- 实现子图抽取，从全量图谱抽取 lac operon 等实验模块。
- 实现 `TemporalState`，保存每轮 Agent 状态和变化原因。
- 实现批量 LLM client，对接 Qwen3.5-9B vLLM 服务。
- 实现最小 `Scheduler`，只唤醒受扰动影响的局部邻居。

成功标准：

- 能从全量图谱抽取一个小子图。
- 能对一批活跃 Agent 构造 prompts。
- 能保存 round snapshot 和 agent history。

详细计划见：

```text
docs/temporal_graphrag_project_plan.md
```

## Phase 1: 乳糖操纵子原型

目标：先验证系统闭环，而不是追求全量数据。

需要完成：

- 整理 10-20 个 lac operon 相关 Agent。
- 手工或半自动建立小型图谱。
- 实现扰动输入。
- 实现多轮 Agent 状态更新。
- 保存 Agent 历史和 round 快照。
- 实现简单 ReportAgent。

成功标准：

- 输入“加入乳糖、降低葡萄糖”后，系统能产生 lac operon 诱导相关状态变化。
- 每个状态变化都有邻居状态和理由。
- ReportAgent 能解释 lacZ 为什么表达上升。

## Phase 2: 扩展到核心调控与代谢小图谱

目标：从单个操纵子扩展到多个互相影响的模块。

建议模块：

- lactose utilization
- glucose uptake
- cAMP-CRP regulation
- glycolysis coarse pathway
- stress response small subset

成功标准：

- 不同营养扰动能产生不同表型标签。
- ReportAgent 能比较两个扰动条件的因果链差异。

## Phase 2.5: 时序 GraphRAG 调度

目标：学习 MiroFish 的时序 GraphRAG 思想，但只用于候选 Agent 唤醒、证据检索、上下文压缩和传播排序。

第一步先做无训练的检索排序：

```text
changed_entity
  -> typed neighbors
  -> same pathway / operon / reaction / complex
  -> recent temporal history
  -> retrieval_score
```

第二步为每个被唤醒 Agent 压缩上下文：

```text
Agent static note
top changed neighbors
top relevant edges
top recent history snippets
allowed states
```

第三步等模拟历史积累后，再考虑训练轻量排序模型，预测：

- 哪些 Agent 下一轮可能变化。
- 哪些边更可能传导扰动。
- 哪些 Agent 需要 LLM 精判。

GraphRAG 不直接决定生化状态，也不能新增规则。

## Phase 3: 自动化知识图谱构建

目标：从数据库自动生成实体和边。

需要整理：

- 所有基因实体。
- 所有蛋白实体。
- 重要小分子实体。
- 转录调控边。
- 代谢反应边。
- 转运和结合边。
- 通路归属。

成功标准：

- 能从数据表生成 `graph.json`。
- Agent 初始化不再依赖手写列表。

## Phase 4: 全细胞规模探索

目标：让系统覆盖更大范围的大肠杆菌知识图谱。

重点不是提高数值精度，而是提高：

- 覆盖实体数。
- 覆盖通路数。
- 扰动类型。
- 表型标签库。
- 历史解释能力。

## 当前最推荐的下一步

先不要继续扩大数据库范围。

现在已有全量基础图谱，下一步应先做工程闭环：

```text
StaticGraph -> 子图抽取 -> TemporalState -> 批量 LLM 决策 -> 历史保存 -> ReportAgent
```

这个闭环跑通后，再加入时序 GraphRAG 调度和更多模块。
