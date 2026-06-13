---
entity_id: "protein.P37674"
entity_type: "protein"
name: "yiaM"
source_database: "UniProt"
source_id: "P37674"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yiaM b3577 JW3549"
---

# yiaM

`protein.P37674`

## Static

- Type: `protein`
- Source: `UniProt:P37674`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of the tripartite ATP-independent periplasmic (TRAP) transport system YiaMNO involved in the uptake of 2,3-diketo-L-gulonate. {ECO:0000269|PubMed:16385129}. Based on sequence similarity, YiaM is a membrane-spanning component of the YiaMNO Binding Protein-dependent Secondary (TRAP) Transporter

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

- `encodes` <-- [[gene.b3577|gene.b3577]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37674`
- `KEGG:ecj:JW3549;eco:b3577;ecoc:C3026_19395;`
- `GeneID:75204655;948093;`
- `GO:GO:0005886; GO:0015144; GO:0015740; GO:0016020; GO:0022857; GO:0031317; GO:0034219; GO:1900190; GO:1902075`

## Notes

2,3-diketo-L-gulonate TRAP transporter small permease protein YiaM
