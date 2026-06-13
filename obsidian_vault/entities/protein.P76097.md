---
entity_id: "protein.P76097"
entity_type: "protein"
name: "ydcJ"
source_database: "UniProt"
source_id: "P76097"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydcJ b1423 JW1419"
---

# ydcJ

`protein.P76097`

## Static

- Type: `protein`
- Source: `UniProt:P76097`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the decarboxylation and hydroxylation of 2-oxoadipate (2OA) to form D-2-hydroxyglutarate (D-2-HGA). {ECO:0000269|PubMed:32523014}. No information about this protein was found by a literature search conducted on February 9, 2017.

## Biological Role

Catalyzes 2-oxoadipate dioxygenase/carboxy lyase (reaction.R13011).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the decarboxylation and hydroxylation of 2-oxoadipate (2OA) to form D-2-hydroxyglutarate (D-2-HGA). {ECO:0000269|PubMed:32523014}.

## Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R13011|reaction.R13011]] `KEGG` `database` - via EC:1.13.11.93

## Incoming Edges (1)

- `encodes` <-- [[gene.b1423|gene.b1423]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76097`
- `KEGG:ecj:JW1419;eco:b1423;ecoc:C3026_08285;`
- `GeneID:945991;`
- `GO:GO:0046872; GO:0051213`
- `EC:1.13.11.93`

## Notes

2-oxoadipate dioxygenase/decarboxylase (EC 1.13.11.93) (2-hydroxyglutarate synthase)
