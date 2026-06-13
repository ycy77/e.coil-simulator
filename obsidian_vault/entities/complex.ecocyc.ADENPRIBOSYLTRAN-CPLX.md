---
entity_id: "complex.ecocyc.ADENPRIBOSYLTRAN-CPLX"
entity_type: "complex"
name: "adenine phosphoribosyltransferase"
source_database: "EcoCyc"
source_id: "ADENPRIBOSYLTRAN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# adenine phosphoribosyltransferase

`complex.ecocyc.ADENPRIBOSYLTRAN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ADENPRIBOSYLTRAN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P69503|protein.P69503]]

## Enriched Summary

EcoCyc complex ADENPRIBOSYLTRAN-CPLX

## Biological Role

Catalyzes ADENPRIBOSYLTRAN-RXN (reaction.ecocyc.ADENPRIBOSYLTRAN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex ADENPRIBOSYLTRAN-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ADENPRIBOSYLTRAN-RXN|reaction.ecocyc.ADENPRIBOSYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P69503|protein.P69503]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ADENPRIBOSYLTRAN-CPLX`
- `QSPROTEOME:QS00182039`

## Notes

2*protein.P69503
