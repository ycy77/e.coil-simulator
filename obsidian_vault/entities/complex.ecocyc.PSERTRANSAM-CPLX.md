---
entity_id: "complex.ecocyc.PSERTRANSAM-CPLX"
entity_type: "complex"
name: "phosphoserine/phosphohydroxythreonine aminotransferase"
source_database: "EcoCyc"
source_id: "PSERTRANSAM-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# phosphoserine/phosphohydroxythreonine aminotransferase

`complex.ecocyc.PSERTRANSAM-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PSERTRANSAM-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P23721|protein.P23721]]

## Enriched Summary

EcoCyc complex PSERTRANSAM-CPLX

## Biological Role

Catalyzes PSERTRANSAM-RXN (reaction.ecocyc.PSERTRANSAM-RXN), PSERTRANSAMPYR-RXN (reaction.ecocyc.PSERTRANSAMPYR-RXN), SUCCINYLDIAMINOPIMTRANS-RXN (reaction.ecocyc.SUCCINYLDIAMINOPIMTRANS-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

EcoCyc complex PSERTRANSAM-CPLX

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.PSERTRANSAM-RXN|reaction.ecocyc.PSERTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PSERTRANSAMPYR-RXN|reaction.ecocyc.PSERTRANSAMPYR-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.SUCCINYLDIAMINOPIMTRANS-RXN|reaction.ecocyc.SUCCINYLDIAMINOPIMTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P23721|protein.P23721]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PSERTRANSAM-CPLX`
- `QSPROTEOME:QS00199083`

## Notes

2*protein.P23721
