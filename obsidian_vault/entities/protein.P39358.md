---
entity_id: "protein.P39358"
entity_type: "protein"
name: "yjhG"
source_database: "UniProt"
source_id: "P39358"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yjhG b4297 JW4259"
---

# yjhG

`protein.P39358`

## Static

- Type: `protein`
- Source: `UniProt:P39358`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dehydration of D-xylonic acid to form 2-dehydro-3-deoxy-D-pentonate. {ECO:0000269|PubMed:26083940, ECO:0000305|PubMed:23233208}. YjhG is a D-xylonate dehydratase . A yjhG yagF double mutant can not use D-xylonate as the sole source of carbon, and crude cell extracts do not contain D-xylonate dehydratase activity . Both phenotypes are complemented by providing yjhG on a plasmid . Overexpression of yjhG is part of a metabolic engineering strategy for production of 1,2,4-butanetriol .

## Biological Role

Catalyzes XYLONATE-DEHYDRATASE-RXN (reaction.ecocyc.XYLONATE-DEHYDRATASE-RXN).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the dehydration of D-xylonic acid to form 2-dehydro-3-deoxy-D-pentonate. {ECO:0000269|PubMed:26083940, ECO:0000305|PubMed:23233208}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.XYLONATE-DEHYDRATASE-RXN|reaction.ecocyc.XYLONATE-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4297|gene.b4297]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39358`
- `KEGG:ecj:JW4259;eco:b4297;ecoc:C3026_23185;`
- `GeneID:946829;`
- `GO:GO:0005829; GO:0016836; GO:0046176; GO:0050401`
- `EC:4.2.1.82`

## Notes

D-xylonate dehydratase YjhG (EC 4.2.1.82)
