---
entity_id: "complex.ecocyc.FUMARASE-B"
entity_type: "complex"
name: "fumarase B"
source_database: "EcoCyc"
source_id: "FUMARASE-B"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# fumarase B

`complex.ecocyc.FUMARASE-B`

## Static

- Type: `complex`
- Source: `EcoCyc:FUMARASE-B`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P14407|protein.P14407]]

## Enriched Summary

EcoCyc complex FUMARASE-B

## Biological Role

Catalyzes D--TARTRATE-DEHYDRATASE-RXN (reaction.ecocyc.D--TARTRATE-DEHYDRATASE-RXN), FUMHYDR-RXN (reaction.ecocyc.FUMHYDR-RXN). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

EcoCyc complex FUMARASE-B

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.D--TARTRATE-DEHYDRATASE-RXN|reaction.ecocyc.D--TARTRATE-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.FUMHYDR-RXN|reaction.ecocyc.FUMHYDR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P14407|protein.P14407]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:FUMARASE-B`
- `QSPROTEOME:QS00049709`

## Notes

2*protein.P14407
