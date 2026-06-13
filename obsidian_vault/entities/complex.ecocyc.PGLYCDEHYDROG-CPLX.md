---
entity_id: "complex.ecocyc.PGLYCDEHYDROG-CPLX"
entity_type: "complex"
name: "phosphoglycerate dehydrogenase"
source_database: "EcoCyc"
source_id: "PGLYCDEHYDROG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# phosphoglycerate dehydrogenase

`complex.ecocyc.PGLYCDEHYDROG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PGLYCDEHYDROG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9T0|protein.P0A9T0]]

## Enriched Summary

EcoCyc complex PGLYCDEHYDROG-CPLX

## Biological Role

Catalyzes KETOGLUTREDUCT-RXN (reaction.ecocyc.KETOGLUTREDUCT-RXN), PGLYCDEHYDROG-RXN (reaction.ecocyc.PGLYCDEHYDROG-RXN), RXN-16701 (reaction.ecocyc.RXN-16701).

## Annotation

EcoCyc complex PGLYCDEHYDROG-CPLX

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.KETOGLUTREDUCT-RXN|reaction.ecocyc.KETOGLUTREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PGLYCDEHYDROG-RXN|reaction.ecocyc.PGLYCDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-16701|reaction.ecocyc.RXN-16701]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9T0|protein.P0A9T0]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:PGLYCDEHYDROG-CPLX`
- `QSPROTEOME:QS00181757`

## Notes

4*protein.P0A9T0
