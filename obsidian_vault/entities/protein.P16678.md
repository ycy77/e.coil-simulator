---
entity_id: "protein.P16678"
entity_type: "protein"
name: "phnK"
source_database: "UniProt"
source_id: "P16678"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phnK b4097 JW5727"
---

# phnK

`protein.P16678`

## Static

- Type: `protein`
- Source: `UniProt:P16678`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Belongs to an operon involved in alkylphosphonate uptake and C-P lyase. Exact function not known. PhnK is not required for the ribophosphonate triphosphate (RPnTP) synthase reaction.

## Biological Role

Component of carbon-phosphorus lyase ATP-binding protein PhnK (complex.ecocyc.CPLX0-10307), carbon-phosphorus lyase system (complex.ecocyc.CPLX0-7958).

## Annotation

FUNCTION: Belongs to an operon involved in alkylphosphonate uptake and C-P lyase. Exact function not known. PhnK is not required for the ribophosphonate triphosphate (RPnTP) synthase reaction.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10307|complex.ecocyc.CPLX0-10307]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7958|complex.ecocyc.CPLX0-7958]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4097|gene.b4097]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16678`
- `KEGG:ecj:JW5727;eco:b4097;ecoc:C3026_22145;`
- `GeneID:948611;99810303;`
- `GO:GO:0005524; GO:0015716; GO:0015833; GO:0016887; GO:0019634; GO:0019700; GO:0061694; GO:1904176`

## Notes

Putative phosphonates utilization ATP-binding protein PhnK
