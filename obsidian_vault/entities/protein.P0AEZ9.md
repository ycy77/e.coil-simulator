---
entity_id: "protein.P0AEZ9"
entity_type: "protein"
name: "moaB"
source_database: "UniProt"
source_id: "P0AEZ9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "moaB chlA2 b0782 JW0765"
---

# moaB

`protein.P0AEZ9`

## Static

- Type: `protein`
- Source: `UniProt:P0AEZ9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: May be involved in the biosynthesis of molybdopterin. Can bind GTP and has low GTPase activity. Can bind MPT, but has no MPT adenylyl transferase activity.

## Biological Role

Component of protein MoaB (complex.ecocyc.CPLX0-2521).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

FUNCTION: May be involved in the biosynthesis of molybdopterin. Can bind GTP and has low GTPase activity. Can bind MPT, but has no MPT adenylyl transferase activity.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2521|complex.ecocyc.CPLX0-2521]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0782|gene.b0782]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEZ9`
- `KEGG:ecj:JW0765;eco:b0782;ecoc:C3026_04960;`
- `GeneID:93776648;945396;`
- `GO:GO:0005525; GO:0005829; GO:0006777; GO:0034214; GO:0042802`

## Notes

Molybdenum cofactor biosynthesis protein B
