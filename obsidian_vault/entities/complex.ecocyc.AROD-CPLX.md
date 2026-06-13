---
entity_id: "complex.ecocyc.AROD-CPLX"
entity_type: "complex"
name: "3-dehydroquinate dehydratase"
source_database: "EcoCyc"
source_id: "AROD-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 3-dehydroquinate dehydratase

`complex.ecocyc.AROD-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:AROD-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P05194|protein.P05194]]

## Enriched Summary

EcoCyc complex AROD-CPLX

## Biological Role

Catalyzes 3-DEHYDROQUINATE-DEHYDRATASE-RXN (reaction.ecocyc.3-DEHYDROQUINATE-DEHYDRATASE-RXN).

## Annotation

EcoCyc complex AROD-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3-DEHYDROQUINATE-DEHYDRATASE-RXN|reaction.ecocyc.3-DEHYDROQUINATE-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P05194|protein.P05194]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:AROD-CPLX`
- `QSPROTEOME:QS00049569`

## Notes

2*protein.P05194
