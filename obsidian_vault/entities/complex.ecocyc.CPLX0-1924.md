---
entity_id: "complex.ecocyc.CPLX0-1924"
entity_type: "complex"
name: "cobalamin outer membrane transport complex"
source_database: "EcoCyc"
source_id: "CPLX0-1924"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cobalamin outer membrane transport complex

`complex.ecocyc.CPLX0-1924`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1924`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P06129|protein.P06129]], [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]]

## Enriched Summary

EcoCyc complex CPLX0-1924

## Biological Role

Catalyzes RXN0-1565 (reaction.ecocyc.RXN0-1565), TRANS-RXN-1592 (reaction.ecocyc.TRANS-RXN-1592), TRANS-RXN0-283 (reaction.ecocyc.TRANS-RXN0-283). Transports Cobamide coenzyme (molecule.C00194), Cob(I)alamin (molecule.C00853), cob(II)inamide (molecule.ecocyc.CPD-20903), hν (molecule.ecocyc.Light).

## Annotation

EcoCyc complex CPLX0-1924

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1565|reaction.ecocyc.RXN0-1565]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-1592|reaction.ecocyc.TRANS-RXN-1592]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-283|reaction.ecocyc.TRANS-RXN0-283]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00194|molecule.C00194]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00853|molecule.C00853]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-20903|molecule.ecocyc.CPD-20903]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (5)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P02929|protein.P02929]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P06129|protein.P06129]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0ABU7|protein.P0ABU7]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=5 | EcoCyc transporter component coefficient=5
- `is_component_of` <-- [[protein.P0ABV2|protein.P0ABV2]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-1924`
- `PDB:2GSK`
- `QSPROTEOME:QS00195961`

## Notes

protein.P06129|complex.ecocyc.CPLX0-1923
