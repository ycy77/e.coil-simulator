---
entity_id: "complex.ecocyc.HYDROPEROXIDII-CPLX"
entity_type: "complex"
name: "catalase HPII"
source_database: "EcoCyc"
source_id: "HYDROPEROXIDII-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "catalase II"
  - "HPII"
  - "hydroperoxidase II"
  - "HPIII"
---

# catalase HPII

`complex.ecocyc.HYDROPEROXIDII-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:HYDROPEROXIDII-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P21179|protein.P21179]]

## Enriched Summary

EcoCyc complex HYDROPEROXIDII-CPLX

## Biological Role

Catalyzes CATAL-RXN (reaction.ecocyc.CATAL-RXN), heme d biosynthesis (reaction.ecocyc.RXN-8073). Bound by cis heme d (molecule.ecocyc.CPD-23429).

## Annotation

EcoCyc complex HYDROPEROXIDII-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.CATAL-RXN|reaction.ecocyc.CATAL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-8073|reaction.ecocyc.RXN-8073]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-23429|molecule.ecocyc.CPD-23429]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P21179|protein.P21179]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:HYDROPEROXIDII-CPLX`
- `QSPROTEOME:QS00181517`

## Notes

4*protein.P21179
