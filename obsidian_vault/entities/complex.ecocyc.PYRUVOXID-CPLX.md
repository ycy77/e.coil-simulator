---
entity_id: "complex.ecocyc.PYRUVOXID-CPLX"
entity_type: "complex"
name: "pyruvate oxidase"
source_database: "EcoCyc"
source_id: "PYRUVOXID-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "pyruvate:ubiquinone oxidoreductase"
  - "pyruvate dehydrogenase (quinone)"
---

# pyruvate oxidase

`complex.ecocyc.PYRUVOXID-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PYRUVOXID-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07003|protein.P07003]]

## Enriched Summary

EcoCyc complex PYRUVOXID-CPLX

## Biological Role

Catalyzes RXN-11496 (reaction.ecocyc.RXN-11496), RXN0-2022 (reaction.ecocyc.RXN0-2022). Bound by FAD (molecule.C00016), Thiamin diphosphate (molecule.C00068), Magnesium cation (molecule.C00305).

## Annotation

EcoCyc complex PYRUVOXID-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-11496|reaction.ecocyc.RXN-11496]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-2022|reaction.ecocyc.RXN0-2022]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P07003|protein.P07003]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:PYRUVOXID-CPLX`
- `QSPROTEOME:QS00197371`

## Notes

4*protein.P07003
