---
entity_id: "complex.ecocyc.CPLX0-1821"
entity_type: "complex"
name: "oligoribonuclease"
source_database: "EcoCyc"
source_id: "CPLX0-1821"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# oligoribonuclease

`complex.ecocyc.CPLX0-1821`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1821`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A784|protein.P0A784]]

## Enriched Summary

EcoCyc complex CPLX0-1821

## Biological Role

Catalyzes 3.1.13.3-RXN (reaction.ecocyc.3.1.13.3-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex CPLX0-1821

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.1.13.3-RXN|reaction.ecocyc.3.1.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A784|protein.P0A784]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-1821`
- `QSPROTEOME:QS00188631`

## Notes

2*protein.P0A784
