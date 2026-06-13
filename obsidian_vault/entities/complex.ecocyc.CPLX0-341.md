---
entity_id: "complex.ecocyc.CPLX0-341"
entity_type: "complex"
name: "fused 4'-phosphopantothenoylcysteine decarboxylase and phosphopantothenoylcysteine synthetase"
source_database: "EcoCyc"
source_id: "CPLX0-341"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# fused 4'-phosphopantothenoylcysteine decarboxylase and phosphopantothenoylcysteine synthetase

`complex.ecocyc.CPLX0-341`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-341`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ABQ0|protein.P0ABQ0]]

## Enriched Summary

EcoCyc complex CPLX0-341

## Biological Role

Catalyzes P-PANTOCYSDECARB-RXN (reaction.ecocyc.P-PANTOCYSDECARB-RXN), P-PANTOCYSLIG-RXN (reaction.ecocyc.P-PANTOCYSLIG-RXN). Bound by FMN (molecule.C00061), Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-341

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.P-PANTOCYSDECARB-RXN|reaction.ecocyc.P-PANTOCYSDECARB-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.P-PANTOCYSLIG-RXN|reaction.ecocyc.P-PANTOCYSLIG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0ABQ0|protein.P0ABQ0]] `EcoCyc` `database` - EcoCyc component coefficient=12 | EcoCyc protcplxs.col coefficient=12

## External IDs

- `EcoCyc:CPLX0-341`
- `QSPROTEOME:QS00181875`

## Notes

12*protein.P0ABQ0
