---
entity_id: "complex.ecocyc.CPLX0-7712"
entity_type: "complex"
name: "GDP-mannose mannosyl hydrolase"
source_database: "EcoCyc"
source_id: "CPLX0-7712"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# GDP-mannose mannosyl hydrolase

`complex.ecocyc.CPLX0-7712`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7712`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P32056|protein.P32056]]

## Enriched Summary

EcoCyc complex CPLX0-7712

## Biological Role

Catalyzes GDP-GLUCOSIDASE-RXN (reaction.ecocyc.GDP-GLUCOSIDASE-RXN), GDPMANMANHYDRO-RXN (reaction.ecocyc.GDPMANMANHYDRO-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-7712

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GDP-GLUCOSIDASE-RXN|reaction.ecocyc.GDP-GLUCOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GDPMANMANHYDRO-RXN|reaction.ecocyc.GDPMANMANHYDRO-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P32056|protein.P32056]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7712`
- `QSPROTEOME:QS00183265`

## Notes

2*protein.P32056
