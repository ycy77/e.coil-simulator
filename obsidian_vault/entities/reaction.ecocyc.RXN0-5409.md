---
entity_id: "reaction.ecocyc.RXN0-5409"
entity_type: "reaction"
name: "RXN0-5409"
source_database: "EcoCyc"
source_id: "RXN0-5409"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5409

`reaction.ecocyc.RXN0-5409`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5409`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-888 + WATER -> CPD0-1189 + FORMATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-888 + WATER -> CPD0-1189 + FORMATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by arnD (protein.P76472). Substrates: H2O (molecule.C00001), Undecaprenyl phosphate alpha-L-Ara4FN (molecule.C16156). Products: Formate (molecule.C00058), Undecaprenyl phosphate alpha-L-Ara4N (molecule.C16157).

## Enriched Pathways

- `ecocyc.PWY0-1338` polymyxin resistance (EcoCyc)

## Annotation

CPD0-888 + WATER -> CPD0-1189 + FORMATE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1338` polymyxin resistance (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P76472|protein.P76472]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C16157|molecule.C16157]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C16156|molecule.C16156]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5409`

## Notes

CPD0-888 + WATER -> CPD0-1189 + FORMATE; direction=LEFT-TO-RIGHT
