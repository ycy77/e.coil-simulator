---
entity_id: "reaction.ecocyc.SUCCGLUDESUCC-RXN"
entity_type: "reaction"
name: "SUCCGLUDESUCC-RXN"
source_database: "EcoCyc"
source_id: "SUCCGLUDESUCC-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SUCCGLUDESUCC-RXN

`reaction.ecocyc.SUCCGLUDESUCC-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SUCCGLUDESUCC-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N2-SUCCINYLGLUTAMATE + WATER -> SUC + GLT; direction=LEFT-TO-RIGHT EcoCyc reaction equation: N2-SUCCINYLGLUTAMATE + WATER -> SUC + GLT; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by astE (protein.P76215). Substrates: H2O (molecule.C00001), N-Succinyl-L-glutamate (molecule.C05931). Products: L-Glutamate (molecule.C00025), Succinate (molecule.C00042).

## Enriched Pathways

- `ecocyc.AST-PWY` L-arginine degradation II (AST pathway) (EcoCyc)

## Annotation

N2-SUCCINYLGLUTAMATE + WATER -> SUC + GLT; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.AST-PWY` L-arginine degradation II (AST pathway) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P76215|protein.P76215]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05931|molecule.C05931]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:SUCCGLUDESUCC-RXN`

## Notes

N2-SUCCINYLGLUTAMATE + WATER -> SUC + GLT; direction=LEFT-TO-RIGHT
