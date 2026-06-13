---
entity_id: "complex.ecocyc.CPLX-8401"
entity_type: "complex"
name: "5-dehydro-4-deoxy-D-glucuronate isomerase"
source_database: "EcoCyc"
source_id: "CPLX-8401"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 5-dehydro-4-deoxy-D-glucuronate isomerase

`complex.ecocyc.CPLX-8401`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-8401`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.Q46938|protein.Q46938]]

## Enriched Summary

EcoCyc complex CPLX-8401

## Biological Role

Catalyzes 5.3.1.17-RXN (reaction.ecocyc.5.3.1.17-RXN), PGLUCISOM-RXN (reaction.ecocyc.PGLUCISOM-RXN).

## Annotation

EcoCyc complex CPLX-8401

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.5.3.1.17-RXN|reaction.ecocyc.5.3.1.17-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PGLUCISOM-RXN|reaction.ecocyc.PGLUCISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.Q46938|protein.Q46938]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX-8401`
- `QSPROTEOME:QS00181915`

## Notes

2*protein.Q46938
