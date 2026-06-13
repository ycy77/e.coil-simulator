---
entity_id: "protein.P07000"
entity_type: "protein"
name: "pldB"
source_database: "UniProt"
source_id: "P07000"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pldB b3825 JW5584"
---

# pldB

`protein.P07000`

## Static

- Type: `protein`
- Source: `UniProt:P07000`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Peripheral membrane protein.

## Enriched Summary

Lysophospholipase L2 (EC 3.1.1.5) (Lecithinase B) Lysophospholipase L2 (PldB) hydrolyzes the acyl-ester bond of acyl-lysophospholipids. The most effective substrates of the purified enzyme in vitro are 2-acyl glycerophosphoethanolamine and 2-acyl glycerophosphocholine; the 1-acyl versions of each compound are hydrolyzed somewhat less effectively. Purified PldB can also transfer an acyl group from acyl-lysophospholipids to phosphatidylglycerol to yield acyl phosphatidylglycerol; the enzyme is more active with 2-acyl donors (2-acyl glycerophosphoethanolamine and 2-acyl glycerophosphocholine) than 1-acyl donors . PldB does not contain an obvious signal sequence or transmembrane domain and is thought to be associated with the cytoplasmic side of the inner membrane . Mutants with altered lysophospholipase activity have been isolated . PldB: "phospholipid degradation B"

## Biological Role

Catalyzes phosphatidylcholine acylhydrolase (reaction.R01309), 1-acyl-sn-glycero-3-phosphoethanolamine aldehydohydrolase (reaction.R03416), L-2-lysophosphatidylethanolamine aldehydohydrolase (reaction.R03417), 2-lysophosphatidylcholine acylhydrolase (reaction.R07291), RXN-19311 (reaction.ecocyc.RXN-19311), RXN-19312 (reaction.ecocyc.RXN-19312), RXN0-7122 (reaction.ecocyc.RXN0-7122).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

Lysophospholipase L2 (EC 3.1.1.5) (Lecithinase B)

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.R01309|reaction.R01309]] `KEGG` `database` - via EC:3.1.1.5
- `catalyzes` --> [[reaction.R03416|reaction.R03416]] `KEGG` `database` - via EC:3.1.1.5
- `catalyzes` --> [[reaction.R03417|reaction.R03417]] `KEGG` `database` - via EC:3.1.1.5
- `catalyzes` --> [[reaction.R07291|reaction.R07291]] `KEGG` `database` - via EC:3.1.1.5
- `catalyzes` --> [[reaction.ecocyc.RXN-19311|reaction.ecocyc.RXN-19311]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19312|reaction.ecocyc.RXN-19312]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7122|reaction.ecocyc.RXN0-7122]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3825|gene.b3825]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07000`
- `KEGG:ecj:JW5584;eco:b3825;ecoc:C3026_20700;`
- `GeneID:93778112;948314;`
- `GO:GO:0004622; GO:0005886; GO:0006650; GO:0016020; GO:0016747`
- `EC:3.1.1.5`

## Notes

Lysophospholipase L2 (EC 3.1.1.5) (Lecithinase B)
