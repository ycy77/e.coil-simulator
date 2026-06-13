---
entity_id: "complex.ecocyc.CPLX0-255"
entity_type: "complex"
name: "phenylhydantoinase"
source_database: "EcoCyc"
source_id: "CPLX0-255"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# phenylhydantoinase

`complex.ecocyc.CPLX0-255`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-255`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.Q46806|protein.Q46806]]

## Enriched Summary

EcoCyc complex CPLX0-255

## Biological Role

Catalyzes RXN0-275 (reaction.ecocyc.RXN0-275). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex CPLX0-255

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-275|reaction.ecocyc.RXN0-275]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.Q46806|protein.Q46806]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-255`
- `QSPROTEOME:QS00181797`

## Notes

4*protein.Q46806
