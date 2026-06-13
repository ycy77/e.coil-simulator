---
entity_id: "protein.P76216"
entity_type: "protein"
name: "astB"
source_database: "UniProt"
source_id: "P76216"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "astB ydjT b1745 JW1734"
---

# astB

`protein.P76216`

## Static

- Type: `protein`
- Source: `UniProt:P76216`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of N(2)-succinylarginine into N(2)-succinylornithine, ammonia and CO(2). {ECO:0000269|PubMed:15703173, ECO:0000269|PubMed:9696779}.

## Biological Role

Component of N-succinylarginine dihydrolase (complex.ecocyc.CPLX0-7947).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of N(2)-succinylarginine into N(2)-succinylornithine, ammonia and CO(2). {ECO:0000269|PubMed:15703173, ECO:0000269|PubMed:9696779}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7947|complex.ecocyc.CPLX0-7947]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1745|gene.b1745]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76216`
- `KEGG:ecj:JW1734;eco:b1745;ecoc:C3026_09970;`
- `GeneID:946259;`
- `GO:GO:0006527; GO:0009015; GO:0019544; GO:0019545; GO:0042803`
- `EC:3.5.3.23`

## Notes

N-succinylarginine dihydrolase (EC 3.5.3.23)
