---
entity_id: "complex.ecocyc.AGMATIN-CPLX"
entity_type: "complex"
name: "agmatinase"
source_database: "EcoCyc"
source_id: "AGMATIN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# agmatinase

`complex.ecocyc.AGMATIN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:AGMATIN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P60651|protein.P60651]]

## Enriched Summary

EcoCyc complex AGMATIN-CPLX

## Biological Role

Catalyzes AGMATIN-RXN (reaction.ecocyc.AGMATIN-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex AGMATIN-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.AGMATIN-RXN|reaction.ecocyc.AGMATIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P60651|protein.P60651]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:AGMATIN-CPLX`
- `QSPROTEOME:QS00049542`

## Notes

2*protein.P60651
