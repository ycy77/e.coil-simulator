---
entity_id: "complex.ecocyc.CPLX0-7718"
entity_type: "complex"
name: "UDP-4-amino-4-deoxy-L-arabinose formyltransferase/UDP-glucuronate dehydrogenase"
source_database: "EcoCyc"
source_id: "CPLX0-7718"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# UDP-4-amino-4-deoxy-L-arabinose formyltransferase/UDP-glucuronate dehydrogenase

`complex.ecocyc.CPLX0-7718`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7718`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77398|protein.P77398]]

## Enriched Summary

EcoCyc complex CPLX0-7718

## Biological Role

Catalyzes RXN0-1861 (reaction.ecocyc.RXN0-1861), RXN0-1862 (reaction.ecocyc.RXN0-1862).

## Annotation

EcoCyc complex CPLX0-7718

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1861|reaction.ecocyc.RXN0-1861]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-1862|reaction.ecocyc.RXN0-1862]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77398|protein.P77398]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-7718`
- `QSPROTEOME:QS00181505`

## Notes

6*protein.P77398
