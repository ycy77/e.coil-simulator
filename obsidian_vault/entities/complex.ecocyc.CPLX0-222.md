---
entity_id: "complex.ecocyc.CPLX0-222"
entity_type: "complex"
name: "RNA polymerase sigma 28"
source_database: "EcoCyc"
source_id: "CPLX0-222"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "RNA polymerase sigma 28 holoenzyme"
  - "RNA polymerase sigma F"
---

# RNA polymerase sigma 28

`complex.ecocyc.CPLX0-222`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-222`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AEM6|protein.P0AEM6]], [[complex.ecocyc.APORNAP-CPLX|complex.ecocyc.APORNAP-CPLX]]

## Enriched Summary

EcoCyc complex CPLX0-222

## Annotation

EcoCyc complex CPLX0-222

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_component_of` <-- [[complex.ecocyc.APORNAP-CPLX|complex.ecocyc.APORNAP-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P0A7Z4|protein.P0A7Z4]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A8T7|protein.P0A8T7]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A8V2|protein.P0A8V2]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AEM6|protein.P0AEM6]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-222`
- `PDB:6PMJ`
- `PDB:6PMI`
- `QSPROTEOME:QS00181809`

## Notes

1*protein.P0AEM6|1*complex.ecocyc.APORNAP-CPLX
