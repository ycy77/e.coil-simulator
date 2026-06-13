---
entity_id: "complex.ecocyc.LTAA-CPLX"
entity_type: "complex"
name: "low-specificity L-threonine aldolase"
source_database: "EcoCyc"
source_id: "LTAA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# low-specificity L-threonine aldolase

`complex.ecocyc.LTAA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:LTAA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P75823|protein.P75823]]

## Enriched Summary

EcoCyc complex LTAA-CPLX

## Biological Role

Catalyzes LTAA-RXN (reaction.ecocyc.LTAA-RXN), PHENYLSERINE-ALDOLASE-RXN (reaction.ecocyc.PHENYLSERINE-ALDOLASE-RXN), RXN0-6563 (reaction.ecocyc.RXN0-6563), THREONINE-ALDOLASE-RXN (reaction.ecocyc.THREONINE-ALDOLASE-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex LTAA-CPLX

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.LTAA-RXN|reaction.ecocyc.LTAA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PHENYLSERINE-ALDOLASE-RXN|reaction.ecocyc.PHENYLSERINE-ALDOLASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6563|reaction.ecocyc.RXN0-6563]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.THREONINE-ALDOLASE-RXN|reaction.ecocyc.THREONINE-ALDOLASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P75823|protein.P75823]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:LTAA-CPLX`
- `QSPROTEOME:QS00195189`

## Notes

4*protein.P75823
