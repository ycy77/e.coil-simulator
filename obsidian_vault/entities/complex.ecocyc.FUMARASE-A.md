---
entity_id: "complex.ecocyc.FUMARASE-A"
entity_type: "complex"
name: "fumarase A"
source_database: "EcoCyc"
source_id: "FUMARASE-A"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# fumarase A

`complex.ecocyc.FUMARASE-A`

## Static

- Type: `complex`
- Source: `EcoCyc:FUMARASE-A`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AC33|protein.P0AC33]]

## Enriched Summary

EcoCyc complex FUMARASE-A

## Biological Role

Catalyzes FUMHYDR-RXN (reaction.ecocyc.FUMHYDR-RXN), OXALOACETATE-TAUTOMERASE-RXN (reaction.ecocyc.OXALOACETATE-TAUTOMERASE-RXN). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

EcoCyc complex FUMARASE-A

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.FUMHYDR-RXN|reaction.ecocyc.FUMHYDR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.OXALOACETATE-TAUTOMERASE-RXN|reaction.ecocyc.OXALOACETATE-TAUTOMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AC33|protein.P0AC33]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:FUMARASE-A`
- `QSPROTEOME:QS00049708`

## Notes

2*protein.P0AC33
