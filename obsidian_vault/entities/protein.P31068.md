---
entity_id: "protein.P31068"
entity_type: "protein"
name: "fliH"
source_database: "UniProt"
source_id: "P31068"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliH fla AII.3 fla BIII b1940 JW1924"
---

# fliH

`protein.P31068`

## Static

- Type: `protein`
- Source: `UniProt:P31068`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Needed for flagellar regrowth and assembly. FliH is a cytoplasmic protein which exists as a dimer in solution and forms a stable heterotrimeric complex with FliI, inhibiting its ATPase activity .

## Biological Role

Component of flagellar export assembly apparatus (complex.ecocyc.CPLX0-7451).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Needed for flagellar regrowth and assembly.

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7451|complex.ecocyc.CPLX0-7451]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=12

## Incoming Edges (1)

- `encodes` <-- [[gene.b1940|gene.b1940]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31068`
- `KEGG:ecj:JW1924;eco:b1940;ecoc:C3026_10990;`
- `GeneID:946456;`
- `GO:GO:0003774; GO:0005829; GO:0006935; GO:0009288; GO:0030254; GO:0030257; GO:0044781; GO:0071973; GO:0120102`

## Notes

Flagellar assembly protein FliH
