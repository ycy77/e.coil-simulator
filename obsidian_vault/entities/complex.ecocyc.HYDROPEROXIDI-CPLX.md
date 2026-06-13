---
entity_id: "complex.ecocyc.HYDROPEROXIDI-CPLX"
entity_type: "complex"
name: "catalase/hydroperoxidase HPI"
source_database: "EcoCyc"
source_id: "HYDROPEROXIDI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "catalase HPI"
  - "HPI"
---

# catalase/hydroperoxidase HPI

`complex.ecocyc.HYDROPEROXIDI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:HYDROPEROXIDI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P13029|protein.P13029]]

## Enriched Summary

EcoCyc complex HYDROPEROXIDI-CPLX

## Biological Role

Catalyzes CATAL-RXN (reaction.ecocyc.CATAL-RXN), RXN-8667 (reaction.ecocyc.RXN-8667). Bound by protoheme (molecule.ecocyc.PROTOHEME).

## Annotation

EcoCyc complex HYDROPEROXIDI-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.CATAL-RXN|reaction.ecocyc.CATAL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-8667|reaction.ecocyc.RXN-8667]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.PROTOHEME|molecule.ecocyc.PROTOHEME]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P13029|protein.P13029]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:HYDROPEROXIDI-CPLX`
- `QSPROTEOME:QS00199667`

## Notes

4*protein.P13029
