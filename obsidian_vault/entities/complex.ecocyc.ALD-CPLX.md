---
entity_id: "complex.ecocyc.ALD-CPLX"
entity_type: "complex"
name: "aldehyde dehydrogenase A, NAD-linked"
source_database: "EcoCyc"
source_id: "ALD-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# aldehyde dehydrogenase A, NAD-linked

`complex.ecocyc.ALD-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ALD-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P25553|protein.P25553]]

## Enriched Summary

EcoCyc complex ALD-CPLX

## Biological Role

Catalyzes GLYCOLALD-DEHYDROG-RXN (reaction.ecocyc.GLYCOLALD-DEHYDROG-RXN), LACTALDDEHYDROG-RXN (reaction.ecocyc.LACTALDDEHYDROG-RXN).

## Annotation

EcoCyc complex ALD-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GLYCOLALD-DEHYDROG-RXN|reaction.ecocyc.GLYCOLALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.LACTALDDEHYDROG-RXN|reaction.ecocyc.LACTALDDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P25553|protein.P25553]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:ALD-CPLX`
- `QSPROTEOME:QS00181999`

## Notes

4*protein.P25553
