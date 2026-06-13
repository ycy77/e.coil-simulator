---
entity_id: "complex.ecocyc.ATOA-CPLX"
entity_type: "complex"
name: "acetyl-CoA:acetoacetyl-CoA transferase subunit β dimer"
source_database: "EcoCyc"
source_id: "ATOA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# acetyl-CoA:acetoacetyl-CoA transferase subunit β dimer

`complex.ecocyc.ATOA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ATOA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76459|protein.P76459]]

## Enriched Summary

EcoCyc complex ATOA-CPLX

## Biological Role

Component of acetoacetyl-CoA transferase (complex.ecocyc.ACETOACETYL-COA-TRANSFER-CPLX).

## Annotation

EcoCyc complex ATOA-CPLX

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ACETOACETYL-COA-TRANSFER-CPLX|complex.ecocyc.ACETOACETYL-COA-TRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P76459|protein.P76459]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ATOA-CPLX`
- `QSPROTEOME:QS00049574`

## Notes

2*protein.P76459
