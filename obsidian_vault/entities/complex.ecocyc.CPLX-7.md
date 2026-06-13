---
entity_id: "complex.ecocyc.CPLX-7"
entity_type: "complex"
name: "arsenite/antimonite:H+ antiporter"
source_database: "EcoCyc"
source_id: "CPLX-7"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ArsB arsenite transporter"
  - "ArsB"
---

# arsenite/antimonite:H+ antiporter

`complex.ecocyc.CPLX-7`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-7`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AB93|protein.P0AB93]]

## Enriched Summary

EcoCyc complex CPLX-7

## Biological Role

Catalyzes RXN-22385 (reaction.ecocyc.RXN-22385), antimonite:proton antiport (reaction.ecocyc.RXN3O-9786). Transports antimonous acid (molecule.ecocyc.CPD0-2039), arsenous acid (molecule.ecocyc.CPD0-2040), hν (molecule.ecocyc.Light).

## Annotation

EcoCyc complex CPLX-7

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.RXN-22385|reaction.ecocyc.RXN-22385]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN3O-9786|reaction.ecocyc.RXN3O-9786]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD0-2039|molecule.ecocyc.CPD0-2039]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD0-2040|molecule.ecocyc.CPD0-2040]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AB93|protein.P0AB93]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX-7`
- `QSPROTEOME:QS00049689`

## Notes

2*protein.P0AB93
