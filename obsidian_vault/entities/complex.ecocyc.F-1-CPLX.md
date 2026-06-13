---
entity_id: "complex.ecocyc.F-1-CPLX"
entity_type: "complex"
name: "ATP synthase F1 complex"
source_database: "EcoCyc"
source_id: "F-1-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ATP synthase F1 complex

`complex.ecocyc.F-1-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:F-1-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6E6|protein.P0A6E6]], [[protein.P0ABA4|protein.P0ABA4]], [[complex.ecocyc.ATPA-CPLX|complex.ecocyc.ATPA-CPLX]], [[protein.P0ABA6|protein.P0ABA6]], [[complex.ecocyc.ATPD-CPLX|complex.ecocyc.ATPD-CPLX]]

## Enriched Summary

The F1 complex of ATP synthase contains the catalytic sites. The complex consists of five subunits, each of which is required for activity . The positive catalytic cooperativity of ATP hydrolysis by the F1 complex has been studied . The F1 complex of ATP synthase contains the catalytic sites. The complex consists of five subunits, each of which is required for activity . The positive catalytic cooperativity of ATP hydrolysis by the F1 complex has been studied .

## Biological Role

Component of ATP synthase / thiamin triphosphate synthase (complex.ecocyc.ATPSYN-CPLX).

## Annotation

The F1 complex of ATP synthase contains the catalytic sites. The complex consists of five subunits, each of which is required for activity . The positive catalytic cooperativity of ATP hydrolysis by the F1 complex has been studied .

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ATPSYN-CPLX|complex.ecocyc.ATPSYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (7)

- `is_component_of` <-- [[complex.ecocyc.ATPA-CPLX|complex.ecocyc.ATPA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.ATPD-CPLX|complex.ecocyc.ATPD-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P0A6E6|protein.P0A6E6]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABA4|protein.P0ABA4]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABA6|protein.P0ABA6]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABB0|protein.P0ABB0]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` <-- [[protein.P0ABB4|protein.P0ABB4]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:F-1-CPLX`
- `PDB:1FS0`
- `PDB:3OAA`
- `PDB:5T4Q`
- `PDB:5T4P`
- `PDB:5T4O`
- `PDB:6WNR`
- `PDB:6WNQ`
- `PDB:6PQV`
- `QSPROTEOME:QS00196933`

## Notes

1*protein.P0A6E6|1*protein.P0ABA4|1*complex.ecocyc.ATPA-CPLX|1*protein.P0ABA6|1*complex.ecocyc.ATPD-CPLX
