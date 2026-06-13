---
entity_id: "complex.ecocyc.CPLX0-3950"
entity_type: "complex"
name: "tRNA m1G37 methyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-3950"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tRNA m1G37 methyltransferase

`complex.ecocyc.CPLX0-3950`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3950`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A873|protein.P0A873]]

## Enriched Summary

EcoCyc complex CPLX0-3950

## Biological Role

Catalyzes S-adenosyl-L-methionine:tRNA (guanine37-N1)-methyltransferase (reaction.ecocyc.RXN-12458). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-3950

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-12458|reaction.ecocyc.RXN-12458]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A873|protein.P0A873]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3950`
- `QSPROTEOME:QS00151413`

## Notes

2*protein.P0A873
