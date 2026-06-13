---
entity_id: "protein.P0ABQ2"
entity_type: "protein"
name: "garR"
source_database: "UniProt"
source_id: "P0ABQ2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "garR yhaE b3125 JW5526"
---

# garR

`protein.P0ABQ2`

## Static

- Type: `protein`
- Source: `UniProt:P0ABQ2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reduction of tatronate semialdehyde to D-glycerate. {ECO:0000255|HAMAP-Rule:MF_02032, ECO:0000269|PubMed:9772162}. Tartronate semialdehyde reductase (GarR) catalyzes the reduction of tatronate semialdehyde to yield glycerate . GarR is one of two tartronate semialdehyde reductase isozymes in E. coli. Enzymatic activity of tartronate semialdehyde reductase is induced by growth on D-glucarate, D-galactarate, and D-glycerate .

## Biological Role

Catalyzes (R)-glycerate:NAD+ oxidoreductase (reaction.R01745), (R)-glycerate:NADP+ oxidoreductase (reaction.R01747), TSA-REDUCT-RXN (reaction.ecocyc.TSA-REDUCT-RXN).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the reduction of tatronate semialdehyde to D-glycerate. {ECO:0000255|HAMAP-Rule:MF_02032, ECO:0000269|PubMed:9772162}.

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R01745|reaction.R01745]] `KEGG` `database` - via EC:1.1.1.60
- `catalyzes` --> [[reaction.R01747|reaction.R01747]] `KEGG` `database` - via EC:1.1.1.60
- `catalyzes` --> [[reaction.ecocyc.TSA-REDUCT-RXN|reaction.ecocyc.TSA-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3125|gene.b3125]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABQ2`
- `KEGG:ecj:JW5526;eco:b3125;`
- `GeneID:947631;`
- `GO:GO:0008679; GO:0042838; GO:0046392; GO:0046487; GO:0050661; GO:0051287`
- `EC:1.1.1.60`

## Notes

2-hydroxy-3-oxopropionate reductase (EC 1.1.1.60) (Tartronate semialdehyde reductase) (TSAR)
