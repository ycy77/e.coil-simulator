---
entity_id: "complex.ecocyc.GST-CPLX"
entity_type: "complex"
name: "glutathione S-transferase GstA"
source_database: "EcoCyc"
source_id: "GST-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glutathione S-transferase GstA

`complex.ecocyc.GST-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GST-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9D2|protein.P0A9D2]]

## Enriched Summary

EcoCyc complex GST-CPLX

## Biological Role

Catalyzes GST-RXN (reaction.ecocyc.GST-RXN).

## Annotation

EcoCyc complex GST-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GST-RXN|reaction.ecocyc.GST-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9D2|protein.P0A9D2]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GST-CPLX`
- `QSPROTEOME:QS00161089`

## Notes

2*protein.P0A9D2
