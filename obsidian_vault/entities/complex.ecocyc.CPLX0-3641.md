---
entity_id: "complex.ecocyc.CPLX0-3641"
entity_type: "complex"
name: "γ-aminobutyraldehyde dehydrogenase"
source_database: "EcoCyc"
source_id: "CPLX0-3641"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# γ-aminobutyraldehyde dehydrogenase

`complex.ecocyc.CPLX0-3641`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3641`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77674|protein.P77674]]

## Enriched Summary

EcoCyc complex CPLX0-3641

## Biological Role

Catalyzes AMINOBUTDEHYDROG-RXN (reaction.ecocyc.AMINOBUTDEHYDROG-RXN), RXN0-7318 (reaction.ecocyc.RXN0-7318).

## Annotation

EcoCyc complex CPLX0-3641

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.AMINOBUTDEHYDROG-RXN|reaction.ecocyc.AMINOBUTDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7318|reaction.ecocyc.RXN0-7318]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77674|protein.P77674]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-3641`
- `QSPROTEOME:QS00181681`

## Notes

4*protein.P77674
