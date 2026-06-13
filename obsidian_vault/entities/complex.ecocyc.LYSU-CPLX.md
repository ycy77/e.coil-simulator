---
entity_id: "complex.ecocyc.LYSU-CPLX"
entity_type: "complex"
name: "lysine—tRNA ligase"
source_database: "EcoCyc"
source_id: "LYSU-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "lysyl-tRNA synthetase"
---

# lysine—tRNA ligase

`complex.ecocyc.LYSU-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:LYSU-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A8N5|protein.P0A8N5]]

## Enriched Summary

EcoCyc complex LYSU-CPLX

## Biological Role

Catalyzes LYSINE--TRNA-LIGASE-RXN (reaction.ecocyc.LYSINE--TRNA-LIGASE-RXN), RXN-23921 (reaction.ecocyc.RXN-23921), RXN-23924 (reaction.ecocyc.RXN-23924), RXN-23927 (reaction.ecocyc.RXN-23927), RXN0-5208 (reaction.ecocyc.RXN0-5208), RXN0-5209 (reaction.ecocyc.RXN0-5209), RXN0-7397 (reaction.ecocyc.RXN0-7397). Bound by L-Lysine (molecule.C00047), Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex LYSU-CPLX

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.LYSINE--TRNA-LIGASE-RXN|reaction.ecocyc.LYSINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23921|reaction.ecocyc.RXN-23921]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23924|reaction.ecocyc.RXN-23924]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-23927|reaction.ecocyc.RXN-23927]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5208|reaction.ecocyc.RXN0-5208]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5209|reaction.ecocyc.RXN0-5209]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7397|reaction.ecocyc.RXN0-7397]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A8N5|protein.P0A8N5]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:LYSU-CPLX`
- `QSPROTEOME:QS00160863`

## Notes

2*protein.P0A8N5
