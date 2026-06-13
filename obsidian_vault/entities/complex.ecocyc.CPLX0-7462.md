---
entity_id: "complex.ecocyc.CPLX0-7462"
entity_type: "complex"
name: "shikimate dehydrogenase / quinate dehydrogenase"
source_database: "EcoCyc"
source_id: "CPLX0-7462"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# shikimate dehydrogenase / quinate dehydrogenase

`complex.ecocyc.CPLX0-7462`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7462`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6D5|protein.P0A6D5]]

## Enriched Summary

EcoCyc complex CPLX0-7462

## Biological Role

Catalyzes QUINATE-5-DEHYDROGENASE-RXN (reaction.ecocyc.QUINATE-5-DEHYDROGENASE-RXN), RXN-11174 (reaction.ecocyc.RXN-11174).

## Annotation

EcoCyc complex CPLX0-7462

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.QUINATE-5-DEHYDROGENASE-RXN|reaction.ecocyc.QUINATE-5-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11174|reaction.ecocyc.RXN-11174]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6D5|protein.P0A6D5]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7462`
- `QSPROTEOME:QS00180871`

## Notes

2*protein.P0A6D5
