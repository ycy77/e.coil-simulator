---
entity_id: "complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX"
entity_type: "complex"
name: "anaerobic ribonucleoside-triphosphate reductase"
source_database: "EcoCyc"
source_id: "RIBONUCLEOSIDE-TRIP-REDUCT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# anaerobic ribonucleoside-triphosphate reductase

`complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:RIBONUCLEOSIDE-TRIP-REDUCT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P28903|protein.P28903]]

## Enriched Summary

EcoCyc complex RIBONUCLEOSIDE-TRIP-REDUCT-CPLX

## Biological Role

Catalyzes RIBONUCLEOSIDE-TRIP-REDUCT-RXN (reaction.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-RXN), RXN0-723 (reaction.ecocyc.RXN0-723), RXN0-724 (reaction.ecocyc.RXN0-724), RXN0-745 (reaction.ecocyc.RXN0-745), RXN0-746 (reaction.ecocyc.RXN0-746). Component of anaerobic nucleoside-triphosphate reductase activating system (complex.ecocyc.NRDACTMULTI-CPLX). Bound by Zinc cation (molecule.C00038), Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex RIBONUCLEOSIDE-TRIP-REDUCT-CPLX

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-RXN|reaction.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-723|reaction.ecocyc.RXN0-723]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-724|reaction.ecocyc.RXN0-724]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-745|reaction.ecocyc.RXN0-745]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-746|reaction.ecocyc.RXN0-746]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.NRDACTMULTI-CPLX|complex.ecocyc.NRDACTMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (4)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P28903|protein.P28903]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:RIBONUCLEOSIDE-TRIP-REDUCT-CPLX`
- `QSPROTEOME:QS00049548`

## Notes

2*protein.P28903
