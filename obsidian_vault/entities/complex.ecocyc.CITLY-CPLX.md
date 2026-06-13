---
entity_id: "complex.ecocyc.CITLY-CPLX"
entity_type: "complex"
name: "citrate lyase, inactive"
source_database: "EcoCyc"
source_id: "CITLY-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "(HS)-citrate lyase"
  - "citrate lyase, thiol form"
  - "deacetyl-citrate lyase"
---

# citrate lyase, inactive

`complex.ecocyc.CITLY-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CITLY-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.ACPSUB-CPLX|complex.ecocyc.ACPSUB-CPLX]], [[complex.ecocyc.CITTRANS-CPLX|complex.ecocyc.CITTRANS-CPLX]], [[complex.ecocyc.CITRYLY-CPLX|complex.ecocyc.CITRYLY-CPLX]]

## Enriched Summary

EcoCyc complex CITLY-CPLX

## Annotation

EcoCyc complex CITLY-CPLX

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_component_of` <-- [[complex.ecocyc.ACPSUB-CPLX|complex.ecocyc.ACPSUB-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.CITRYLY-CPLX|complex.ecocyc.CITRYLY-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.CITTRANS-CPLX|complex.ecocyc.CITTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P0A9I1|protein.P0A9I1]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6
- `is_component_of` <-- [[protein.P69330|protein.P69330]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6
- `is_component_of` <-- [[protein.P75726|protein.P75726]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CITLY-CPLX`

## Notes

1*complex.ecocyc.ACPSUB-CPLX|1*complex.ecocyc.CITTRANS-CPLX|1*complex.ecocyc.CITRYLY-CPLX
