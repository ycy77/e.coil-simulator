---
entity_id: "complex.ecocyc.SUCC-DEHASE"
entity_type: "complex"
name: "succinate:quinone oxidoreductase subcomplex"
source_database: "EcoCyc"
source_id: "SUCC-DEHASE"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "SQR"
---

# succinate:quinone oxidoreductase subcomplex

`complex.ecocyc.SUCC-DEHASE`

## Static

- Type: `complex`
- Source: `EcoCyc:SUCC-DEHASE`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P0AC41|protein.P0AC41]], [[protein.P07014|protein.P07014]], [[protein.P69054|protein.P69054]], [[protein.P0AC44|protein.P0AC44]]

## Enriched Summary

EcoCyc complex SUCC-DEHASE

## Biological Role

Component of succinate:quinone oxidoreductase (complex.ecocyc.CPLX0-8160).

## Annotation

EcoCyc complex SUCC-DEHASE

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8160|complex.ecocyc.CPLX0-8160]] `EcoCyc` `database` - EcoCyc component coefficient=3

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P07014|protein.P07014]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AC41|protein.P0AC41]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AC44|protein.P0AC44]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P69054|protein.P69054]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:SUCC-DEHASE`
- `PDB:1NEN`
- `PDB:2WU5`
- `PDB:2WU2`
- `PDB:2WS3`
- `PDB:2WP9`
- `PDB:2WDV`
- `PDB:2WDR`
- `PDB:2WDQ`
- `QSPROTEOME:QS00181507`

## Notes

1*protein.P0AC41|1*protein.P07014|1*protein.P69054|1*protein.P0AC44
