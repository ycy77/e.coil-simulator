---
entity_id: "complex.ecocyc.COBU-CPLX"
entity_type: "complex"
name: "cobinamide-P guanylyltransferase / cobinamide kinase"
source_database: "EcoCyc"
source_id: "COBU-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cobinamide-P guanylyltransferase / cobinamide kinase

`complex.ecocyc.COBU-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:COBU-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AE76|protein.P0AE76]]

## Enriched Summary

EcoCyc complex COBU-CPLX

## Biological Role

Catalyzes COBINAMIDEKIN-RXN (reaction.ecocyc.COBINAMIDEKIN-RXN), COBINPGUANYLYLTRANS-RXN (reaction.ecocyc.COBINPGUANYLYLTRANS-RXN).

## Annotation

EcoCyc complex COBU-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.COBINAMIDEKIN-RXN|reaction.ecocyc.COBINAMIDEKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.COBINPGUANYLYLTRANS-RXN|reaction.ecocyc.COBINPGUANYLYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AE76|protein.P0AE76]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:COBU-CPLX`
- `QSPROTEOME:QS00201593`

## Notes

2*protein.P0AE76
