---
entity_id: "complex.ecocyc.CPLX0-8553"
entity_type: "complex"
name: "ferric catecholate outer membrane transport complex II"
source_database: "EcoCyc"
source_id: "CPLX0-8553"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "iron-catecholate outer membrane transport complex II"
---

# ferric catecholate outer membrane transport complex II

`complex.ecocyc.CPLX0-8553`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8553`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]], [[protein.P17315|protein.P17315]]

## Enriched Summary

EcoCyc complex CPLX0-8553

## Biological Role

Catalyzes TRANS-RXN-1598 (reaction.ecocyc.TRANS-RXN-1598).

## Annotation

EcoCyc complex CPLX0-8553

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-1598|reaction.ecocyc.TRANS-RXN-1598]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-1923|complex.ecocyc.CPLX0-1923]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P02929|protein.P02929]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABU7|protein.P0ABU7]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=5
- `is_component_of` <-- [[protein.P0ABV2|protein.P0ABV2]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P17315|protein.P17315]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-8553`
- `PDB:8VGC`
- `PDB:8VGD`
- `QSPROTEOME:QS00188605`

## Notes

1*complex.ecocyc.CPLX0-1923|protein.P17315
