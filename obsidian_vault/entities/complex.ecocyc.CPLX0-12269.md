---
entity_id: "complex.ecocyc.CPLX0-12269"
entity_type: "complex"
name: "SecYEG-SecA complex"
source_database: "EcoCyc"
source_id: "CPLX0-12269"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# SecYEG-SecA complex

`complex.ecocyc.CPLX0-12269`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-12269`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P10408|protein.P10408]], [[complex.ecocyc.SECE-G-Y-CPLX|complex.ecocyc.SECE-G-Y-CPLX]]

## Enriched Summary

EcoCyc complex CPLX0-12269

## Biological Role

Catalyzes TRANS-RXN-403 (reaction.ecocyc.TRANS-RXN-403), SecA-dependent protein translocation (reaction.ecocyc.TRANS-RXN0-636).

## Annotation

EcoCyc complex CPLX0-12269

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-403|reaction.ecocyc.TRANS-RXN-403]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-636|reaction.ecocyc.TRANS-RXN0-636]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `is_component_of` <-- [[complex.ecocyc.SECE-G-Y-CPLX|complex.ecocyc.SECE-G-Y-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0AG96|protein.P0AG96]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AG99|protein.P0AG99]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P0AGA2|protein.P0AGA2]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P10408|protein.P10408]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX0-12269`
- `QSPROTEOME:QS00195649`

## Notes

protein.P10408|complex.ecocyc.SECE-G-Y-CPLX
