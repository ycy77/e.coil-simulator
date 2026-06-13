---
entity_id: "complex.ecocyc.ASPCARBREG-DIMER"
entity_type: "complex"
name: "aspartate carbamoyltransferase, regulatory subunit"
source_database: "EcoCyc"
source_id: "ASPCARBREG-DIMER"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# aspartate carbamoyltransferase, regulatory subunit

`complex.ecocyc.ASPCARBREG-DIMER`

## Static

- Type: `complex`
- Source: `EcoCyc:ASPCARBREG-DIMER`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A7F3|protein.P0A7F3]]

## Enriched Summary

The regulatory subunit is catalytically inactive but contains the common binding site for the allosteric effectors CTP and ATP . Zn2+ binding to the regulatory subunit is important for its interaction with the catalytic subunit . The regulatory subunit is catalytically inactive but contains the common binding site for the allosteric effectors CTP and ATP . Zn2+ binding to the regulatory subunit is important for its interaction with the catalytic subunit .

## Biological Role

Component of aspartate carbamoyltransferase (complex.ecocyc.ASPCARBTRANS-CPLX).

## Annotation

The regulatory subunit is catalytically inactive but contains the common binding site for the allosteric effectors CTP and ATP . Zn2+ binding to the regulatory subunit is important for its interaction with the catalytic subunit .

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ASPCARBTRANS-CPLX|complex.ecocyc.ASPCARBTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A7F3|protein.P0A7F3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ASPCARBREG-DIMER`
- `QSPROTEOME:QS00049572`

## Notes

2*protein.P0A7F3
