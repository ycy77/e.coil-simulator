---
entity_id: "complex.ecocyc.ASPCARBCAT-TRIMER"
entity_type: "complex"
name: "aspartate carbamoyltransferase catalytic subunit"
source_database: "EcoCyc"
source_id: "ASPCARBCAT-TRIMER"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# aspartate carbamoyltransferase catalytic subunit

`complex.ecocyc.ASPCARBCAT-TRIMER`

## Static

- Type: `complex`
- Source: `EcoCyc:ASPCARBCAT-TRIMER`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A786|protein.P0A786]]

## Enriched Summary

The catalytic subunit is enzymatically active but lacks the homotropic response to the substates, and is insensitive to inhibition by CTP . The catalytic subunit is enzymatically active but lacks the homotropic response to the substates, and is insensitive to inhibition by CTP .

## Biological Role

Component of aspartate carbamoyltransferase (complex.ecocyc.ASPCARBTRANS-CPLX).

## Annotation

The catalytic subunit is enzymatically active but lacks the homotropic response to the substates, and is insensitive to inhibition by CTP .

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ASPCARBTRANS-CPLX|complex.ecocyc.ASPCARBTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A786|protein.P0A786]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:ASPCARBCAT-TRIMER`
- `QSPROTEOME:QS00151893`

## Notes

3*protein.P0A786
