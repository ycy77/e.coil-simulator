---
entity_id: "complex.ecocyc.CPLX0-1943"
entity_type: "complex"
name: "ferric citrate outer membrane transport complex"
source_database: "EcoCyc"
source_id: "CPLX0-1943"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ferric dicitrate outer membrane transport complex"
---

# ferric citrate outer membrane transport complex

`complex.ecocyc.CPLX0-1943`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1943`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P13036|protein.P13036]], [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]]

## Enriched Summary

EcoCyc complex CPLX0-1943

## Biological Role

Catalyzes RXN0-1684 (reaction.ecocyc.RXN0-1684). Transports Fe(III)dicitrate (molecule.C06229), hν (molecule.ecocyc.Light).

## Annotation

EcoCyc complex CPLX0-1943

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1684|reaction.ecocyc.RXN0-1684]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C06229|molecule.C06229]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (5)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P02929|protein.P02929]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0ABU7|protein.P0ABU7]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=5 | EcoCyc transporter component coefficient=5
- `is_component_of` <-- [[protein.P0ABV2|protein.P0ABV2]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P13036|protein.P13036]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX0-1943`
- `QSPROTEOME:QS00199265`

## Notes

protein.P13036|complex.ecocyc.CPLX0-1923
