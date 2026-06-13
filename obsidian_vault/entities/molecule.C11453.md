---
entity_id: "molecule.C11453"
entity_type: "small_molecule"
name: "2-C-Methyl-D-erythritol 2,4-cyclodiphosphate"
source_database: "KEGG"
source_id: "C11453"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-C-Methyl-D-erythritol 2,4-cyclodiphosphate"
  - "3-Methyl-1,2,3,4-tetrahydroxybutane-1,3-cyclic bisphosphate"
---

# 2-C-Methyl-D-erythritol 2,4-cyclodiphosphate

`molecule.C11453`

## Static

- Type: `small_molecule`
- Source: `KEGG:C11453`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-C-Methyl-D-erythritol 2,4-cyclodiphosphate; 3-Methyl-1,2,3,4-tetrahydroxybutane-1,3-cyclic bisphosphate EcoCyc common name: 2-C-methyl-D-erythritol-2,4-cyclodiphosphate.

## Biological Role

Produced in 3 reaction(s).

## Enriched Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)

## Annotation

KEGG compound: 2-C-Methyl-D-erythritol 2,4-cyclodiphosphate; 3-Methyl-1,2,3,4-tetrahydroxybutane-1,3-cyclic bisphosphate

## Pathways

- `eco00900` Terpenoid backbone biosynthesis (KEGG)

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.CPLX0-12545|complex.ecocyc.CPLX0-12545]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R10859|reaction.R10859]] `KEGG` `database` - C11811 + C00001 + C02869 <=> C11453 + C02745
- `is_product_of` --> [[reaction.ecocyc.RXN-15878|reaction.ecocyc.RXN-15878]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-302|reaction.ecocyc.RXN0-302]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C11453`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
