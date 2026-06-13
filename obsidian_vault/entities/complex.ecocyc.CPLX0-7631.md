---
entity_id: "complex.ecocyc.CPLX0-7631"
entity_type: "complex"
name: "L-fucose isomerase"
source_database: "EcoCyc"
source_id: "CPLX0-7631"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# L-fucose isomerase

`complex.ecocyc.CPLX0-7631`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7631`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P69922|protein.P69922]]

## Enriched Summary

EcoCyc complex CPLX0-7631

## Biological Role

Catalyzes DARABISOM-RXN (reaction.ecocyc.DARABISOM-RXN), FUCISOM-RXN (reaction.ecocyc.FUCISOM-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex CPLX0-7631

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.DARABISOM-RXN|reaction.ecocyc.DARABISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.FUCISOM-RXN|reaction.ecocyc.FUCISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P69922|protein.P69922]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-7631`
- `QSPROTEOME:QS00192173`

## Notes

6*protein.P69922
