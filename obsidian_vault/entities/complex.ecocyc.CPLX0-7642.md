---
entity_id: "complex.ecocyc.CPLX0-7642"
entity_type: "complex"
name: "osmolyte:H+ symporter ProP"
source_database: "EcoCyc"
source_id: "CPLX0-7642"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# osmolyte:H+ symporter ProP

`complex.ecocyc.CPLX0-7642`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7642`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0C0L7|protein.P0C0L7]]

## Enriched Summary

EcoCyc complex CPLX0-7642

## Biological Role

Catalyzes L-proline:proton symport (reaction.ecocyc.TRANS-RXN-29), glycine betaine:proton symport (reaction.ecocyc.TRANS-RXN-29A). Transports L-Proline (molecule.C00148), Betaine (molecule.C00719), hν (molecule.ecocyc.Light).

## Annotation

EcoCyc complex CPLX0-7642

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-29|reaction.ecocyc.TRANS-RXN-29]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-29A|reaction.ecocyc.TRANS-RXN-29A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00148|molecule.C00148]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00719|molecule.C00719]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0C0L7|protein.P0C0L7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-7642`
- `QSPROTEOME:QS00049633`

## Notes

2*protein.P0C0L7
