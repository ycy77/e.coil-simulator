---
entity_id: "complex.ecocyc.CPLX0-1941"
entity_type: "complex"
name: "ferric enterobactin outer membrane transport complex"
source_database: "EcoCyc"
source_id: "CPLX0-1941"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ferric enterobactin outer membrane transport complex

`complex.ecocyc.CPLX0-1941`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1941`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]], [[protein.P05825|protein.P05825]]

## Enriched Summary

EcoCyc complex CPLX0-1941

## Biological Role

Catalyzes RXN0-1682 (reaction.ecocyc.RXN0-1682), TRANS-RXN-1598 (reaction.ecocyc.TRANS-RXN-1598). Transports Fe-enterobactin (molecule.C06230), hν (molecule.ecocyc.Light).

## Annotation

EcoCyc complex CPLX0-1941

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1682|reaction.ecocyc.RXN0-1682]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-1598|reaction.ecocyc.TRANS-RXN-1598]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C06230|molecule.C06230]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (5)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P02929|protein.P02929]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P05825|protein.P05825]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0ABU7|protein.P0ABU7]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=5 | EcoCyc transporter component coefficient=5
- `is_component_of` <-- [[protein.P0ABV2|protein.P0ABV2]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-1941`
- `PDB:8VGC`
- `PDB:8VGD`
- `QSPROTEOME:QS00196143`

## Notes

complex.ecocyc.CPLX0-1923|protein.P05825
