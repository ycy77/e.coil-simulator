# 数据获取与整理计划

## 总体思路

E.coil 的数据不是直接喂给 LLM 的语料，而是用来构建“细胞知识图谱”。

你真正需要整理的是四类核心数据：

1. 实体信息：细胞里有哪些 Agent。
2. 关系信息：Agent 之间如何连接。
3. 通路信息：哪些实体属于同一个功能模块。
4. 表型信息：哪些状态组合代表一个可观察结果。

外源药物、外源诱导物、噬菌体、质粒等暂时不进入系统数据表。之后做扰动实验时，它们作为用户提示词输入，由扰动解析层临时判断会影响哪些原生分子实体。

第一版不要追求全量 MG1655，先用乳糖操纵子做最小闭环。

## 需要整理的数据

## 当前数据状态

现在已经整理出第一版全量基础图谱，来源包括 UniProt、KEGG、NCBI RefSeq，以及你手动下载的 RegulonDB TSV 文件。EcoCyc/BioCyc 许可已经拿到，下一步可以下载 flat files 并作为最高优先级补充源整合。

当前规模：

```text
entities.csv: 13194 entities
  gene: 4506
  protein: 4403
  small_molecule: 3480
  reaction: 590
  rna: 215

edges.csv: 27232 edges
  participates_in: 9867
  catalyzes: 4415
  encodes: 4402
  activates: 3721
  represses: 2356
  is_product_of: 1307
  is_substrate_of: 1164

pathways.csv: 137 pathways
```

这意味着：基础实体目录、KEGG 代谢/通路骨架、RefSeq 基因/RNA 补齐、RegulonDB confirmed/strong 转录调控边都已经有了。现在已经足够支持“图谱预筛 + LLM 精判”的原型实验，也足够从全量图谱中抽取 lac operon、中心碳代谢、细胞壁合成等小模块来跑第一批模拟。

还不完整的地方不是“系统不能跑”，而是以下几类连接还不够细：

- 复合物：等待解析 EcoCyc flat files，补充复合体实体、组分、关键亚基关系。
- 转运：等待解析 EcoCyc transport/reaction 信息，补充 transporter 到 substrate 的明确边。
- 操纵子/启动子：RegulonDB 已有文件，但当前只合并了 regulator/sigma 到 gene 的调控边，尚未展开 TU、operon、promoter、binding site 层级。
- 结合/PPI：还缺蛋白-蛋白结合、小分子-蛋白结合、蛋白-DNA 结合的系统化边。
- 表型：还缺突变体、营养变化、药物处理等状态组合到可观察表型的验证规则。

### 1. 所有实体信息

这是 Agent 的来源。

需要整理：

- 基因：编码基因、rRNA、tRNA、sRNA、调控区域。
- 蛋白：单体蛋白、转运蛋白、酶、转录因子。
- 小分子：原生营养物质、代谢物、辅因子。
- 复合体：蛋白复合体、蛋白-DNA 复合体、小分子-蛋白复合体。

每个实体至少需要：

```text
entity_id
entity_type
name
aliases
annotation
source_database
source_id
```

后续可增加：

```text
subcellular_location
default_state
pathways
external_ids
is_external
complex_type
is_virtual
components
critical_components
assembly_condition
```

复合物统一进入 `entities.csv`，但分两类行为：

- `complex_type=structural`: 结构性大型复合物，不参与 LLM 决策，状态由组成成分自动计算。
- `complex_type=regulatory`: 调控性小型复合物，参与 LLM 决策，组装/解聚是调控事件。

### 2. 关系信息

这是知识图谱的主干。

需要整理：

- 基因编码哪些蛋白。
- 蛋白催化哪些反应。
- 小分子是哪些蛋白/反应的底物或产物。
- 转录因子激活或抑制哪些基因。
- 蛋白或小分子之间是否结合。
- 哪些蛋白形成复合体。
- 哪些实体属于某条通路。

推荐关系类型：

```text
encodes
catalyzes
transports
activates
represses
binds
inhibits
forms_complex
is_substrate_of
is_product_of
is_component_of
is_critical_for
participates_in
```

其中 `is_substrate_of` 和 `is_product_of` 很重要，因为代谢物 Agent 需要知道谁在消耗它、谁在产生它。

`is_component_of` 和 `is_critical_for` 用于复合物 Agent：

