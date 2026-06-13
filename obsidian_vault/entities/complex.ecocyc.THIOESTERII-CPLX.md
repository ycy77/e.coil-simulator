---
entity_id: "complex.ecocyc.THIOESTERII-CPLX"
entity_type: "complex"
name: "acyl-CoA thioesterase II"
source_database: "EcoCyc"
source_id: "THIOESTERII-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# acyl-CoA thioesterase II

`complex.ecocyc.THIOESTERII-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:THIOESTERII-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AGG2|protein.P0AGG2]]

## Enriched Summary

EcoCyc complex THIOESTERII-CPLX

## Biological Role

Catalyzes ACYL-COA-HYDROLASE-RXN (reaction.ecocyc.ACYL-COA-HYDROLASE-RXN), RXN-14251 (reaction.ecocyc.RXN-14251), RXN-14255 (reaction.ecocyc.RXN-14255), RXN0-5390 (reaction.ecocyc.RXN0-5390).

## Annotation

EcoCyc complex THIOESTERII-CPLX

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.ACYL-COA-HYDROLASE-RXN|reaction.ecocyc.ACYL-COA-HYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14251|reaction.ecocyc.RXN-14251]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14255|reaction.ecocyc.RXN-14255]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5390|reaction.ecocyc.RXN0-5390]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AGG2|protein.P0AGG2]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:THIOESTERII-CPLX`
- `QSPROTEOME:QS00049553`

## Notes

4*protein.P0AGG2
