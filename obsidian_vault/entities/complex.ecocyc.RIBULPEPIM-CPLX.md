---
entity_id: "complex.ecocyc.RIBULPEPIM-CPLX"
entity_type: "complex"
name: "L-ribulose-5-phosphate 4-epimerase AraD"
source_database: "EcoCyc"
source_id: "RIBULPEPIM-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-ribulose-5-phosphate 4-epimerase AraD

`complex.ecocyc.RIBULPEPIM-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:RIBULPEPIM-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P08203|protein.P08203]]

## Enriched Summary

EcoCyc complex RIBULPEPIM-CPLX

## Biological Role

Catalyzes RIBULPEPIM-RXN (reaction.ecocyc.RIBULPEPIM-RXN). Bound by Zinc cation (molecule.C00038).

## Annotation

EcoCyc complex RIBULPEPIM-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RIBULPEPIM-RXN|reaction.ecocyc.RIBULPEPIM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P08203|protein.P08203]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:RIBULPEPIM-CPLX`
- `QSPROTEOME:QS00195209`

## Notes

4*protein.P08203
