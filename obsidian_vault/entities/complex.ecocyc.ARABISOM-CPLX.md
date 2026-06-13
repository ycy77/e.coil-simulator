---
entity_id: "complex.ecocyc.ARABISOM-CPLX"
entity_type: "complex"
name: "L-arabinose isomerase"
source_database: "EcoCyc"
source_id: "ARABISOM-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-arabinose isomerase

`complex.ecocyc.ARABISOM-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ARABISOM-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P08202|protein.P08202]]

## Enriched Summary

EcoCyc complex ARABISOM-CPLX

## Biological Role

Catalyzes ARABISOM-RXN (reaction.ecocyc.ARABISOM-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex ARABISOM-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ARABISOM-RXN|reaction.ecocyc.ARABISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P08202|protein.P08202]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:ARABISOM-CPLX`
- `QSPROTEOME:QS00182021`

## Notes

6*protein.P08202
