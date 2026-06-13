# Agent 模型

## Agent 是什么

Agent 代表一个“分子种类”，不是一个分子拷贝。

例如：

- 一个 `LacI` Agent 代表 LacI 这类蛋白。
- 一个 `lactose` Agent 代表乳糖这种小分子。
- 一个 `lacZ` Agent 代表 lacZ 这个基因。

这样可以避免细胞内分子数量带来的规模爆炸，同时保留分子之间的逻辑关系。

## Agent 基本结构

```json
{
  "agent_id": "protein.LacI",
  "type": "protein",
  "static": {
    "name": "LacI repressor",
    "annotation": "功能注释",
    "pathways": ["lac operon regulation"],
    "neighbors": ["gene.lacZ", "molecule.allolactose", "complex.LacI_lacO"]
  },
  "history": []
}
```

## 静态信息

静态信息来自数据库整理，不由 LLM 生成。

需要包含：

- 标准 ID
- 名称和别名
- 实体类型
- 功能注释
- 所在通路
- 邻居关系
- 数据来源

## 动态状态

动态状态由仿真产生。

不同类型 Agent 使用不同状态词汇：

| 类型 | 推荐状态 |
| --- | --- |
| 基因 | `expressed`, `repressed`, `knocked_out`, `mutated`, `overexpressed` |
| 蛋白 | `active`, `inhibited`, `degraded`, `sequestered` |
| 小分子 | `absent`, `low`, `medium`, `high` |
| 复合体 | `active`, `impaired`, `disrupted`, `assembled`, `dissociated`, `partial` |

## 复合物 Agent

大肠杆菌复合物数量级是几百个，适合全部作为独立 Agent 纳入 `entities.csv`。不需要设计复杂的虚拟节点体系，但需要把行为分成两类。

### 结构性大型复合物

例子：

- 核糖体
- RNA polymerase
- ATP synthase

行为逻辑：

- 不参与 LLM 决策轮。
- 状态由组成成分自动计算。
- 作为下游 Agent 感知的状态节点。

状态计算示例：

```text
critical_components 全部 active -> active
任一 critical_component inhibited -> impaired
任一 critical_component degraded -> disrupted
```

### 调控性小型复合物

例子：

- 转录因子二聚体
- 双组分系统复合物
- 蛋白-DNA 复合物
- 小分子-转录因子复合物

行为逻辑：

- 参与 LLM 决策轮。
- 组装和解聚本身就是调控事件。

例子：

```text
LacI-lacO 复合物感知 allolactose 上升
  -> 判断是否 dissociated
  -> lacO 暴露
  -> lac 操纵子更可能 expressed
```

### 复合物字段

`entities.csv` 为复合物增加这些字段：

```text
complex_type
is_virtual
components
critical_components
assembly_condition
```

含义：

- `complex_type`: `structural` 或 `regulatory`。
- `is_virtual`: `true` 表示不走 LLM 决策，状态由组件自动计算。
- `components`: 所有组成成分。
- `critical_components`: 关键成分。
- `assembly_condition`: 组装条件的自然语言描述。

## 历史记录

每轮保存：

```json
{
  "round": 1,
  "state": "inhibited",
  "neighbors_snapshot": {
    "molecule.allolactose": "high",
    "complex.LacI_lacO": "disassembled"
  },
  "reasoning": "allolactose 高，LacI 更可能被诱导物结合并失去阻遏能力。"
}
```

## Agent 重新实例化

仿真结束后，可以把某个 Agent 的完整历史重新喂给 LLM，让它以该 Agent 的视角回答问题。

这不是为了让 Agent 改写历史，而是为了做解释和追问。

示例问题：

- “你为什么在第 1 轮从 active 变成 inhibited？”
- “你看到哪些邻居状态后做出判断？”
- “如果 lactose 没有升高，你可能会怎样？”
