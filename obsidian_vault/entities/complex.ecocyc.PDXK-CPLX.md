---
entity_id: "complex.ecocyc.PDXK-CPLX"
entity_type: "complex"
name: "pyridoxal kinase 1 / hydroxymethylpyrimidine kinase"
source_database: "EcoCyc"
source_id: "PDXK-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "pyridoxal kinase I"
---

# pyridoxal kinase 1 / hydroxymethylpyrimidine kinase

`complex.ecocyc.PDXK-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PDXK-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P40191|protein.P40191]]

## Enriched Summary

EcoCyc complex PDXK-CPLX

## Biological Role

Catalyzes OHMETPYRKIN-RXN (reaction.ecocyc.OHMETPYRKIN-RXN), PNKIN-RXN (reaction.ecocyc.PNKIN-RXN), PYRAMKIN-RXN (reaction.ecocyc.PYRAMKIN-RXN), PYRIDOXKIN-RXN (reaction.ecocyc.PYRIDOXKIN-RXN), RXN0-7436 (reaction.ecocyc.RXN0-7436). Bound by Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex PDXK-CPLX

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.OHMETPYRKIN-RXN|reaction.ecocyc.OHMETPYRKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PNKIN-RXN|reaction.ecocyc.PNKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PYRAMKIN-RXN|reaction.ecocyc.PYRAMKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PYRIDOXKIN-RXN|reaction.ecocyc.PYRIDOXKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7436|reaction.ecocyc.RXN0-7436]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P40191|protein.P40191]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PDXK-CPLX`
- `QSPROTEOME:QS00049516`

## Notes

2*protein.P40191
