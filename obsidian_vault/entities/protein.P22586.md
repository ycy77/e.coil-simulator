---
entity_id: "protein.P22586"
entity_type: "protein"
name: "fliO"
source_database: "UniProt"
source_id: "P22586"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}. Bacterial flagellum basal body {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliO flaP flbD b1947 JW5316"
---

# fliO

`protein.P22586`

## Static

- Type: `protein`
- Source: `UniProt:P22586`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}. Bacterial flagellum basal body {ECO:0000250}.

## Enriched Summary

Flagellar protein FliO FliO is one of six integral membrane components of the flagellar export apparatus . FliO has a small N-terminal cytoplasmic domain, a hydrophobic domain consisting of a single transmembrane helix and a considerable periplasmic domain .

## Biological Role

Component of flagellar export assembly apparatus (complex.ecocyc.CPLX0-7451).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

Flagellar protein FliO

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7451|complex.ecocyc.CPLX0-7451]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1947|gene.b1947]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P22586`
- `KEGG:ecj:JW5316;eco:b1947;ecoc:C3026_11025;`
- `GeneID:75205812;946458;`
- `GO:GO:0005886; GO:0006935; GO:0009288; GO:0030254; GO:0030257; GO:0044781; GO:0071973; GO:0120102`

## Notes

Flagellar protein FliO
