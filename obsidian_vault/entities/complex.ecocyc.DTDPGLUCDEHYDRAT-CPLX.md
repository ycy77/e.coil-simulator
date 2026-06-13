---
entity_id: "complex.ecocyc.DTDPGLUCDEHYDRAT-CPLX"
entity_type: "complex"
name: "dTDP-glucose 4,6-dehydratase 1"
source_database: "EcoCyc"
source_id: "DTDPGLUCDEHYDRAT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# dTDP-glucose 4,6-dehydratase 1

`complex.ecocyc.DTDPGLUCDEHYDRAT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DTDPGLUCDEHYDRAT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P37759|protein.P37759]]

## Enriched Summary

EcoCyc complex DTDPGLUCDEHYDRAT-CPLX

## Biological Role

Catalyzes DTDPGLUCDEHYDRAT-RXN (reaction.ecocyc.DTDPGLUCDEHYDRAT-RXN). Bound by NAD+ (molecule.C00003).

## Annotation

EcoCyc complex DTDPGLUCDEHYDRAT-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DTDPGLUCDEHYDRAT-RXN|reaction.ecocyc.DTDPGLUCDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P37759|protein.P37759]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:DTDPGLUCDEHYDRAT-CPLX`
- `QSPROTEOME:QS00182701`

## Notes

2*protein.P37759
