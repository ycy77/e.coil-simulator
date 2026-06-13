---
entity_id: "complex.ecocyc.CPLX0-1401"
entity_type: "complex"
name: "2,3-diaminopropionate ammonia-lyase"
source_database: "EcoCyc"
source_id: "CPLX0-1401"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 2,3-diaminopropionate ammonia-lyase

`complex.ecocyc.CPLX0-1401`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1401`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P66899|protein.P66899]]

## Enriched Summary

EcoCyc complex CPLX0-1401

## Biological Role

Catalyzes 4.3.1.15-RXN (reaction.ecocyc.4.3.1.15-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex CPLX0-1401

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.4.3.1.15-RXN|reaction.ecocyc.4.3.1.15-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P66899|protein.P66899]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-1401`
- `QSPROTEOME:QS00165605`

## Notes

2*protein.P66899
