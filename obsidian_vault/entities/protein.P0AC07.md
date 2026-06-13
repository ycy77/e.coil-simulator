---
entity_id: "protein.P0AC07"
entity_type: "protein"
name: "fliQ"
source_database: "UniProt"
source_id: "P0AC07"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}. Bacterial flagellum basal body {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliQ flaQ b1949 JW1933"
---

# fliQ

`protein.P0AC07`

## Static

- Type: `protein`
- Source: `UniProt:P0AC07`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}. Bacterial flagellum basal body {ECO:0000250}.

## Enriched Summary

FUNCTION: Required for the assembly of the rivet at the earliest stage of flagellar biosynthesis. FliQ is one of six integral membrane components of the flagellar export apparatus . FliQ has two transmembrane domains .

## Biological Role

Component of flagellar export assembly apparatus (complex.ecocyc.CPLX0-7451).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Required for the assembly of the rivet at the earliest stage of flagellar biosynthesis.

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7451|complex.ecocyc.CPLX0-7451]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1949|gene.b1949]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC07`
- `KEGG:ecj:JW1933;eco:b1949;ecoc:C3026_11035;`
- `GeneID:86860088;93775236;946463;`
- `GO:GO:0005886; GO:0006935; GO:0009288; GO:0030254; GO:0030257; GO:0044780; GO:0071973; GO:0120102`

## Notes

Flagellar biosynthetic protein FliQ
