---
entity_id: "complex.ecocyc.PORPHOBILSYNTH-CPLX"
entity_type: "complex"
name: "porphobilinogen synthase"
source_database: "EcoCyc"
source_id: "PORPHOBILSYNTH-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# porphobilinogen synthase

`complex.ecocyc.PORPHOBILSYNTH-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PORPHOBILSYNTH-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ACB2|protein.P0ACB2]]

## Enriched Summary

EcoCyc complex PORPHOBILSYNTH-CPLX

## Biological Role

Catalyzes PORPHOBILSYNTH-RXN (reaction.ecocyc.PORPHOBILSYNTH-RXN). Bound by Zinc cation (molecule.C00038).

## Annotation

EcoCyc complex PORPHOBILSYNTH-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PORPHOBILSYNTH-RXN|reaction.ecocyc.PORPHOBILSYNTH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0ACB2|protein.P0ACB2]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## External IDs

- `EcoCyc:PORPHOBILSYNTH-CPLX`
- `QSPROTEOME:QS00188429`

## Notes

8*protein.P0ACB2
