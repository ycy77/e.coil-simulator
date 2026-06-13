---
entity_id: "complex.ecocyc.CPLX0-7667"
entity_type: "complex"
name: "NADPH-dependent aldehyde reductase YqhD"
source_database: "EcoCyc"
source_id: "CPLX0-7667"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# NADPH-dependent aldehyde reductase YqhD

`complex.ecocyc.CPLX0-7667`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7667`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.Q46856|protein.Q46856]]

## Enriched Summary

EcoCyc complex CPLX0-7667

## Biological Role

Catalyzes ALCOHOL-DEHYDROGENASE-NADPORNOP+-RXN (reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN), RXN-14023 (reaction.ecocyc.RXN-14023), RXN0-4281 (reaction.ecocyc.RXN0-4281), RXN0-6487 (reaction.ecocyc.RXN0-6487), RXN0-7154 (reaction.ecocyc.RXN0-7154). Bound by Zinc cation (molecule.C00038).

## Annotation

EcoCyc complex CPLX0-7667

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN|reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14023|reaction.ecocyc.RXN-14023]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-4281|reaction.ecocyc.RXN0-4281]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6487|reaction.ecocyc.RXN0-6487]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7154|reaction.ecocyc.RXN0-7154]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.Q46856|protein.Q46856]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7667`
- `QSPROTEOME:QS00180865`

## Notes

2*protein.Q46856
