---
entity_id: "complex.ecocyc.CPLX0-7717"
entity_type: "complex"
name: "peptidoglycan glycosyltransferase / peptidoglycan DD-transpeptidase MrcA"
source_database: "EcoCyc"
source_id: "CPLX0-7717"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "penicillin binding protein 1A"
---

# peptidoglycan glycosyltransferase / peptidoglycan DD-transpeptidase MrcA

`complex.ecocyc.CPLX0-7717`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7717`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P02918|protein.P02918]]

## Enriched Summary

EcoCyc complex CPLX0-7717

## Biological Role

Catalyzes RXN-16649 (reaction.ecocyc.RXN-16649), RXN-16650 (reaction.ecocyc.RXN-16650), peptidoglycan transpeptidase (Gram-negative bacteria) (reaction.ecocyc.RXN-16659).

## Annotation

EcoCyc complex CPLX0-7717

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-16649|reaction.ecocyc.RXN-16649]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-16650|reaction.ecocyc.RXN-16650]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-16659|reaction.ecocyc.RXN-16659]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P02918|protein.P02918]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7717`
- `QSPROTEOME:QS00049644`

## Notes

2*protein.P02918
