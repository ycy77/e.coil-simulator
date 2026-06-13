---
entity_id: "complex.ecocyc.CPLX0-7727"
entity_type: "complex"
name: "16S rRNA m3U1498 methyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-7727"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ribosomal RNA small subunit methyltransferase E"
---

# 16S rRNA m3U1498 methyltransferase

`complex.ecocyc.CPLX0-7727`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7727`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AGL7|protein.P0AGL7]]

## Enriched Summary

EcoCyc complex CPLX0-7727

## Biological Role

Catalyzes RXN-11598 (reaction.ecocyc.RXN-11598).

## Annotation

EcoCyc complex CPLX0-7727

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11598|reaction.ecocyc.RXN-11598]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AGL7|protein.P0AGL7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7727`
- `QSPROTEOME:QS00199203`

## Notes

2*protein.P0AGL7
