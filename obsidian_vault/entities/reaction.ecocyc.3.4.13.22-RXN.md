---
entity_id: "reaction.ecocyc.3.4.13.22-RXN"
entity_type: "reaction"
name: "3.4.13.22-RXN"
source_database: "EcoCyc"
source_id: "3.4.13.22-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.4.13.22-RXN

`reaction.ecocyc.3.4.13.22-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.4.13.22-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-ALA-D-ALA + WATER -> D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-ALA-D-ALA + WATER -> D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ddpX (protein.P77790). Substrates: H2O (molecule.C00001), D-Alanyl-D-alanine (molecule.C00993). Products: D-Alanine (molecule.C00133).

## Annotation

D-ALA-D-ALA + WATER -> D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P77790|protein.P77790]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00993|molecule.C00993]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.4.13.22-RXN`

## Notes

D-ALA-D-ALA + WATER -> D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT
