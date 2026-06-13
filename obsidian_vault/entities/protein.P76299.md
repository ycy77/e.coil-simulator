---
entity_id: "protein.P76299"
entity_type: "protein"
name: "flhB"
source_database: "UniProt"
source_id: "P76299"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "flhB yecQ b1880 JW1869"
---

# flhB

`protein.P76299`

## Static

- Type: `protein`
- Source: `UniProt:P76299`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Required for formation of the rod structure in the basal body of the flagellar apparatus. Together with FliI and FliH, may constitute the export apparatus of flagellin. FlhB is one of six integral membrane components of the flagellar export apparatus. FlhB has two regions: the hydrophobic N-terminal domain which, according to hydophobicity studies, crosses the cytoplasmic membrane four times and the C-terminal cytoplasmic domain .

## Biological Role

Component of flagellar export assembly apparatus (complex.ecocyc.CPLX0-7451).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Required for formation of the rod structure in the basal body of the flagellar apparatus. Together with FliI and FliH, may constitute the export apparatus of flagellin.

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7451|complex.ecocyc.CPLX0-7451]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1880|gene.b1880]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76299`
- `KEGG:ecj:JW1869;eco:b1880;ecoc:C3026_10695;`
- `GeneID:75202714;946391;`
- `GO:GO:0005886; GO:0006935; GO:0009288; GO:0030254; GO:0030257; GO:0044780; GO:0071973; GO:0120102`

## Notes

Flagellar biosynthetic protein FlhB
