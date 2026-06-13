---
entity_id: "protein.P77596"
entity_type: "protein"
name: "yagF"
source_database: "UniProt"
source_id: "P77596"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yagF b0269 JW0262"
---

# yagF

`protein.P77596`

## Static

- Type: `protein`
- Source: `UniProt:P77596`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dehydration of D-xylonic acid to form 2-dehydro-3-deoxy-D-pentonate. {ECO:0000305|PubMed:23233208}. The YagF protein has D-xylonate dehydratase activity . A yjhG yagF double mutant can not use D-xylonate as the sole source of carbon, and crude cell extracts do not contain D-xylonate dehydratase activity . Both phenotypes are complemented by providing yjhG on a plasmid . Overexpression of yagF alleviates a bottleneck in the engineered production of glycolate . A yagF mutant is more resistant to the plant essential oil thymol than wild type .

## Biological Role

Catalyzes XYLONATE-DEHYDRATASE-RXN (reaction.ecocyc.XYLONATE-DEHYDRATASE-RXN).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the dehydration of D-xylonic acid to form 2-dehydro-3-deoxy-D-pentonate. {ECO:0000305|PubMed:23233208}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.XYLONATE-DEHYDRATASE-RXN|reaction.ecocyc.XYLONATE-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0269|gene.b0269]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77596`
- `KEGG:ecj:JW0262;eco:b0269;ecoc:C3026_01305;`
- `GeneID:944928;`
- `GO:GO:0005829; GO:0016836; GO:0046176; GO:0050401`
- `EC:4.2.1.82`

## Notes

D-xylonate dehydratase YagF (EC 4.2.1.82)
