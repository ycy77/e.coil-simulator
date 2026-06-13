---
entity_id: "complex.ecocyc.RNAPS-CPLX"
entity_type: "complex"
name: "RNA polymerase sigma S"
source_database: "EcoCyc"
source_id: "RNAPS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "RNA polymerase sigma 38"
  - "RNA polymerase sigma 38 holoenzyme"
---

# RNA polymerase sigma S

`complex.ecocyc.RNAPS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:RNAPS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.APORNAP-CPLX|complex.ecocyc.APORNAP-CPLX]], [[protein.P13445|protein.P13445]]

## Enriched Summary

EcoCyc complex RNAPS-CPLX

## Annotation

EcoCyc complex RNAPS-CPLX

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_component_of` <-- [[complex.ecocyc.APORNAP-CPLX|complex.ecocyc.APORNAP-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P0A7Z4|protein.P0A7Z4]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A8T7|protein.P0A8T7]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A8V2|protein.P0A8V2]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P13445|protein.P13445]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:RNAPS-CPLX`
- `PDB:3LU0`
- `PDB:3IYD`
- `PDB:4KN7`
- `PDB:4KN4`
- `PDB:4KMU`
- `PDB:4JK2`
- `PDB:4JK1`
- `PDB:4MEY`
- `QSPROTEOME:QS00197301`

## Notes

1*complex.ecocyc.APORNAP-CPLX|1*protein.P13445
