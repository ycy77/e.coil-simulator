---
entity_id: "protein.P0AC05"
entity_type: "protein"
name: "fliP"
source_database: "UniProt"
source_id: "P0AC05"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}. Bacterial flagellum basal body {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliP flaR b1948 JW1932"
---

# fliP

`protein.P0AC05`

## Static

- Type: `protein`
- Source: `UniProt:P0AC05`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}. Bacterial flagellum basal body {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Plays a role in the flagellum-specific transport system. FliP is one of six integral membrane components of the flagellar export apparatus . FliP has a substantial periplasmic domain between two of its four transmembrane domains .

## Biological Role

Component of flagellar export assembly apparatus (complex.ecocyc.CPLX0-7451).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Plays a role in the flagellum-specific transport system.

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7451|complex.ecocyc.CPLX0-7451]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1948|gene.b1948]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC05`
- `KEGG:ecj:JW1932;eco:b1948;ecoc:C3026_11030;`
- `GeneID:75172067;946462;`
- `GO:GO:0005886; GO:0006935; GO:0009288; GO:0030254; GO:0030257; GO:0044780; GO:0071973; GO:0071978; GO:0120102`

## Notes

Flagellar biosynthetic protein FliP
