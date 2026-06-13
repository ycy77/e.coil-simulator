---
entity_id: "complex.ecocyc.GABATRANSAM-CPLX"
entity_type: "complex"
name: "4-aminobutyrate aminotransferase GabT"
source_database: "EcoCyc"
source_id: "GABATRANSAM-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 4-aminobutyrate aminotransferase GabT

`complex.ecocyc.GABATRANSAM-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GABATRANSAM-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P22256|protein.P22256]]

## Enriched Summary

EcoCyc complex GABATRANSAM-CPLX

## Biological Role

Catalyzes ACETYLORNTRANSAM-RXN (reaction.ecocyc.ACETYLORNTRANSAM-RXN), GABATRANSAM-RXN (reaction.ecocyc.GABATRANSAM-RXN), VAGL-RXN (reaction.ecocyc.VAGL-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex GABATRANSAM-CPLX

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ACETYLORNTRANSAM-RXN|reaction.ecocyc.ACETYLORNTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GABATRANSAM-RXN|reaction.ecocyc.GABATRANSAM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.VAGL-RXN|reaction.ecocyc.VAGL-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P22256|protein.P22256]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GABATRANSAM-CPLX`
- `QSPROTEOME:QS00049713`

## Notes

2*protein.P22256
