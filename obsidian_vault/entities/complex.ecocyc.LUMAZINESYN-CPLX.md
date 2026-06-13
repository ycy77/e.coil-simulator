---
entity_id: "complex.ecocyc.LUMAZINESYN-CPLX"
entity_type: "complex"
name: "6,7-dimethyl-8-ribityllumazine synthase"
source_database: "EcoCyc"
source_id: "LUMAZINESYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 6,7-dimethyl-8-ribityllumazine synthase

`complex.ecocyc.LUMAZINESYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:LUMAZINESYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P61714|protein.P61714]]

## Enriched Summary

EcoCyc complex LUMAZINESYN-CPLX

## Biological Role

Catalyzes LUMAZINESYN-RXN (reaction.ecocyc.LUMAZINESYN-RXN).

## Annotation

EcoCyc complex LUMAZINESYN-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.LUMAZINESYN-RXN|reaction.ecocyc.LUMAZINESYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P61714|protein.P61714]] `EcoCyc` `database` - EcoCyc component coefficient=60 | EcoCyc protcplxs.col coefficient=60

## External IDs

- `EcoCyc:LUMAZINESYN-CPLX`

## Notes

60*protein.P61714
