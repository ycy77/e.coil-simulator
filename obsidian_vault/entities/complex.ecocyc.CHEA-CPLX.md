---
entity_id: "complex.ecocyc.CHEA-CPLX"
entity_type: "complex"
name: "chemotaxis protein CheA(L)"
source_database: "EcoCyc"
source_id: "CHEA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "chemotaxis kinase-phosphotransferase CheA(L)"
  - "CheA"
  - "CheAL"
---

# chemotaxis protein CheA(L)

`complex.ecocyc.CHEA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CHEA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07363|protein.P07363]]

## Enriched Summary

EcoCyc complex CHEA-CPLX

## Biological Role

Component of chemotaxis signaling complex core unit - dipeptide sensing (complex.ecocyc.TAP-CPLX), chemotaxis signaling complex core unit - aspartate sensing (complex.ecocyc.TAR-CPLX), chemotaxis signaling complex core unit - ribose/galactose/glucose sensing (complex.ecocyc.TRG-CPLX), chemotaxis signaling complex core unit - serine sensing (complex.ecocyc.TSR-CPLX).

## Annotation

EcoCyc complex CHEA-CPLX

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.TAP-CPLX|complex.ecocyc.TAP-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.TAR-CPLX|complex.ecocyc.TAR-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.TRG-CPLX|complex.ecocyc.TRG-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.TSR-CPLX|complex.ecocyc.TSR-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P07363|protein.P07363]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CHEA-CPLX`
- `QSPROTEOME:QS00049579`

## Notes

2*protein.P07363
