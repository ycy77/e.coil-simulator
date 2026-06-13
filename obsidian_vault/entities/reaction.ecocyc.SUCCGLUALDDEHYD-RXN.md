---
entity_id: "reaction.ecocyc.SUCCGLUALDDEHYD-RXN"
entity_type: "reaction"
name: "SUCCGLUALDDEHYD-RXN"
source_database: "EcoCyc"
source_id: "SUCCGLUALDDEHYD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SUCCGLUALDDEHYD-RXN

`reaction.ecocyc.SUCCGLUALDDEHYD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SUCCGLUALDDEHYD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-822 + NAD + WATER -> N2-SUCCINYLGLUTAMATE + NADH + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-822 + NAD + WATER -> N2-SUCCINYLGLUTAMATE + NADH + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by astD (protein.P76217). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), N-Succinyl-L-glutamate 5-semialdehyde (molecule.C05932). Products: NADH (molecule.C00004), H+ (molecule.C00080), N-Succinyl-L-glutamate (molecule.C05931).

## Enriched Pathways

- `ecocyc.AST-PWY` L-arginine degradation II (AST pathway) (EcoCyc)

## Annotation

CPD-822 + NAD + WATER -> N2-SUCCINYLGLUTAMATE + NADH + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.AST-PWY` L-arginine degradation II (AST pathway) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P76217|protein.P76217]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05931|molecule.C05931]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05932|molecule.C05932]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:SUCCGLUALDDEHYD-RXN`

## Notes

CPD-822 + NAD + WATER -> N2-SUCCINYLGLUTAMATE + NADH + PROTON; direction=LEFT-TO-RIGHT