```text
rpsA --is_component_of--> ribosome_70S
rpsA --is_critical_for--> ribosome_70S
LacI --is_component_of--> LacI_lacO_complex
lacO --is_component_of--> LacI_lacO_complex
```

### 3. 代谢通路与反应信息

这是小分子和蛋白之间互动的骨架。

需要整理：

- 通路名称。
- 通路包含哪些反应。
- 每个反应的底物和产物。
- 哪些酶催化该反应。
- 反应所在细胞区域。

在本项目中，代谢反应不用于数值计算，而是转成图谱边：

```text
enzyme --catalyzes--> reaction
substrate --is_substrate_of--> enzyme/reaction
product --is_product_of--> enzyme/reaction
entity --participates_in--> pathway
```

主要来源：

- KEGG
- EcoCyc
- BiGG / iML1515，作为补充图谱，不运行 FBA

### 4. 转录调控信息

这是基因状态变化的关键。

需要整理：

- 哪个转录因子调控哪个基因或操纵子。
- 调控方向是激活还是抑制。
- 是否需要小分子配体。
- 操纵子、启动子、转录单元关系。

转成图谱边：

```text
TF --activates/represses--> gene
small_molecule --binds/modulates--> TF
gene --belongs_to--> operon
operon --controls--> genes
```

主要来源：

- RegulonDB
- EcoCyc

### 5. 蛋白功能与注释信息

这是 Agent “自我描述”的来源。

需要整理：

- 蛋白名称。
- 对应基因。
- 功能描述。
- EC number。
- GO terms。
- 结合位点、辅因子、催化活性。
- 亚细胞定位。

主要来源：

- UniProt
- EcoCyc

### 6. 小分子标准化信息

小分子名称容易混乱，需要统一 ID。

需要整理：

- 标准名称。
- 同义词。
- KEGG Compound ID。
- ChEBI ID。
- PubChem ID。
- 分子类别：营养、代谢物、辅因子。

注意：

外源药物和外源诱导物暂时不进入 `entities.csv`，也不需要单独整理成系统表。它们以后作为扰动提示词输入，例如“加入氨苄青霉素”或“加入 IPTG”，再由扰动解析层根据功能注释和知识图谱判断受影响的原生实体。

主要来源：

- KEGG Compound
- ChEBI
- PubChem

### 7. 转运与空间定位信息

如果后面要模拟药物进入、营养摄取、膜蛋白作用，就需要空间信息。

需要整理：

- 蛋白定位：胞质、内膜、周质、外膜、胞外。
- 小分子可出现的位置。
- 哪些蛋白负责转运哪些小分子。

主要来源：

- UniProt localization
- EcoCyc transport reactions
- PSORTdb，作为定位补充

### 8. 响应模式和验证信息

这是 ReportAgent 做“最终状态组合像什么”的可选对照依据，不参与仿真传导。

需要整理：

- 已知突变体响应模式。
- 药物处理响应模式。
- 营养切换响应模式。
- 必需基因信息。
- 数据库中的经典注释和条件实验结论。

第一版可以先手工写少量响应模式。

例子：

```text
protein.P02918 inhibited + protein.P0AD68 inhibited
=> beta_lactam_cell_wall_response
```

主要来源：

- EcoCyc phenotype
- RegulonDB 条件实验
- Keio collection / 必需基因数据库

### 9. 外源扰动输入

外源扰动暂时不作为静态数据整理。

后续实验时，用户用自然语言输入扰动，系统再解析成对原生实体的状态影响。

例子：

```text
加入氨苄青霉素 -> 根据功能注释判断 PBP 相关蛋白受影响
加入 IPTG -> 根据功能注释判断 LacI/lac 操纵子相关实体受影响
加入氯霉素 -> 根据功能注释判断核糖体/翻译相关实体受影响
敲除 lacI -> gene.lacI 状态改变
```

这些影响不直接写死为静态表，而是在扰动解析阶段产生本次实验的初始状态变更。

## 数据优先级

### MVP 必须整理

只围绕乳糖操纵子。

需要：

- lacI、lacZ、lacY、lacA、crp、cyaA 等基因。
- LacI、LacZ、LacY、LacA、CRP、RNAP 等蛋白。
- lactose、allolactose、glucose、cAMP 等原生小分子。
- LacI 对 lac 操纵子的抑制关系。
- allolactose 对 LacI 的影响。
- cAMP-CRP 对 lac 操纵子的激活关系。
- glucose 对 cAMP-CRP 的间接影响。
- lac operon 诱导相关表型标签。

