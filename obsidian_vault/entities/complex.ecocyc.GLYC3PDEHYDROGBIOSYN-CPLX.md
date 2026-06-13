---
entity_id: "complex.ecocyc.GLYC3PDEHYDROGBIOSYN-CPLX"
entity_type: "complex"
name: "glycerol-3-phosphate dehydrogenase, biosynthetic"
source_database: "EcoCyc"
source_id: "GLYC3PDEHYDROGBIOSYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glycerol-3-phosphate dehydrogenase, biosynthetic

`complex.ecocyc.GLYC3PDEHYDROGBIOSYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLYC3PDEHYDROGBIOSYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6S7|protein.P0A6S7]]

## Enriched Summary

EcoCyc complex GLYC3PDEHYDROGBIOSYN-CPLX

## Biological Role

Catalyzes GLYC3PDEHYDROGBIOSYN-RXN (reaction.ecocyc.GLYC3PDEHYDROGBIOSYN-RXN).

## Annotation

EcoCyc complex GLYC3PDEHYDROGBIOSYN-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLYC3PDEHYDROGBIOSYN-RXN|reaction.ecocyc.GLYC3PDEHYDROGBIOSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6S7|protein.P0A6S7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GLYC3PDEHYDROGBIOSYN-CPLX`
- `QSPROTEOME:QS00049720`

## Notes

2*protein.P0A6S7
