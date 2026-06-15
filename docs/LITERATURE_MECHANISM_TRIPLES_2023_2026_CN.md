# 近三年大肠杆菌机制文献与可落图三元组

整理日期：2026-06-15  
范围：2023-06 至 2026-06，优先收录原始研究。  
用途：为仿真知识图谱补充带文献来源的条件触发机制边，覆盖基因调控、药物/抗生素响应、应激/饥饿响应、代谢/碳源切换。

## 使用原则

这些文献边不建议直接混入 STRING 边。STRING 更像背景互作强度，这里整理的是条件触发的机制证据，适合单独落到：

```text
data/curated/literature_mechanism_edges.csv
```

建议字段：

```text
source_entity,relation,target_entity,condition,perturbation,effect,confidence,evidence_type,pmid,doi,note
```

仿真中可用：

```text
edge_weight = literature_confidence * condition_match_score
```

证据强度建议：

| tier | 含义 | 建议用途 |
|---|---|---|
| direct | 遗传扰动、报告基因、成像、结构、生化直接支持 | 可作为硬机制边或高权重条件边 |
| omics | RNA-seq、proteomics、metabolomics、ICA 等系统证据 | 可作为中等权重边或模块状态 |
| model_or_review | 模型、综述、二级综合 | 只作调度提示、模块注释或待验证候选 |
| preprint | 预印本 | 可先入候选库，不建议直接覆盖现有硬边 |

## 一、优先入库机制

| 优先级 | 机制模块 | 推荐三元组 | 为什么适合仿真 |
|---|---|---|---|
| P0 | CsrA 酸胁迫 | `CsrA represses evgA/gadE/gadA/gadB/ydeO` | 方向清楚，能连接 growth-survival tradeoff |
| P0 | OxyR 氧化胁迫 | `H2O2 activates OxyR`; `OxyR activates katG/ahpC/grxA/...` | 有时间动力学类别，适合 round-based 传播 |
| P0 | ppGpp/RNAP/ciprofloxacin | `ciprofloxacin activates ppGpp`; `ppGpp-RNAP promotes mutable_gambler_cells` | 能解释抗生素诱导突变和持留 |
| P0 | 代谢状态调孔蛋白 | `lipid_growth decreases porin_permeability`; `glucose_high_metabolism activates Kch` | 连接碳源、膜通透性、抗生素进入 |
| P1 | Crp-cAMP persister | `Crp-cAMP redirects metabolism_to_oxidative_phosphorylation` | 适合做 persister 状态门控 |
| P1 | nutrient stress sRNA | `ArcA activates csrB`; `PhoP activates csrC`; `OxyR regulates gcvB`; `ArcA regulates gadY` | 补足 sRNA 调控层 |
| P1 | bioenergetic stress | `bioenergetic_stress increases ROS`; `bioenergetic_stress activates stringent_response` | 连接 ATP/NADH、ROS、突变、持留 |
| P2 | arginine + florfenicol | `arginine inhibits AST_pathway`; `arginine inhibits AcrAB-TolC/EmrAB-TolC_efflux` | 适合作为外源扰动库条目 |
| P2 | HNQ 胞外呼吸 | `HNQ redox_cycles_via NfsA/NfsB`; `OmpC_adaptation increases EET` | 特殊环境场景，不是默认胞内状态 |
| P2 | sulfoglycolysis | `sulfoquinovose_catabolism diverts triose_phosphate_to_gluconeogenesis` | 碳源切换场景 |

## 二、机制三元组明细

### 1. 基因调控

