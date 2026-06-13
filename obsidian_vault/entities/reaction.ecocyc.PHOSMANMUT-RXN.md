---
entity_id: "reaction.ecocyc.PHOSMANMUT-RXN"
entity_type: "reaction"
name: "PHOSMANMUT-RXN"
source_database: "EcoCyc"
source_id: "PHOSMANMUT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PHOSMANMUT-RXN

`reaction.ecocyc.PHOSMANMUT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHOSMANMUT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in the synthesis of GDP-mannose. EcoCyc reaction equation: MANNOSE-1P -> CPD-15979; direction=REVERSIBLE. This is the second reaction in the synthesis of GDP-mannose.

## Biological Role

Catalyzed by manB (protein.P24175). Substrates: D-Mannose 1-phosphate (molecule.C00636). Products: D-mannopyranose 6-phosphate (molecule.ecocyc.CPD-15979).

## Enriched Pathways

- `ecocyc.PWY-5659` GDP-mannose biosynthesis (EcoCyc)

## Annotation

This is the second reaction in the synthesis of GDP-mannose.

## Pathways

- `ecocyc.PWY-5659` GDP-mannose biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P24175|protein.P24175]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-15979|molecule.ecocyc.CPD-15979]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00636|molecule.C00636]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PHOSMANMUT-RXN`

## Notes

MANNOSE-1P -> CPD-15979; direction=REVERSIBLE
