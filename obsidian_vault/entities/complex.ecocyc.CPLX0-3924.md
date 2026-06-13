---
entity_id: "complex.ecocyc.CPLX0-3924"
entity_type: "complex"
name: "peptidyl-prolyl cis-trans isomerase FklB"
source_database: "EcoCyc"
source_id: "CPLX0-3924"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# peptidyl-prolyl cis-trans isomerase FklB

`complex.ecocyc.CPLX0-3924`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3924`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PERI-BAC-GN
- Complex type: `structural`
- Components: [[protein.P0A9L3|protein.P0A9L3]]

## Enriched Summary

EcoCyc complex CPLX0-3924

## Biological Role

Catalyzes PEPTIDYLPROLYL-ISOMERASE-RXN (reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN).

## Annotation

EcoCyc complex CPLX0-3924

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN|reaction.ecocyc.PEPTIDYLPROLYL-ISOMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9L3|protein.P0A9L3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3924`
- `QSPROTEOME:QS00049615`

## Notes

2*protein.P0A9L3
