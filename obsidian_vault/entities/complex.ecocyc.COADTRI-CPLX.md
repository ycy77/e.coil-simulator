---
entity_id: "complex.ecocyc.COADTRI-CPLX"
entity_type: "complex"
name: "pantetheine-phosphate adenylyltransferase"
source_database: "EcoCyc"
source_id: "COADTRI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# pantetheine-phosphate adenylyltransferase

`complex.ecocyc.COADTRI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:COADTRI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6I6|protein.P0A6I6]]

## Enriched Summary

EcoCyc complex COADTRI-CPLX

## Biological Role

Catalyzes PANTEPADENYLYLTRAN-RXN (reaction.ecocyc.PANTEPADENYLYLTRAN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex COADTRI-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PANTEPADENYLYLTRAN-RXN|reaction.ecocyc.PANTEPADENYLYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A6I6|protein.P0A6I6]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:COADTRI-CPLX`
- `QSPROTEOME:QS00188547`

## Notes

6*protein.P0A6I6
