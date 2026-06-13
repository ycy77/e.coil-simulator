---
entity_id: "complex.ecocyc.3-METHYL-2-OXOBUT-OHCH3XFER-CPLX"
entity_type: "complex"
name: "3-methyl-2-oxobutanoate hydroxymethyltransferase"
source_database: "EcoCyc"
source_id: "3-METHYL-2-OXOBUT-OHCH3XFER-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 3-methyl-2-oxobutanoate hydroxymethyltransferase

`complex.ecocyc.3-METHYL-2-OXOBUT-OHCH3XFER-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:3-METHYL-2-OXOBUT-OHCH3XFER-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P31057|protein.P31057]]

## Enriched Summary

EcoCyc complex 3-METHYL-2-OXOBUT-OHCH3XFER-CPLX

## Biological Role

Catalyzes 3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN (reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex 3-METHYL-2-OXOBUT-OHCH3XFER-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN|reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P31057|protein.P31057]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## External IDs

- `EcoCyc:3-METHYL-2-OXOBUT-OHCH3XFER-CPLX`
- `QSPROTEOME:QS00182017`

## Notes

10*protein.P31057
