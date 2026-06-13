# 知识图谱与规则约束

## 为什么需要规则约束

这个项目的风险不是“模型不够聪明”，而是模型太会编合理故事。

所以必须有一个外部知识图谱约束 Agent：

> Agent 只能沿图谱已有边互动，不能自由建立新关系。

## 知识图谱保存什么

知识图谱至少保存三类信息：

### 1. 实体节点

- 基因
- 蛋白
- 小分子
- 复合体
- 通路
- 表型标签

### 2. 关系边

- `encodes`: 基因编码蛋白
- `regulates`: 转录调控
- `activates`: 激活
- `inhibits`: 抑制
- `catalyzes`: 催化
- `transports`: 转运
- `binds`: 结合
- `forms_complex`: 形成复合体
- `participates_in_pathway`: 属于某条通路
- `is_substrate_of`: 小分子作为底物
- `is_product_of`: 小分子作为产物
- `is_component_of`: 是复合物组成成分
- `is_critical_for`: 是复合物关键成分

### 3. 证据来源

每条边都要保留来源：

- 数据库名称
- 数据库 ID
- 证据类型
- 可信度

## LLM 的位置

LLM 不直接修改知识图谱。

每轮仿真时，系统先从图谱中取出某个 Agent 的邻居和候选边，再让 LLM 在这个局部范围内判断状态变化。

简单说：

```text
图谱决定“谁能影响谁”
LLM 判断“在当前状态下影响是否发生”
```

同一个邻居变化不一定会传导给所有相邻实体。图谱边只表示“存在可能关系”，真正是否响应由 Agent 根据自身功能注释、关系类型和邻居状态变化判断。

这可以避免过度传播：

```text
PBP inhibited
  -> 细胞壁合成相关实体可能响应
  -> 功能无关但图谱邻近的实体可以不响应
```

## 状态变化的约束

每个状态变化最好都能追溯到一条图谱边。

例如：

```text
molecule.allolactose --binds/inhibits--> protein.LacI
protein.LacI --regulates/represses--> gene.lacZYA
```

这样当 lacZYA 从 `repressed` 变为 `expressed` 时，ReportAgent 可以解释：

1. lactose 升高。
2. allolactose 升高。
3. allolactose 影响 LacI。
4. LacI 阻遏下降。
5. lacZYA 表达上升。

## 第一版不需要过度复杂

第一版不必建立完整规则语言。

只需要：

- 节点表
- 边表
- Agent 初始状态表
- 表型标签触发表

等 lac operon 原型跑通后，再扩展成更严格的规则注册表。

## 外源输入

药物、外源诱导物、噬菌体、质粒等暂时不作为细胞原生 Agent 放进 `entities.csv`。

它们以后作为用户提示词里的扰动输入，由扰动解析层根据功能注释和知识图谱判断哪些原生实体受影响。

推荐解析方式：

```text
图谱预筛
  -> 根据扰动关键词、同义词、通路名称召回候选实体
LLM 精判
  -> 只读取候选实体注释，判断直接受影响实体和状态
```

例子：

```text
加入 IPTG -> 影响 lac 调控相关实体
加入氨苄青霉素 -> 影响细胞壁合成/PBP 相关实体
加入氯霉素 -> 影响翻译/核糖体相关实体
```

这样可以保持细胞知识图谱主要描述原生分子和通路，而把外源处理作为实验条件管理。
