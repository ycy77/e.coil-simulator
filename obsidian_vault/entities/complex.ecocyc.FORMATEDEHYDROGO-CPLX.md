---
entity_id: "complex.ecocyc.FORMATEDEHYDROGO-CPLX"
entity_type: "complex"
name: "formate dehydrogenase O subcomplex"
source_database: "EcoCyc"
source_id: "FORMATEDEHYDROGO-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "FDH-O"
  - "FDH-Z"
  - "formate:quinone oxidoreductase O"
  - "formate:quinone oxidoreductase Z"
---

# formate dehydrogenase O subcomplex

`complex.ecocyc.FORMATEDEHYDROGO-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:FORMATEDEHYDROGO-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `structural`
- Components: [[protein.P32176|protein.P32176]], [[protein.P0AAJ5|protein.P0AAJ5]], [[protein.P0AEL0|protein.P0AEL0]]

## Enriched Summary

EcoCyc complex FORMATEDEHYDROGO-CPLX

## Biological Role

Component of formate dehydrogenase O (complex.ecocyc.CPLX0-13310).

## Annotation

EcoCyc complex FORMATEDEHYDROGO-CPLX

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-13310|complex.ecocyc.CPLX0-13310]] `EcoCyc` `database` - EcoCyc component coefficient=3

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0AAJ5|protein.P0AAJ5]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AEL0|protein.P0AEL0]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P32176|protein.P32176]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:FORMATEDEHYDROGO-CPLX`

## Notes

1*protein.P32176|1*protein.P0AAJ5|1*protein.P0AEL0
