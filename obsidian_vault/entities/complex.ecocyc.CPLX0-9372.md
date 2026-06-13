---
entity_id: "complex.ecocyc.CPLX0-9372"
entity_type: "complex"
name: "pyrroloquinoline quinone outer membrane transport complex"
source_database: "EcoCyc"
source_id: "CPLX0-9372"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# pyrroloquinoline quinone outer membrane transport complex

`complex.ecocyc.CPLX0-9372`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-9372`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]], [[protein.P76115|protein.P76115]]

## Enriched Summary

EcoCyc complex CPLX0-9372

## Biological Role

Catalyzes TRANS-RXN0-629 (reaction.ecocyc.TRANS-RXN0-629). Transports hν (molecule.ecocyc.Light), pyrroloquinoline quinone (molecule.ecocyc.PQQ).

## Annotation

EcoCyc complex CPLX0-9372

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-629|reaction.ecocyc.TRANS-RXN0-629]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.PQQ|molecule.ecocyc.PQQ]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (5)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P02929|protein.P02929]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0ABU7|protein.P0ABU7]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=5 | EcoCyc transporter component coefficient=5
- `is_component_of` <-- [[protein.P0ABV2|protein.P0ABV2]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P76115|protein.P76115]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX0-9372`
- `PDB:8VGC`
- `PDB:8VGD`
- `QSPROTEOME:QS00195677`

## Notes

complex.ecocyc.CPLX0-1923|protein.P76115