| 状态/扰动 | 可落图三元组 | 证据强度 | 文献来源 |
|---|---|---|---|
| nutrient stress, glucose/amino acid starvation | `nutrient_stress changes EPOD/chromatin_occupancy`; `EPOD_state represses_or_permits condition_specific_genes` | omics/direct mixed | Ekdahl et al., 2025, Nucleic Acids Research. PMID: [40671525](https://pubmed.ncbi.nlm.nih.gov/40671525/). DOI: [10.1093/nar/gkaf647](https://doi.org/10.1093/nar/gkaf647) |
| nutrient stress | `ArcA activates csrB`; `PhoP activates csrC`; `OxyR regulates gcvB`; `ArcA regulates gadY` | direct promoter mutant/Miller assay | Ekdahl et al., 2025, Nucleic Acids Research. PMID: [40671525](https://pubmed.ncbi.nlm.nih.gov/40671525/). DOI: [10.1093/nar/gkaf647](https://doi.org/10.1093/nar/gkaf647) |
| mild acid / extreme acid | `CsrA translationally_represses evgA`; `CsrA represses gadA`; `CsrA represses gadB`; `CsrA represses gadE`; `CsrA represses ydeO` | direct RNA binding/reporters | Yakhnin et al., 2024, Journal of Bacteriology. PMID: [38319100](https://pubmed.ncbi.nlm.nih.gov/38319100/). DOI: [10.1128/jb.00354-23](https://doi.org/10.1128/jb.00354-23) |
| acid stress tradeoff | `csrA_loss increases acid_survival`; `csrA_loss decreases growth_at_mild_acid` | direct phenotype | Yakhnin et al., 2024, Journal of Bacteriology. PMID: [38319100](https://pubmed.ncbi.nlm.nih.gov/38319100/). DOI: [10.1128/jb.00354-23](https://doi.org/10.1128/jb.00354-23) |
| H2O2 | `H2O2 oxidizes/activates OxyR`; `OxyR activates_pulsatile katG/yaaA/clpS/hemH/uxuA/poxB/yaiA`; `OxyR activates_gradual grxA/trxC/fur/ahpC` | direct single-cell reporter | Choudhary et al., 2024, Cell Systems. PMID: [39541985](https://pubmed.ncbi.nlm.nih.gov/39541985/). DOI: [10.1016/j.cels.2024.10.003](https://doi.org/10.1016/j.cels.2024.10.003) |
| AZT / replication inhibition | `AZT activates SOS_genes`; `LexA indirectly_regulates pyrimidine_pathway_genes`; `SspA required_for AZT_induced_gene_program`; `AZT induces sRNA_genes` | direct RNA-seq/genetics | Sass et al., 2024, PNAS. PMID: [38935560](https://pubmed.ncbi.nlm.nih.gov/38935560/). DOI: [10.1073/pnas.2407832121](https://doi.org/10.1073/pnas.2407832121) |

### 2. 药物和抗生素响应

| 状态/扰动 | 可落图三元组 | 证据强度 | 文献来源 |
|---|---|---|---|
| ciprofloxacin | `ciprofloxacin induces ppGpp`; `ppGpp_RNAP_site1 activates DNA_damage_response`; `ppGpp_RNAP_site2 activates sigmaS_response`; `RNAP_backtracking promotes mutable_gambler_cells` | direct genetics/mechanism | Zhai et al., 2023, Molecular Cell. PMID: [36965481](https://pubmed.ncbi.nlm.nih.gov/36965481/). DOI: [10.1016/j.molcel.2023.03.003](https://doi.org/10.1016/j.molcel.2023.03.003) |
| mecillinam / beta-lactam | `(p)ppGpp modifies RNAP_function`; `RNAP/rRNA_program_shift confers beta_lactam_resistance`; note: `peptidoglycan-independent` | direct | Voedts et al., 2024, Nature Microbiology. PMID: [38443580](https://pubmed.ncbi.nlm.nih.gov/38443580/). DOI: [10.1038/s41564-024-01609-w](https://doi.org/10.1038/s41564-024-01609-w) |
| ATP/NADH hydrolysis, ciprofloxacin | `bioenergetic_stress increases ROS`; `ROS activates mutagenic_break_repair`; `bioenergetic_stress activates stringent_response`; `stringent_response increases persistence` | direct synthetic biology/metabolomics | Li et al., 2025, Nature Communications. PMID: [40490453](https://pubmed.ncbi.nlm.nih.gov/40490453/). DOI: [10.1038/s41467-025-60302-6](https://doi.org/10.1038/s41467-025-60302-6) |
| starvation/lipid/glucose state affects antibiotics | `starvation lowers_periplasmic_H+`; `low_periplasmic_H+ increases porin_permeability`; `lipid_growth causes periplasmic_acidification`; `periplasmic_acidification decreases porin_permeability`; `glucose_high_metabolism activates Kch`; `Kch increases periplasmic_K+`; `periplasmic_K+ increases porin_permeability`; `lipid_catabolism increases ciprofloxacin_resistance` | direct single-cell imaging/genetics | 2025, Nature Microbiology. PMID: [41286116](https://pubmed.ncbi.nlm.nih.gov/41286116/). DOI: [10.1038/s41564-025-02175-5](https://doi.org/10.1038/s41564-025-02175-5) |
| ciprofloxacin early adaptation | `argI_regulatory_mutation modulates arginine_metabolism`; `narU_regulatory_mutation modulates carbohydrate/anaerobic_metabolism`; `metabolic_regulatory_mutations increase ATP_production_under_ciprofloxacin` | direct evolution/WGS | Pal et al., 2024, Nucleic Acids Research. PMID: [39180403](https://pubmed.ncbi.nlm.nih.gov/39180403/). DOI: [10.1093/nar/gkae719](https://doi.org/10.1093/nar/gkae719) |
| arginine + florfenicol | `arginine inhibits AST_pathway`; `AST_inhibition decreases fatty_acid_beta_oxidation`; `free_fatty_acid_accumulation damages membrane`; `arginine inhibits AcrAB-TolC_efflux`; `arginine inhibits EmrAB-TolC_efflux`; `efflux_inhibition increases intracellular_florfenicol` | direct in vitro/in vivo, non-K12 caution | 2026, Virulence. PMID: [42047263](https://pubmed.ncbi.nlm.nih.gov/42047263/). DOI: [10.1080/21505594.2026.2666994](https://doi.org/10.1080/21505594.2026.2666994) |

### 3. 应激和饥饿响应

| 状态/扰动 | 可落图三元组 | 证据强度 | 文献来源 |
|---|---|---|---|
| nutrient starvation | `(p)ppGpp increases IncA_homolog_activity`; `IncA_homolog interacts_with DnaN`; `IncA_homolog delocalizes DnaN`; `DnaN_delocalization inhibits DNA_replication_progression` | direct, cross-species with E. coli homolog note | 2025, Current Biology. PMID: [41075781](https://pubmed.ncbi.nlm.nih.gov/41075781/). DOI: [10.1016/j.cub.2025.09.042](https://doi.org/10.1016/j.cub.2025.09.042) |
| H2O2 oxidative stress | `OxyR_binding_kinetics determines pulsatile_or_gradual_response`; `pulsatile_response provides early_protection`; `gradual_response provides lasting_population_protection` | direct single-cell/model | Choudhary et al., 2024, Cell Systems. PMID: [39541985](https://pubmed.ncbi.nlm.nih.gov/39541985/). DOI: [10.1016/j.cels.2024.10.003](https://doi.org/10.1016/j.cels.2024.10.003) |
| replication inhibition | `replication_block activates LexA_SOS_arm`; `replication_block activates SspA_dependent_arm`; `IraD/IraM links DNA_damage_to_RpoS_axis` | direct RNA-seq | Sass et al., 2024, PNAS. PMID: [38935560](https://pubmed.ncbi.nlm.nih.gov/38935560/). DOI: [10.1073/pnas.2407832121](https://doi.org/10.1073/pnas.2407832121) |
| acid stress | `mild_acid activates EvgAS_circuit`; `EvgA/YdeO/GadE activates GDAR_genes`; `GDAR increases acid_survival`; `CsrA represses this circuit` | direct and curated from article mechanism | Yakhnin et al., 2024, Journal of Bacteriology. PMID: [38319100](https://pubmed.ncbi.nlm.nih.gov/38319100/). DOI: [10.1128/jb.00354-23](https://doi.org/10.1128/jb.00354-23) |

### 4. 代谢和碳源切换

| 状态/扰动 | 可落图三元组 | 证据强度 | 文献来源 |
|---|---|---|---|
| late stationary persisters | `Crp-cAMP redirects metabolism_to_oxidative_phosphorylation`; `oxidative_phosphorylation supports persister_survival`; `persisters retain reduced_but_required_energy_metabolism` | direct multi-omics/deletion analysis | 2025, eLife. PMID: [40627543](https://pubmed.ncbi.nlm.nih.gov/40627543/). DOI: [10.7554/eLife.99735](https://doi.org/10.7554/eLife.99735) |
| HNQ + extracellular electrode, no electron sink | `HNQ redox_cycles_via NfsA`; `HNQ redox_cycles_via NfsB`; `NfsA/NfsB enables extracellular_electron_transfer`; `OmpC_adaptation increases HNQ_mediated_EET` | direct systems biology/electrochemistry | 2025, Cell. PMID: [40215961](https://pubmed.ncbi.nlm.nih.gov/40215961/). DOI: [10.1016/j.cell.2025.03.016](https://doi.org/10.1016/j.cell.2025.03.016) |
| sulfoquinovose instead of glucose | `sulfoquinovose_catabolism diverts triose_phosphate_to_gluconeogenesis`; `sulfoglycolysis increases trehalose_storage`; `sulfoglycolysis increases glycogen_storage`; `sulfoglycolysis produces/excretes DHPS` | direct metabolomics | 2023, Applied and Environmental Microbiology. PMID: [36728421](https://pubmed.ncbi.nlm.nih.gov/36728421/). DOI: [10.1128/aem.02016-22](https://doi.org/10.1128/aem.02016-22) |
| glycolate as carbon source | `glycolate enables growth_as_sole_carbon_source`; `strain_background affects glycolate_adaptation_lag`; `overexpression_of_glycolate_degradation_genes does_not_improve_growth` | direct physiology, weaker mechanism | 2024, Journal of Biotechnology. PMID: [38190849](https://pubmed.ncbi.nlm.nih.gov/38190849/). DOI: [10.1016/j.jbiotec.2024.01.001](https://doi.org/10.1016/j.jbiotec.2024.01.001) |
| lipid/glucose/starvation metabolic state | `lipid_growth decreases antibiotic_entry_via_porin_closing`; `glucose_high_metabolism opens_porin_via_Kch`; `starvation opens_porin_for_nutrient_uptake` | direct | 2025, Nature Microbiology. PMID: [41286116](https://pubmed.ncbi.nlm.nih.gov/41286116/). DOI: [10.1038/s41564-025-02175-5](https://doi.org/10.1038/s41564-025-02175-5) |

## 三、推荐落图格式

### CSV 示例

```csv
source_entity,relation,target_entity,condition,perturbation,effect,confidence,evidence_type,pmid,doi,note
CsrA,represses,evgA,mild_acid,,decrease_translation,0.90,direct,38319100,10.1128/jb.00354-23,translational repression via evgL coupling
H2O2,activates,OxyR,oxidative_stress,H2O2,oxidized_active_OxyR,0.90,direct,39541985,10.1016/j.cels.2024.10.003,single-cell temporal response
bioenergetic_stress,increases,ROS,antibiotic_stress,ATP_or_NADH_hydrolysis,increased_mutagenesis,0.85,direct,40490453,10.1038/s41467-025-60302-6,links resistance evolution and persistence
lipid_growth,decreases,porin_permeability,lipid_media,,reduced_ciprofloxacin_entry,0.85,direct,41286116,10.1038/s41564-025-02175-5,periplasmic acidification
Crp-cAMP,redirects,oxidative_phosphorylation,late_stationary_persister,,persister_survival,0.80,direct,40627543,10.7554/eLife.99735,energy metabolism remains required
```

### YAML 示例

```yaml
- source: CsrA
  relation: represses
  target: evgA
  condition: mild_acid
  evidence:
    pmid: "38319100"
    doi: "10.1128/jb.00354-23"
    tier: direct
  simulator:
    edge_weight: 0.90
    trigger: "pH <= 5.5 or acid_stress"
    effect: "target translation decreases"
```

## 四、入库注意事项

1. 不要把外源药物和特殊底物放进默认初始胞内状态。`arginine + florfenicol`、`HNQ + electrode`、`sulfoquinovose` 应作为扰动或环境条件。
2. 三元组里的 `condition` 很关键。同一条边在不同条件下可能方向不同，例如 OxyR-GcvB 在不同培养基中有差异。
3. `review` 和 `omics` 证据不要覆盖 RegulonDB/EcoCyc 的硬边，只做权重调节或候选边。
4. `PMID 41075781` 的 starvation-triggered IncA 机制主要来自 Caulobacter，并验证了 E. coli homolog 的能力，入图时应标注 `cross_species_homolog_evidence`。
5. STRING 边不能替代这些机制边。STRING 适合背景邻接和调度先验，这些文献三元组适合条件触发和报告解释。

## 五、下一步建议

1. 先把 P0/P1 文献转为 `data/curated/literature_mechanism_edges.csv`。
2. 运行 entity grounding，把 `CsrA/OxyR/Crp/ArcA/PhoP/Kch/OmpC/NfsA/NfsB/RelA/SpoT/RNAP` 对齐到当前 KG id。
3. 对每条边加 `condition_gate`，避免在 glucose log phase 默认唤醒外源或特殊环境机制。
4. 把 `drug -> metabolic_state -> porin_permeability -> antibiotic_entry` 做成一个验证场景，特别适合测试 LLM Agent 是否能从代谢状态推出药物响应差异。
