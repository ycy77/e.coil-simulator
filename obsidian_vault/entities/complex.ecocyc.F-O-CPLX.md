---
entity_id: "complex.ecocyc.F-O-CPLX"
entity_type: "complex"
name: "ATP synthase Fo complex"
source_database: "EcoCyc"
source_id: "F-O-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ATP synthase Fo complex

`complex.ecocyc.F-O-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:F-O-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.ATPE-CPLX|complex.ecocyc.ATPE-CPLX]], [[complex.ecocyc.ATPF-CPLX|complex.ecocyc.ATPF-CPLX]], [[protein.P0AB98|protein.P0AB98]]

## Enriched Summary

The Fo complex of ATP synthase functions as the proton channel and consists of three subunits. All are required for a functional Fo complex. The Fo complex is membrane-bound. The Fo complex of ATP synthase functions as the proton channel and consists of three subunits. All are required for a functional Fo complex. The Fo complex is membrane-bound.

## Biological Role

Component of ATP synthase / thiamin triphosphate synthase (complex.ecocyc.ATPSYN-CPLX).

## Annotation

The Fo complex of ATP synthase functions as the proton channel and consists of three subunits. All are required for a functional Fo complex. The Fo complex is membrane-bound.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ATPSYN-CPLX|complex.ecocyc.ATPSYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (5)

- `is_component_of` <-- [[complex.ecocyc.ATPE-CPLX|complex.ecocyc.ATPE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.ATPF-CPLX|complex.ecocyc.ATPF-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P0AB98|protein.P0AB98]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABA0|protein.P0ABA0]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P68699|protein.P68699]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=10

## External IDs

- `EcoCyc:F-O-CPLX`
- `PDB:1C17`
- `PDB:5T4Q`
- `PDB:5T4P`
- `PDB:5T4O`
- `PDB:6WNR`
- `PDB:6WNQ`
- `PDB:6VWK`
- `PDB:6PQV`
- `QSPROTEOME:QS00188703`

## Notes

1*complex.ecocyc.ATPE-CPLX|1*complex.ecocyc.ATPF-CPLX|1*protein.P0AB98
