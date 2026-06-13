---
entity_id: "complex.ecocyc.CPLX0-7625"
entity_type: "complex"
name: "dCMP phosphohydrolase"
source_database: "EcoCyc"
source_id: "CPLX0-7625"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# dCMP phosphohydrolase

`complex.ecocyc.CPLX0-7625`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7625`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76491|protein.P76491]]

## Enriched Summary

EcoCyc complex CPLX0-7625

## Biological Role

Catalyzes RXN-14143 (reaction.ecocyc.RXN-14143), RXN-14161 (reaction.ecocyc.RXN-14161), RXN0-3741 (reaction.ecocyc.RXN0-3741), RXN0-5292 (reaction.ecocyc.RXN0-5292). Bound by Cobalt ion (molecule.C00175).

## Annotation

EcoCyc complex CPLX0-7625

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.RXN-14143|reaction.ecocyc.RXN-14143]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14161|reaction.ecocyc.RXN-14161]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3741|reaction.ecocyc.RXN0-3741]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5292|reaction.ecocyc.RXN0-5292]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P76491|protein.P76491]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7625`
- `QSPROTEOME:QS00183233`

## Notes

2*protein.P76491
