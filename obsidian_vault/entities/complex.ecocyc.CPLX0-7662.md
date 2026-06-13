---
entity_id: "complex.ecocyc.CPLX0-7662"
entity_type: "complex"
name: "β-D-glucuronidase"
source_database: "EcoCyc"
source_id: "CPLX0-7662"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# β-D-glucuronidase

`complex.ecocyc.CPLX0-7662`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7662`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P05804|protein.P05804]]

## Enriched Summary

EcoCyc complex CPLX0-7662

## Biological Role

Catalyzes BETA-GLUCURONID-RXN (reaction.ecocyc.BETA-GLUCURONID-RXN), RXN-13605 (reaction.ecocyc.RXN-13605), RXN-25221 (reaction.ecocyc.RXN-25221).

## Annotation

EcoCyc complex CPLX0-7662

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.BETA-GLUCURONID-RXN|reaction.ecocyc.BETA-GLUCURONID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-13605|reaction.ecocyc.RXN-13605]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-25221|reaction.ecocyc.RXN-25221]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P05804|protein.P05804]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7662`
- `QSPROTEOME:QS00183221`

## Notes

4*protein.P05804
