---
entity_id: "complex.ecocyc.CPLX0-246"
entity_type: "complex"
name: "L-cysteine desulfurase SufS"
source_database: "EcoCyc"
source_id: "CPLX0-246"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-cysteine desulfurase SufS

`complex.ecocyc.CPLX0-246`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-246`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77444|protein.P77444]]

## Enriched Summary

EcoCyc complex CPLX0-246

## Biological Role

Catalyzes RXN0-7439 (reaction.ecocyc.RXN0-7439), RXN0-7442 (reaction.ecocyc.RXN0-7442). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex CPLX0-246

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7439|reaction.ecocyc.RXN0-7439]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7442|reaction.ecocyc.RXN0-7442]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P77444|protein.P77444]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-246`
- `QSPROTEOME:QS00093706`

## Notes

2*protein.P77444
