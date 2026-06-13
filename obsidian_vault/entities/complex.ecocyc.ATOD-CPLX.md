---
entity_id: "complex.ecocyc.ATOD-CPLX"
entity_type: "complex"
name: "cetyl-CoA:acetoacetyl-CoA transferase subunit α dimer"
source_database: "EcoCyc"
source_id: "ATOD-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cetyl-CoA:acetoacetyl-CoA transferase subunit α dimer

`complex.ecocyc.ATOD-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ATOD-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76458|protein.P76458]]

## Enriched Summary

EcoCyc complex ATOD-CPLX

## Biological Role

Component of acetoacetyl-CoA transferase (complex.ecocyc.ACETOACETYL-COA-TRANSFER-CPLX).

## Annotation

EcoCyc complex ATOD-CPLX

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ACETOACETYL-COA-TRANSFER-CPLX|complex.ecocyc.ACETOACETYL-COA-TRANSFER-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P76458|protein.P76458]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ATOD-CPLX`
- `QSPROTEOME:QS00180861`

## Notes

2*protein.P76458
