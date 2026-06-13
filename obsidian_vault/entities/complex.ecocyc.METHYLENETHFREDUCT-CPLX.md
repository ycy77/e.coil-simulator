---
entity_id: "complex.ecocyc.METHYLENETHFREDUCT-CPLX"
entity_type: "complex"
name: "5,10-methylenetetrahydrofolate reductase"
source_database: "EcoCyc"
source_id: "METHYLENETHFREDUCT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 5,10-methylenetetrahydrofolate reductase

`complex.ecocyc.METHYLENETHFREDUCT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:METHYLENETHFREDUCT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AEZ1|protein.P0AEZ1]]

## Enriched Summary

EcoCyc complex METHYLENETHFREDUCT-CPLX

## Biological Role

Catalyzes RXN-22438 (reaction.ecocyc.RXN-22438). Bound by FAD (molecule.C00016).

## Annotation

EcoCyc complex METHYLENETHFREDUCT-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-22438|reaction.ecocyc.RXN-22438]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AEZ1|protein.P0AEZ1]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:METHYLENETHFREDUCT-CPLX`
- `QSPROTEOME:QS00181837`

## Notes

4*protein.P0AEZ1
