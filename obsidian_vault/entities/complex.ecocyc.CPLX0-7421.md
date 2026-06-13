---
entity_id: "complex.ecocyc.CPLX0-7421"
entity_type: "complex"
name: "tRNA (cytidine/uridine-2'-O)-ribose methyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-7421"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tRNA (cytidine/uridine-2'-O)-ribose methyltransferase

`complex.ecocyc.CPLX0-7421`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7421`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AGJ7|protein.P0AGJ7]]

## Enriched Summary

EcoCyc complex CPLX0-7421

## Biological Role

Catalyzes S-adenosyl-L-methionine:tRNA (cytidine34/5-carboxymethylaminomethyluridine34-2'-O)-methyltransferase (reaction.ecocyc.RXN-11860), S-adenosyl-L-methionine:tRNA (cytidine34/5-carboxymethylaminomethyluridine34-2'-O)-methyltransferase (reaction.ecocyc.RXN-11865), RXN0-7168 (reaction.ecocyc.RXN0-7168).

## Annotation

EcoCyc complex CPLX0-7421

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-11860|reaction.ecocyc.RXN-11860]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11865|reaction.ecocyc.RXN-11865]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7168|reaction.ecocyc.RXN0-7168]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AGJ7|protein.P0AGJ7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7421`
- `QSPROTEOME:QS00180881`

## Notes

2*protein.P0AGJ7
