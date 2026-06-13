---
entity_id: "complex.ecocyc.CPLX0-7726"
entity_type: "complex"
name: "23S rRNA m5C1962 methyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-7726"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ribosomal RNA large subunit methyltransferase I"
---

# 23S rRNA m5C1962 methyltransferase

`complex.ecocyc.CPLX0-7726`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7726`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P75876|protein.P75876]]

## Enriched Summary

EcoCyc complex CPLX0-7726

## Biological Role

Catalyzes RXN-11602 (reaction.ecocyc.RXN-11602).

## Annotation

EcoCyc complex CPLX0-7726

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11602|reaction.ecocyc.RXN-11602]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P75876|protein.P75876]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7726`
- `QSPROTEOME:QS00182023`

## Notes

2*protein.P75876
