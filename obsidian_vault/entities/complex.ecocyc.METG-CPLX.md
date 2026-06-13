---
entity_id: "complex.ecocyc.METG-CPLX"
entity_type: "complex"
name: "methionine—tRNA ligase"
source_database: "EcoCyc"
source_id: "METG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# methionine—tRNA ligase

`complex.ecocyc.METG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:METG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00959|protein.P00959]]

## Enriched Summary

EcoCyc complex METG-CPLX

## Biological Role

Catalyzes METHIONINE--TRNA-LIGASE-RXN (reaction.ecocyc.METHIONINE--TRNA-LIGASE-RXN), RXN-16165 (reaction.ecocyc.RXN-16165), RXN-23924 (reaction.ecocyc.RXN-23924). Bound by Zinc cation (molecule.C00038), Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex METG-CPLX

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.METHIONINE--TRNA-LIGASE-RXN|reaction.ecocyc.METHIONINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-16165|reaction.ecocyc.RXN-16165]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23924|reaction.ecocyc.RXN-23924]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00959|protein.P00959]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:METG-CPLX`
- `QSPROTEOME:QS00049731`

## Notes

2*protein.P00959
