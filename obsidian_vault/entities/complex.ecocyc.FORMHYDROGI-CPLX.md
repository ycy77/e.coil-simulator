---
entity_id: "complex.ecocyc.FORMHYDROGI-CPLX"
entity_type: "complex"
name: "hydrogenase 1"
source_database: "EcoCyc"
source_id: "FORMHYDROGI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "HYD1"
  - "hydrogenase I"
  - "NiFe hydrogenase"
  - "hydrogen:menaquinone oxidoreductase"
  - "hydrogen oxidase"
  - "hydrogen:oxygen oxidoreductase"
---

# hydrogenase 1

`complex.ecocyc.FORMHYDROGI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:FORMHYDROGI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P69739|protein.P69739]], [[protein.P0ACD8|protein.P0ACD8]], [[protein.P0AAM1|protein.P0AAM1]]

## Enriched Summary

Review: Review:

## Biological Role

Component of hydrogenase 1, oxygen tolerant hydrogenase (complex.ecocyc.CPLX0-8167).

## Annotation

Review:

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8167|complex.ecocyc.CPLX0-8167]] `EcoCyc` `database` - EcoCyc component coefficient=2

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0AAM1|protein.P0AAM1]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ACD8|protein.P0ACD8]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P69739|protein.P69739]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:FORMHYDROGI-CPLX`
- `PDB:3UQY`
- `PDB:3USC`
- `PDB:3USE`
- `PDB:4GD3`
- `PDB:4UE3`
- `PDB:5ADU`
- `PDB:5A4M`
- `PDB:5A4I`
- `QSPROTEOME:QS00177501`

## Notes

2*protein.P69739|2*protein.P0ACD8|1*protein.P0AAM1
