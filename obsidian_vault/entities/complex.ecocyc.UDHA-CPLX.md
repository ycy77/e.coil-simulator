---
entity_id: "complex.ecocyc.UDHA-CPLX"
entity_type: "complex"
name: "soluble pyridine nucleotide transhydrogenase"
source_database: "EcoCyc"
source_id: "UDHA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# soluble pyridine nucleotide transhydrogenase

`complex.ecocyc.UDHA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:UDHA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P27306|protein.P27306]]

## Enriched Summary

EcoCyc complex UDHA-CPLX

## Biological Role

Catalyzes PYRNUTRANSHYDROGEN-RXN (reaction.ecocyc.PYRNUTRANSHYDROGEN-RXN), RXN-10745 (reaction.ecocyc.RXN-10745), RXN0-7427 (reaction.ecocyc.RXN0-7427). Bound by FAD (molecule.C00016).

## Annotation

EcoCyc complex UDHA-CPLX

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.PYRNUTRANSHYDROGEN-RXN|reaction.ecocyc.PYRNUTRANSHYDROGEN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-10745|reaction.ecocyc.RXN-10745]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7427|reaction.ecocyc.RXN0-7427]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P27306|protein.P27306]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## External IDs

- `EcoCyc:UDHA-CPLX`
- `QSPROTEOME:QS00188557`

## Notes

8*protein.P27306
