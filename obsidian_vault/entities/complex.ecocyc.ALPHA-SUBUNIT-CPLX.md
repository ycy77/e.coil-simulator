---
entity_id: "complex.ecocyc.ALPHA-SUBUNIT-CPLX"
entity_type: "complex"
name: "formate dehydrogenase N, subcomplex"
source_database: "EcoCyc"
source_id: "ALPHA-SUBUNIT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# formate dehydrogenase N, subcomplex

`complex.ecocyc.ALPHA-SUBUNIT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ALPHA-SUBUNIT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AEK7|protein.P0AEK7]], [[protein.P0AAJ3|protein.P0AAJ3]], [[protein.P24183|protein.P24183]]

## Enriched Summary

EcoCyc complex ALPHA-SUBUNIT-CPLX

## Biological Role

Component of formate dehydrogenase N (complex.ecocyc.FORMATEDEHYDROGN-CPLX).

## Annotation

EcoCyc complex ALPHA-SUBUNIT-CPLX

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.FORMATEDEHYDROGN-CPLX|complex.ecocyc.FORMATEDEHYDROGN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0AAJ3|protein.P0AAJ3]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AEK7|protein.P0AEK7]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P24183|protein.P24183]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:ALPHA-SUBUNIT-CPLX`
- `PDB:1KQF`
- `PDB:1KQG`

## Notes

1*protein.P0AEK7|1*protein.P0AAJ3|1*protein.P24183
