---
entity_id: "complex.ecocyc.S-ADENMETSYN-CPLX"
entity_type: "complex"
name: "methionine adenosyltransferase"
source_database: "EcoCyc"
source_id: "S-ADENMETSYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# methionine adenosyltransferase

`complex.ecocyc.S-ADENMETSYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:S-ADENMETSYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A817|protein.P0A817]]

## Enriched Summary

EcoCyc complex S-ADENMETSYN-CPLX

## Biological Role

Catalyzes S-ADENMETSYN-RXN (reaction.ecocyc.S-ADENMETSYN-RXN). Bound by Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex S-ADENMETSYN-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.S-ADENMETSYN-RXN|reaction.ecocyc.S-ADENMETSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A817|protein.P0A817]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:S-ADENMETSYN-CPLX`
- `QSPROTEOME:QS00188421`

## Notes

4*protein.P0A817
