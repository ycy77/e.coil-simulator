---
entity_id: "protein.P0CF40"
entity_type: "protein"
name: "insC1"
source_database: "UniProt"
source_id: "P0CF40"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "insC1 b0360 JW0351"
---

# insC1

`protein.P0CF40`

## Static

- Type: `protein`
- Source: `UniProt:P0CF40`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the transposition of the insertion sequence IS2.

## Biological Role

Component of IS2 insertion element repressor InsA (complex.ecocyc.CPLX0-7417).

## Annotation

FUNCTION: Involved in the transposition of the insertion sequence IS2.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7417|complex.ecocyc.CPLX0-7417]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0360|gene.b0360]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0CF40`
- `KEGG:ecj:JW0351;eco:b0360;eco:b1403;eco:b1997;eco:b2861;eco:b3044;eco:b4272;ecoc:C3026_00670;ecoc:C3026_03840;ecoc:C3026_06235;ecoc:C3026_08180;ecoc:C3026_09100;ecoc:C3026_11265;ecoc:C3026_15305;ecoc:C3026_15700;ecoc:C3026_16625;ecoc:C3026_20340;ecoc:C3026_23040;ecoc:C3026_24220;`
- `GeneID:945025;`
- `GO:GO:0003677; GO:0004803; GO:0006313`

## Notes

Transposase InsC for insertion element IS2A
