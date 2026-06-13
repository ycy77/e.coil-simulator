---
entity_id: "protein.P0AGE9"
entity_type: "protein"
name: "sucD"
source_database: "UniProt"
source_id: "P0AGE9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sucD b0729 JW0718"
---

# sucD

`protein.P0AGE9`

## Static

- Type: `protein`
- Source: `UniProt:P0AGE9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Succinyl-CoA synthetase functions in the citric acid cycle (TCA), coupling the hydrolysis of succinyl-CoA to the synthesis of either ATP or GTP and thus represents the only step of substrate-level phosphorylation in the TCA. The alpha subunit of the enzyme binds the substrates coenzyme A and phosphate, while succinate binding and nucleotide specificity is provided by the beta subunit. Can use either ATP or GTP, but prefers ATP. It can also function in the other direction for anabolic purposes, and this may be particularly important for providing succinyl-CoA during anaerobic growth when the oxidative route from 2-oxoglutarate is severely repressed. {ECO:0000255|HAMAP-Rule:MF_01988, ECO:0000269|PubMed:10353839}. SucD is the α subunit of succinyl-CoA synthetase. His246 is the phosphorylated residue of the reaction intermediate. A His246Asp mutant can not autophosphorylate and has no catalytic activity . A His142 mutant is catalytically inactive for the overall reaction, but the enzyme can be phosphorylated with ATP and dephosphorylated with succinate . Glu208 is essential for phosphorylation and dephosphorylation of His246 . The conserved Cys123 is not required for catalytic activity...

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

FUNCTION: Succinyl-CoA synthetase functions in the citric acid cycle (TCA), coupling the hydrolysis of succinyl-CoA to the synthesis of either ATP or GTP and thus represents the only step of substrate-level phosphorylation in the TCA. The alpha subunit of the enzyme binds the substrates coenzyme A and phosphate, while succinate binding and nucleotide specificity is provided by the beta subunit. Can use either ATP or GTP, but prefers ATP. It can also function in the other direction for anabolic purposes, and this may be particularly important for providing succinyl-CoA during anaerobic growth when the oxidative route from 2-oxoglutarate is severely repressed. {ECO:0000255|HAMAP-Rule:MF_01988, ECO:0000269|PubMed:10353839}.

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

- `encodes` <-- [[gene.b0729|gene.b0729]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGE9`
- `KEGG:ecj:JW0718;eco:b0729;ecoc:C3026_03650;`
- `GeneID:86863239;93776756;945314;`
- `GO:GO:0000166; GO:0004775; GO:0004776; GO:0005737; GO:0005829; GO:0006099; GO:0009361`
- `EC:6.2.1.5`

## Notes

Succinate--CoA ligase [ADP-forming] subunit alpha (EC 6.2.1.5) (Succinyl-CoA synthetase subunit alpha) (SCS-alpha)
