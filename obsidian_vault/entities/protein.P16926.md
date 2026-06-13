---
entity_id: "protein.P16926"
entity_type: "protein"
name: "mreC"
source_database: "UniProt"
source_id: "P16926"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15612918}; Single-pass membrane protein {ECO:0000269|PubMed:15612918}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mreC b3250 JW3219"
---

# mreC

`protein.P16926`

## Static

- Type: `protein`
- Source: `UniProt:P16926`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15612918}; Single-pass membrane protein {ECO:0000269|PubMed:15612918}.

## Enriched Summary

FUNCTION: Involved in formation and maintenance of cell shape. Responsible for formation of rod shape. May also contribute to regulation of formation of penicillin-binding proteins. {ECO:0000269|PubMed:15612918, ECO:0000269|PubMed:2687239}.

## Biological Role

Component of cell shape determining protein MreC (complex.ecocyc.CPLX0-8612).

## Annotation

FUNCTION: Involved in formation and maintenance of cell shape. Responsible for formation of rod shape. May also contribute to regulation of formation of penicillin-binding proteins. {ECO:0000269|PubMed:15612918, ECO:0000269|PubMed:2687239}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8612|complex.ecocyc.CPLX0-8612]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3250|gene.b3250]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16926`
- `KEGG:ecj:JW3219;eco:b3250;`
- `GeneID:947655;`
- `GO:GO:0005886; GO:0008360; GO:0009252; GO:0071963`

## Notes

Cell shape-determining protein MreC (Cell shape protein MreC) (Rod shape-determining protein MreC)
