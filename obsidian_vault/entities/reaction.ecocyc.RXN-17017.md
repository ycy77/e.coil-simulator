---
entity_id: "reaction.ecocyc.RXN-17017"
entity_type: "reaction"
name: "RXN-17017"
source_database: "EcoCyc"
source_id: "RXN-17017"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17017

`reaction.ecocyc.RXN-17017`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17017`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Myristoyl-ACPs + GLYCEROL-3P -> CPD-18379 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Myristoyl-ACPs + GLYCEROL-3P -> CPD-18379 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by plsB (protein.P0A7A7). Substrates: sn-Glycerol 3-phosphate (molecule.C00093). Products: 1-myristoyl-sn-glycerol 3-phosphate (molecule.ecocyc.CPD-18379).

## Annotation

Myristoyl-ACPs + GLYCEROL-3P -> CPD-18379 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A7A7|protein.P0A7A7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-18379|molecule.ecocyc.CPD-18379]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17017`

## Notes

Myristoyl-ACPs + GLYCEROL-3P -> CPD-18379 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT
