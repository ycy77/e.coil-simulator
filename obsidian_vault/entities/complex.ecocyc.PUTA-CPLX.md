---
entity_id: "complex.ecocyc.PUTA-CPLX"
entity_type: "complex"
name: "fused DNA-binding transcriptional repressor / proline dehydrogenase / 1-pyrroline-5-carboxylate dehydrogenase PutA"
source_database: "EcoCyc"
source_id: "PUTA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# fused DNA-binding transcriptional repressor / proline dehydrogenase / 1-pyrroline-5-carboxylate dehydrogenase PutA

`complex.ecocyc.PUTA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PUTA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P09546|protein.P09546]]

## Enriched Summary

EcoCyc complex PUTA-CPLX

## Biological Role

Catalyzes RXN-14116 (reaction.ecocyc.RXN-14116), RXN0-7008 (reaction.ecocyc.RXN0-7008). Bound by FAD (molecule.C00016).

## Annotation

EcoCyc complex PUTA-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-14116|reaction.ecocyc.RXN-14116]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7008|reaction.ecocyc.RXN0-7008]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P09546|protein.P09546]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PUTA-CPLX`
- `QSPROTEOME:QS00188733`

## Notes

2*protein.P09546
