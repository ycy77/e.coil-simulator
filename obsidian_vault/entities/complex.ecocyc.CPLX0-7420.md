---
entity_id: "complex.ecocyc.CPLX0-7420"
entity_type: "complex"
name: "tRNA Cm32/Um32 methyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-7420"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tRNA Cm32/Um32 methyltransferase

`complex.ecocyc.CPLX0-7420`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7420`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AE01|protein.P0AE01]]

## Enriched Summary

EcoCyc complex CPLX0-7420

## Biological Role

Catalyzes "S-adenosyl-L-methionine:tRNA (cytidine32/uridine32-2'-O)-methyltransferase" (reaction.ecocyc.RXN-11866), S-adenosyl-L-methionine:tRNA (cytidine32/uridine32-2'-O)-methyltransferase (reaction.ecocyc.RXN-11867).

## Annotation

EcoCyc complex CPLX0-7420

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-11866|reaction.ecocyc.RXN-11866]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11867|reaction.ecocyc.RXN-11867]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AE01|protein.P0AE01]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7420`
- `QSPROTEOME:QS00192155`

## Notes

2*protein.P0AE01
