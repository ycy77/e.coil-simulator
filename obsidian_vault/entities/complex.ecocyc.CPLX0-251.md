---
entity_id: "complex.ecocyc.CPLX0-251"
entity_type: "complex"
name: "2-methylcitrate synthase"
source_database: "EcoCyc"
source_id: "CPLX0-251"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "citrate synthase 2"
---

# 2-methylcitrate synthase

`complex.ecocyc.CPLX0-251`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-251`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P31660|protein.P31660]]

## Enriched Summary

EcoCyc complex CPLX0-251

## Biological Role

Catalyzes 2-METHYLCITRATE-SYNTHASE-RXN (reaction.ecocyc.2-METHYLCITRATE-SYNTHASE-RXN).

## Annotation

EcoCyc complex CPLX0-251

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2-METHYLCITRATE-SYNTHASE-RXN|reaction.ecocyc.2-METHYLCITRATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P31660|protein.P31660]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-251`
- `QSPROTEOME:QS00191675`

## Notes

2*protein.P31660
