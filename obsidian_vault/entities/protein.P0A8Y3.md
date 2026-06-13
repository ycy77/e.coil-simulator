---
entity_id: "protein.P0A8Y3"
entity_type: "protein"
name: "yihX"
source_database: "UniProt"
source_id: "P0A8Y3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yihX b3885 JW5566"
---

# yihX

`protein.P0A8Y3`

## Static

- Type: `protein`
- Source: `UniProt:P0A8Y3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dephosphorylation of alpha-D-glucose 1-phosphate (Glc1P) and, to a lesser extent, of other sugar phosphates (PubMed:16990279, PubMed:25484615). Has no activity with the beta form of Glc1P. In addition, YihX has significant phosphatase activity against pyridoxal phosphate (PLP) and low beta-phosphoglucomutase activity (PubMed:16990279). {ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:25484615}. YihX is a phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. It selectively hydrolyzes α-D-glucose-1-phosphate and has no activity with the β form or D-glucose-6-phosphate . In addition, YihX has significant phosphatase activity against pyridoxal phosphate and low β-phosphoglucomutase activity . The phosphatase activity of YihX was first discovered in a high-throughput screen of purified proteins . No measurable sorbitol-6-phosphate phosphatase activity was detected .

## Biological Role

Catalyzes D-glucose-1-phosphate phosphohydrolase (reaction.R00304), GLUCOSE-1-PHOSPHAT-RXN (reaction.ecocyc.GLUCOSE-1-PHOSPHAT-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the dephosphorylation of alpha-D-glucose 1-phosphate (Glc1P) and, to a lesser extent, of other sugar phosphates (PubMed:16990279, PubMed:25484615). Has no activity with the beta form of Glc1P. In addition, YihX has significant phosphatase activity against pyridoxal phosphate (PLP) and low beta-phosphoglucomutase activity (PubMed:16990279). {ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:25484615}.

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00304|reaction.R00304]] `KEGG` `database` - via EC:3.1.3.10
- `catalyzes` --> [[reaction.ecocyc.GLUCOSE-1-PHOSPHAT-RXN|reaction.ecocyc.GLUCOSE-1-PHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3885|gene.b3885]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8Y3`
- `KEGG:ecj:JW5566;eco:b3885;ecoc:C3026_21000;`
- `GeneID:93778053;948380;`
- `GO:GO:0000287; GO:0008877; GO:0030145`
- `EC:3.1.3.10`

## Notes

Alpha-D-glucose 1-phosphate phosphatase YihX (Alpha-D-glucose-1-P phosphatase) (EC 3.1.3.10) (Alpha-D-glucose-1-phosphatase) (Haloacid dehalogenase-like phosphatase 4) (HAD4)
