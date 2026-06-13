---
entity_id: "complex.ecocyc.PEPCARBOX-CPLX"
entity_type: "complex"
name: "phosphoenolpyruvate carboxylase"
source_database: "EcoCyc"
source_id: "PEPCARBOX-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# phosphoenolpyruvate carboxylase

`complex.ecocyc.PEPCARBOX-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PEPCARBOX-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00864|protein.P00864]]

## Enriched Summary

EcoCyc complex PEPCARBOX-CPLX

## Biological Role

Catalyzes PEPCARBOX-RXN (reaction.ecocyc.PEPCARBOX-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex PEPCARBOX-CPLX

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PEPCARBOX-RXN|reaction.ecocyc.PEPCARBOX-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00864|protein.P00864]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:PEPCARBOX-CPLX`
- `QSPROTEOME:QS00196525`

## Notes

4*protein.P00864
