---
entity_id: "complex.ecocyc.ADHC-CPLX"
entity_type: "complex"
name: "S-(hydroxymethyl)glutathione dehydrogenase"
source_database: "EcoCyc"
source_id: "ADHC-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# S-(hydroxymethyl)glutathione dehydrogenase

`complex.ecocyc.ADHC-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ADHC-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P25437|protein.P25437]]

## Enriched Summary

EcoCyc complex ADHC-CPLX

## Biological Role

Catalyzes RXN-2962 (reaction.ecocyc.RXN-2962). Bound by Zinc cation (molecule.C00038).

## Annotation

EcoCyc complex ADHC-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-2962|reaction.ecocyc.RXN-2962]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P25437|protein.P25437]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ADHC-CPLX`
- `QSPROTEOME:QS00049541`

## Notes

2*protein.P25437
