---
entity_id: "complex.ecocyc.MALIC-NADP-CPLX"
entity_type: "complex"
name: "malate dehydrogenase (oxaloacetate-decarboxylating) (NADP+)"
source_database: "EcoCyc"
source_id: "MALIC-NADP-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# malate dehydrogenase (oxaloacetate-decarboxylating) (NADP+)

`complex.ecocyc.MALIC-NADP-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:MALIC-NADP-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76558|protein.P76558]]

## Enriched Summary

EcoCyc complex MALIC-NADP-CPLX

## Biological Role

Catalyzes MALIC-NADP-RXN (reaction.ecocyc.MALIC-NADP-RXN), RXN-16819 (reaction.ecocyc.RXN-16819). Bound by Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

EcoCyc complex MALIC-NADP-CPLX

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.MALIC-NADP-RXN|reaction.ecocyc.MALIC-NADP-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-16819|reaction.ecocyc.RXN-16819]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P76558|protein.P76558]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## External IDs

- `EcoCyc:MALIC-NADP-CPLX`

## Notes

8*protein.P76558
