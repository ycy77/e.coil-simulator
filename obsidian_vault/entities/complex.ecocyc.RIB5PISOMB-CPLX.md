---
entity_id: "complex.ecocyc.RIB5PISOMB-CPLX"
entity_type: "complex"
name: "allose-6-phosphate isomerase / ribose-5-phosphate isomerase B"
source_database: "EcoCyc"
source_id: "RIB5PISOMB-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# allose-6-phosphate isomerase / ribose-5-phosphate isomerase B

`complex.ecocyc.RIB5PISOMB-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:RIB5PISOMB-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P37351|protein.P37351]]

## Enriched Summary

EcoCyc complex RIB5PISOMB-CPLX

## Biological Role

Catalyzes RIB5PISOM-RXN (reaction.ecocyc.RIB5PISOM-RXN), RXN0-303 (reaction.ecocyc.RXN0-303).

## Annotation

EcoCyc complex RIB5PISOMB-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RIB5PISOM-RXN|reaction.ecocyc.RIB5PISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-303|reaction.ecocyc.RXN0-303]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P37351|protein.P37351]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:RIB5PISOMB-CPLX`
- `QSPROTEOME:QS00191627`

## Notes

2*protein.P37351
