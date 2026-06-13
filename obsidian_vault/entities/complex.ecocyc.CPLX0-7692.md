---
entity_id: "complex.ecocyc.CPLX0-7692"
entity_type: "complex"
name: "nucleoside triphosphate pyrophosphohydrolase"
source_database: "EcoCyc"
source_id: "CPLX0-7692"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# nucleoside triphosphate pyrophosphohydrolase

`complex.ecocyc.CPLX0-7692`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7692`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AEY3|protein.P0AEY3]]

## Enriched Summary

EcoCyc complex CPLX0-7692

## Biological Role

Catalyzes NUCLEOTIDE-PYROPHOSPHATASE-RXN (reaction.ecocyc.NUCLEOTIDE-PYROPHOSPHATASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex CPLX0-7692

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.NUCLEOTIDE-PYROPHOSPHATASE-RXN|reaction.ecocyc.NUCLEOTIDE-PYROPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AEY3|protein.P0AEY3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7692`
- `QSPROTEOME:QS00160725`

## Notes

2*protein.P0AEY3
