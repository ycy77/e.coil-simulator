---
entity_id: "complex.ecocyc.CPLX0-1942"
entity_type: "complex"
name: "ferrichrome outer membrane transport complex"
source_database: "EcoCyc"
source_id: "CPLX0-1942"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ferrichrome outer membrane transport complex

`complex.ecocyc.CPLX0-1942`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1942`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]], [[protein.P06971|protein.P06971]]

## Enriched Summary

EcoCyc complex CPLX0-1942

## Biological Role

Catalyzes RXN0-1701 (reaction.ecocyc.RXN0-1701). Transports ferrichrome (molecule.ecocyc.CPD0-2241), hν (molecule.ecocyc.Light).

## Annotation

EcoCyc complex CPLX0-1942

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1701|reaction.ecocyc.RXN0-1701]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD0-2241|molecule.ecocyc.CPD0-2241]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (5)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P02929|protein.P02929]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P06971|protein.P06971]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0ABU7|protein.P0ABU7]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=5 | EcoCyc transporter component coefficient=5
- `is_component_of` <-- [[protein.P0ABV2|protein.P0ABV2]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-1942`
- `PDB:2GRX`
- `PDB:8VGC`
- `PDB:8VGD`
- `QSPROTEOME:QS00181987`

## Notes

complex.ecocyc.CPLX0-1923|protein.P06971
