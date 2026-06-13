---
entity_id: "complex.ecocyc.RHAMNULPALDOL-CPLX"
entity_type: "complex"
name: "rhamnulose-1-phosphate aldolase"
source_database: "EcoCyc"
source_id: "RHAMNULPALDOL-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# rhamnulose-1-phosphate aldolase

`complex.ecocyc.RHAMNULPALDOL-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:RHAMNULPALDOL-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P32169|protein.P32169]]

## Enriched Summary

EcoCyc complex RHAMNULPALDOL-CPLX

## Biological Role

Catalyzes RHAMNULPALDOL-RXN (reaction.ecocyc.RHAMNULPALDOL-RXN). Bound by Zinc cation (molecule.C00038), Potassium cation (molecule.C00238).

## Annotation

EcoCyc complex RHAMNULPALDOL-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RHAMNULPALDOL-RXN|reaction.ecocyc.RHAMNULPALDOL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P32169|protein.P32169]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:RHAMNULPALDOL-CPLX`
- `QSPROTEOME:QS00195943`

## Notes

4*protein.P32169
