---
entity_id: "protein.P0A836"
entity_type: "protein"
name: "sucC"
source_database: "UniProt"
source_id: "P0A836"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sucC b0728 JW0717"
---

# sucC

`protein.P0A836`

## Static

- Type: `protein`
- Source: `UniProt:P0A836`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Succinyl-CoA synthetase functions in the citric acid cycle (TCA), coupling the hydrolysis of succinyl-CoA to the synthesis of either ATP or GTP and thus represents the only step of substrate-level phosphorylation in the TCA. The beta subunit provides nucleotide specificity of the enzyme and binds the substrate succinate, while the binding sites for coenzyme A and phosphate are found in the alpha subunit. Can use either ATP or GTP, but prefers ATP. It can also function in the other direction for anabolic purposes, and this may be particularly important for providing succinyl-CoA during anaerobic growth when the oxidative route from 2-oxoglutarate is severely repressed. {ECO:0000255|HAMAP-Rule:MF_00558, ECO:0000269|PubMed:10353839}. SucC is the β subunit of succinyl-CoA synthetase. Trp45 and His50 are required for activity , while Cys47 and Cys325 are not essential. Single mutations of tryptophan residues W43, W76 and W248 have little effect on enzyme activity. W76 and W248 may be part of the CoA binding site . Glu197 is essential for phosphorylation and dephosphorylation of the active site His246 in the α subunit . SucC was identified as a putative phosphohistidine acceptor using chemoproteomics analysis with a stable analogue of 3-pHis...

## Biological Role

Catalyzes succinate:CoA ligase (ADP-forming) (reaction.R00405), itaconate:CoA ligase (ADP-forming) (reaction.R02404). Component of succinyl-CoA synthetase (complex.ecocyc.SUCCCOASYN).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Succinyl-CoA synthetase functions in the citric acid cycle (TCA), coupling the hydrolysis of succinyl-CoA to the synthesis of either ATP or GTP and thus represents the only step of substrate-level phosphorylation in the TCA. The beta subunit provides nucleotide specificity of the enzyme and binds the substrate succinate, while the binding sites for coenzyme A and phosphate are found in the alpha subunit. Can use either ATP or GTP, but prefers ATP. It can also function in the other direction for anabolic purposes, and this may be particularly important for providing succinyl-CoA during anaerobic growth when the oxidative route from 2-oxoglutarate is severely repressed. {ECO:0000255|HAMAP-Rule:MF_00558, ECO:0000269|PubMed:10353839}.

## Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00405|reaction.R00405]] `KEGG` `database` - via EC:6.2.1.5
- `catalyzes` --> [[reaction.R02404|reaction.R02404]] `KEGG` `database` - via EC:6.2.1.5
- `is_component_of` --> [[complex.ecocyc.SUCCCOASYN|complex.ecocyc.SUCCCOASYN]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0728|gene.b0728]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A836`
- `KEGG:ecj:JW0717;eco:b0728;ecoc:C3026_03645;`
- `GeneID:93776757;945312;`
- `GO:GO:0000287; GO:0004775; GO:0004776; GO:0005524; GO:0005737; GO:0005829; GO:0006099; GO:0006104; GO:0009361; GO:0042709`
- `EC:6.2.1.5`

## Notes

Succinate--CoA ligase [ADP-forming] subunit beta (EC 6.2.1.5) (Succinyl-CoA synthetase subunit beta) (SCS-beta)