### 第二阶段整理

扩展到小型细胞图谱。

需要：

- 中心碳代谢核心反应。
- 葡萄糖摄取相关系统。
- 乳糖转运和分解相关反应。
- cAMP-CRP 调控的更多基因。
- 少量抗生素或应激响应模块。

### 第三阶段整理

扩展到全 MG1655。

需要：

- 全基因列表。
- 全蛋白列表。
- 主要代谢物列表。
- 主要通路列表。
- 全转录调控网络。
- 主要转运反应。
- 主要蛋白复合体。
- 表型和验证数据。

## 推荐数据源

| 数据类型 | 主要来源 | 用途 |
| --- | --- | --- |
| 基因组注释 | NCBI RefSeq | 建立基因 Agent |
| 蛋白功能 | UniProt | 建立蛋白 Agent 注释 |
| 大肠杆菌通路和反应 | EcoCyc | 构建高质量细菌知识图谱 |
| 代谢通路 | KEGG | 构建通路拓扑 |
| 转录调控 | RegulonDB | 构建调控边 |
| 小分子 ID | ChEBI / KEGG Compound | 标准化小分子 Agent |
| 代谢模型 | BiGG iML1515 | 补充反应和代谢物关系 |
| 蛋白定位 | UniProt / PSORTdb | 建立空间约束 |
| 蛋白互作 | EcoCyc / Complex Portal / STRING | 补充复合体和 PPI |

## 全量数据获取方法

全量整理建议做成自动化管线，而不是手工整理。

### A. 我可以直接自动获取的数据

这些数据源公开接口相对稳定，可以先由脚本自动下载和解析：

| 数据 | 来源 | 产出 |
| --- | --- | --- |
| 全基因、RNA、蛋白基础注释 | NCBI RefSeq `GCF_000005845.2` | gene/rRNA/tRNA/sRNA/protein 基础实体 |
| 蛋白功能、EC、GO、定位、外部 ID | UniProt proteome `UP000000625` | protein 实体注释 |
| 代谢通路、反应、酶、化合物链接 | KEGG REST `eco` | pathway、reaction、enzyme、compound 边 |
| 小分子标准名和同义词 | KEGG Compound / ChEBI | small_molecule 实体 |
| 代谢模型关系 | BiGG iML1515 或 Ecoli-GEM | GPR、reaction、metabolite、compartment 边 |

### B. 最好由你提供下载包的数据

这些数据对质量很关键，但完整下载可能涉及账号、许可或网页手动下载：

| 数据 | 来源 | 用途 |
| --- | --- | --- |
| 高质量大肠杆菌通路、反应、复合物、调控 | EcoCyc | 最核心的综合知识图谱 |
| 转录调控、操纵子、启动子、TF binding | RegulonDB | 调控边和 operon 结构 |

RegulonDB 你已经提供了 TSV 文件，当前已经解析并合并了 regulator-gene 和 sigma-gene 两类 confirmed/strong 调控边。下一步如果继续深化 RegulonDB，就解析 TU、operon、promoter 和 binding-site 层级。

EcoCyc/BioCyc 许可已经拿到。不要把邮件里的保密下载 URL、用户名或密码写进仓库；用环境变量传给下载脚本：

```bash
export BIOCYC_FLATFILES_URL="..."
export BIOCYC_FLATFILES_USER="..."
export BIOCYC_FLATFILES_PASSWORD="..."
python3 scripts/fetch_ecocyc_flatfiles.py --dry-run
python3 scripts/fetch_ecocyc_flatfiles.py
```

下载后的文件放在：

```text
data/raw/ecocyc/
```

优先解析这些 EcoCyc 内容：

```text
protcplx.dat              -> complex 实体、is_component_of、is_critical_for
reactions.dat/enzrxns.dat -> 反应、催化、底物、产物、方向和条件
pathways.dat              -> EcoCyc 通路元信息
compounds.dat             -> 小分子同义词和数据库交叉 ID
proteins.dat/genes.dat    -> UniProt/RefSeq/RegulonDB ID 对齐增强
promoters.dat/transcription-units.dat/regulation.dat
                           -> operon/TU/promoter/regulatory-region 结构
```

### C. 可选补充数据

| 数据 | 来源 | 用途 |
| --- | --- | --- |
| 蛋白复合体 | Complex Portal / EcoCyc / STRING | 补充 `complex` 实体和 component 边 |
| 蛋白互作 | STRING / IntAct / BioGRID | 候选 PPI 边，置信度需要保留 |
| 定位预测/注释 | PSORTdb / UniProt | 空间约束 |
| 响应模式验证 | Keio collection / EcoCyc phenotype | 报告阶段的响应模式对照 |

