---
entity_id: "complex.ecocyc.BADH-CPLX"
entity_type: "complex"
name: "betaine aldehyde dehydrogenase"
source_database: "EcoCyc"
source_id: "BADH-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# betaine aldehyde dehydrogenase

`complex.ecocyc.BADH-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:BADH-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P17445|protein.P17445]]

## Enriched Summary

EcoCyc complex BADH-CPLX

## Biological Role

Catalyzes BADH-RXN (reaction.ecocyc.BADH-RXN).

## Annotation

EcoCyc complex BADH-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.BADH-RXN|reaction.ecocyc.BADH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P17445|protein.P17445]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:BADH-CPLX`
- `QSPROTEOME:QS00183227`

## Notes

4*protein.P17445
