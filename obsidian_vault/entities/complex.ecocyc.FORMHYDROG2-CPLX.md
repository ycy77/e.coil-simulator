---
entity_id: "complex.ecocyc.FORMHYDROG2-CPLX"
entity_type: "complex"
name: "hydrogenase 2"
source_database: "EcoCyc"
source_id: "FORMHYDROG2-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "HYD2"
  - "hydrogenase-2"
  - "hydrogen:menaquinone oxidoreductase 2"
---

# hydrogenase 2

`complex.ecocyc.FORMHYDROG2-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:FORMHYDROG2-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AAJ8|protein.P0AAJ8]], [[protein.P37180|protein.P37180]], [[protein.P69741|protein.P69741]], [[protein.P0ACE0|protein.P0ACE0]]

## Enriched Summary

EcoCyc complex FORMHYDROG2-CPLX

## Biological Role

Component of hydrogenase 2 (complex.ecocyc.CPLX0-8762).

## Annotation

EcoCyc complex FORMHYDROG2-CPLX

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8762|complex.ecocyc.CPLX0-8762]] `EcoCyc` `database` - EcoCyc component coefficient=2

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P0AAJ8|protein.P0AAJ8]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ACE0|protein.P0ACE0]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P37180|protein.P37180]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P69741|protein.P69741]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:FORMHYDROG2-CPLX`
- `QSPROTEOME:QS00049492`
- `PDB:6EN9`
- `PDB:6EHS`
- `PDB:6EHQ`

## Notes

1*protein.P0AAJ8|1*protein.P37180|1*protein.P69741|1*protein.P0ACE0