## 建议自动管线

建议新增：

```text
scripts/
  download_sources.py
  build_entities.py
  build_edges.py
  build_pathways.py
  build_graph.py
  extract_subgraph.py
data/
  raw/
  normalized/
  graph/
  seed/
```

工作流：

```text
download_sources.py
  -> 下载 NCBI/UniProt/KEGG/ChEBI/BiGG 原始数据

build_entities.py
  -> 生成全量 entities.csv

build_edges.py
  -> 生成全量 edges.csv

build_pathways.py
  -> 生成 pathways.csv

build_graph.py
  -> 合并成 graph.json

extract_subgraph.py
  -> 从全量图谱抽取 lac_operon、cell_wall、ribosome 等实验子图
```

第一版可以先不等 EcoCyc 完整包：

1. 先用 NCBI + UniProt + KEGG + RegulonDB 生成基础全量图谱。
2. 用 lac operon seed 验证仿真闭环。
3. 你提供 EcoCyc 后，再增强复合物、转运、反应细节和表型质量。

## 最终应该产出的数据文件

不需要一开始设计复杂数据库。第一版只要能产出这些 JSON/CSV 即可：

```text
entities.csv          # 所有 Agent 节点
edges.csv             # Agent 之间的关系边
pathways.csv          # 通路信息
data/phenotypes/phenotype_db.yaml   # 可选响应模式对照库
initial_states.csv    # 初始状态
graph.json            # 本次仿真使用的图谱快照
```

## 对应到仿真系统

这些数据进入系统后，对应关系是：

```text
entities.csv -> 初始化 Agent
edges.csv -> 决定 Agent 邻居
pathways.csv -> 保存通路元信息
data/phenotypes/phenotype_db.yaml -> 报告阶段匹配已知响应模式
initial_states.csv -> 设置仿真起点
graph.json -> 保存本次仿真的世界快照
```

## 建议的实际顺序

1. 手工整理 lac operon 的 `entities.csv` 和 `edges.csv`。
2. 手工写 3-5 条响应模式到 `data/phenotypes/phenotype_db.yaml`。
3. 跑通仿真和 ReportAgent。
4. 再加入扰动解析层，把自然语言扰动转成本次实验的初始状态变更。
5. 再从 UniProt/RegulonDB/KEGG 自动补数据。
6. 最后才考虑全 MG1655 数据整合。

## 当前已开始整理

第一份实体目录已经放在：

```text
data/seed/lac_operon/entities.csv
```

它先覆盖乳糖操纵子原型所需的基因、蛋白、小分子、调控区域和复合体。下一步应在同一目录补充：

```text
edges.csv
pathways.csv
initial_states.csv
data/phenotypes/phenotype_db.yaml
```

## 当前公开/手动数据已获取

我已经先用公开 API/FTP 和你提供的 RegulonDB 文件生成了第一版全量基础数据：

```text
data/raw/uniprot/
data/raw/kegg/
data/raw/ncbi_refseq/
data/regulationDB/
data/normalized/entities.csv
data/normalized/ncbi_entities.csv
data/normalized/regulondb_edges.csv
data/normalized/regulondb_skipped.tsv
data/normalized/edges.csv
data/normalized/pathways.csv
```

当前规模：

```text
entities.csv: 13194 entities
  protein: 4403
  small_molecule: 3480
  reaction: 590
  gene: 4506
  rna: 215

edges.csv: 27232 edges
  participates_in: 9867
  catalyzes: 4415
  encodes: 4402
  activates: 3721
  represses: 2356
  is_product_of: 1307
  is_substrate_of: 1164

pathways.csv: 137 pathways
```

这部分包含 UniProt、KEGG、NCBI RefSeq 和 RegulonDB 数据。代谢骨架已经具备初步传播能力：蛋白可通过催化边连接 reaction，reaction 可通过底物/产物边连接 small molecule。调控骨架也已经具备初步传播能力：RegulonDB 的 regulator/sigma 可通过 `activates` 和 `represses` 连接到目标 gene。

仍需要补齐的是复合物组成、operon/promoter/TF binding 细结构、转运、PPI、结合/抑制、以及表型验证规则。其中 EcoCyc 是下一块最值得补的数据。
