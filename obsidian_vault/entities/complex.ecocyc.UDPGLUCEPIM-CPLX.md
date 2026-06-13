---
entity_id: "complex.ecocyc.UDPGLUCEPIM-CPLX"
entity_type: "complex"
name: "UDP-glucose 4-epimerase"
source_database: "EcoCyc"
source_id: "UDPGLUCEPIM-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# UDP-glucose 4-epimerase

`complex.ecocyc.UDPGLUCEPIM-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:UDPGLUCEPIM-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P09147|protein.P09147]]

## Enriched Summary

EcoCyc complex UDPGLUCEPIM-CPLX

## Biological Role

Catalyzes UDPGLUCEPIM-RXN (reaction.ecocyc.UDPGLUCEPIM-RXN). Bound by NAD+ (molecule.C00003).

## Annotation

EcoCyc complex UDPGLUCEPIM-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.UDPGLUCEPIM-RXN|reaction.ecocyc.UDPGLUCEPIM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P09147|protein.P09147]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:UDPGLUCEPIM-CPLX`
- `QSPROTEOME:QS00183039`

## Notes

2*protein.P09147
