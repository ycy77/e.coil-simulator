---
entity_id: "complex.ecocyc.GLUTDECARBOXB-CPLX"
entity_type: "complex"
name: "glutamate decarboxylase B"
source_database: "EcoCyc"
source_id: "GLUTDECARBOXB-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glutamate decarboxylase B

`complex.ecocyc.GLUTDECARBOXB-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLUTDECARBOXB-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P69910|protein.P69910]]

## Enriched Summary

EcoCyc complex GLUTDECARBOXB-CPLX

## Biological Role

Catalyzes GLUTDECARBOX-RXN (reaction.ecocyc.GLUTDECARBOX-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex GLUTDECARBOXB-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUTDECARBOX-RXN|reaction.ecocyc.GLUTDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P69910|protein.P69910]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:GLUTDECARBOXB-CPLX`
- `QSPROTEOME:QS00181683`
- `PDB:1PMM`
- `PDB:2DGK`
- `PDB:2DGL`
- `PDB:2DGM`

## Notes

6*protein.P69910
