# Lac operon seed entity catalog

这个目录保存第一版乳糖操纵子原型的手工整理种子数据。

目标不是一次性覆盖全 MG1655，而是先得到一份可以初始化 Agent 的最小实体目录。

## 文件

- `entities.csv`: 每一行是一个未来 Agent 或图谱节点。

## 当前范围

包括：

- lac 操纵子相关基因。
- 对应蛋白。
- 关键小分子。
- 两个调控复合体。
- lacO 调控区域。

## 后续补充

下一步应继续整理：

- `edges.csv`: 实体之间的调控、结合、催化、转运关系。
- `pathways.csv`: lac operon regulation、galactose metabolism、carbon catabolite repression 等模块。
- `initial_states.csv`: 不同扰动条件下的初始状态。
- `phenotype_rules.csv`: 表型标签触发条件。
