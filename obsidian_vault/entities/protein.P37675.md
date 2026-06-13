---
entity_id: "protein.P37675"
entity_type: "protein"
name: "yiaN"
source_database: "UniProt"
source_id: "P37675"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yiaN b3578 JW5651"
---

# yiaN

`protein.P37675`

## Static

- Type: `protein`
- Source: `UniProt:P37675`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the tripartite ATP-independent periplasmic (TRAP) transport system YiaMNO involved in the uptake of 2,3-diketo-L-gulonate. {ECO:0000269|PubMed:16385129}. Based on sequence similarity, YiaN is a membrane-spanning component of the YiaMNO Binding protein-dependent Secondary (TRAP) Transporter .

## Biological Role

Component of 2,3-diketo-L-gulonate:Na+ symporter (complex.ecocyc.TRANS-CPLX-203).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the tripartite ATP-independent periplasmic (TRAP) transport system YiaMNO involved in the uptake of 2,3-diketo-L-gulonate. {ECO:0000269|PubMed:16385129}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.TRANS-CPLX-203|complex.ecocyc.TRANS-CPLX-203]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3578|gene.b3578]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37675`
- `KEGG:ecj:JW5651;eco:b3578;ecoc:C3026_19400;`
- `GeneID:75204654;948092;`
- `GO:GO:0005886; GO:0015144; GO:0016020; GO:0031317; GO:0034219; GO:1900190; GO:1902075`

## Notes

2,3-diketo-L-gulonate TRAP transporter large permease protein YiaN
