---
entity_id: "protein.P33135"
entity_type: "protein"
name: "fliR"
source_database: "UniProt"
source_id: "P33135"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}. Bacterial flagellum basal body {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliR flaP b1950 JW1934"
---

# fliR

`protein.P33135`

## Static

- Type: `protein`
- Source: `UniProt:P33135`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}. Bacterial flagellum basal body {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Role in flagellar biosynthesis. FliR is one of six integral membrane components of the flagellar export apparatus . FliR has five or six transmembrane helices connected by short loops .

## Biological Role

Component of flagellar export assembly apparatus (complex.ecocyc.CPLX0-7451).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Role in flagellar biosynthesis.

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7451|complex.ecocyc.CPLX0-7451]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1950|gene.b1950]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33135`
- `KEGG:ecj:JW1934;eco:b1950;ecoc:C3026_11040;`
- `GeneID:946464;`
- `GO:GO:0005886; GO:0006605; GO:0006935; GO:0009288; GO:0030254; GO:0030257; GO:0044780; GO:0071973; GO:0120102`

## Notes

Flagellar biosynthetic protein FliR
