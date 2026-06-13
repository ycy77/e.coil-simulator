---
entity_id: "complex.ecocyc.PHOSACETYLTRANS-CPLX"
entity_type: "complex"
name: "phosphate acetyltransferase"
source_database: "EcoCyc"
source_id: "PHOSACETYLTRANS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# phosphate acetyltransferase

`complex.ecocyc.PHOSACETYLTRANS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PHOSACETYLTRANS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9M8|protein.P0A9M8]]

## Enriched Summary

EcoCyc complex PHOSACETYLTRANS-CPLX

## Biological Role

Catalyzes PHOSACETYLTRANS-RXN (reaction.ecocyc.PHOSACETYLTRANS-RXN), PTAALT-RXN (reaction.ecocyc.PTAALT-RXN).

## Annotation

EcoCyc complex PHOSACETYLTRANS-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.PHOSACETYLTRANS-RXN|reaction.ecocyc.PHOSACETYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PTAALT-RXN|reaction.ecocyc.PTAALT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9M8|protein.P0A9M8]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:PHOSACETYLTRANS-CPLX`
- `QSPROTEOME:QS00197037`

## Notes

6*protein.P0A9M8
