---
entity_id: "protein.P06989"
entity_type: "protein"
name: "hisI"
source_database: "UniProt"
source_id: "P06989"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hisI hisIE b2026 JW2008"
---

# hisI

`protein.P06989`

## Static

- Type: `protein`
- Source: `UniProt:P06989`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

Histidine biosynthesis bifunctional protein HisIE [Includes: Phosphoribosyl-AMP cyclohydrolase (PRA-CH) (EC 3.5.4.19); Phosphoribosyl-ATP pyrophosphatase (PRA-PH) (EC 3.6.1.31)] HisI is predicted to be a bifunctional enzyme carrying out the second and third steps in the biosynthesis of histidine. Based largely on sequence comparisons with these enzymes in other organisms, HisI is predicted to be a bifunctional enzyme. The carboxy-terminal domain is expected to catalyze the phosphoribosyl-ATP pyrophosphatase reaction, and the amino-terminal domain is expected to carry out the phosphoribosyl-AMP cyclohydrolase reaction . Only the first activity has been functionally demonstrated to exist in E. coli, via crosschecking with the appropriate Salmonella mutant .

## Biological Role

Catalyzes HISTCYCLOHYD-RXN (reaction.ecocyc.HISTCYCLOHYD-RXN), HISTPRATPHYD-RXN (reaction.ecocyc.HISTPRATPHYD-RXN).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

Histidine biosynthesis bifunctional protein HisIE [Includes: Phosphoribosyl-AMP cyclohydrolase (PRA-CH) (EC 3.5.4.19); Phosphoribosyl-ATP pyrophosphatase (PRA-PH) (EC 3.6.1.31)]

## Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.HISTCYCLOHYD-RXN|reaction.ecocyc.HISTCYCLOHYD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.HISTPRATPHYD-RXN|reaction.ecocyc.HISTPRATPHYD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2026|gene.b2026]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06989`
- `KEGG:ecj:JW2008;eco:b2026;ecoc:C3026_11420;`
- `GeneID:946515;`
- `GO:GO:0000105; GO:0004635; GO:0004636; GO:0005524; GO:0005829`
- `EC:3.5.4.19; 3.6.1.31`

## Notes

Histidine biosynthesis bifunctional protein HisIE [Includes: Phosphoribosyl-AMP cyclohydrolase (PRA-CH) (EC 3.5.4.19); Phosphoribosyl-ATP pyrophosphatase (PRA-PH) (EC 3.6.1.31)]
