---
entity_id: "reaction.ecocyc.RXN-17022"
entity_type: "reaction"
name: "RXN-17022"
source_database: "EcoCyc"
source_id: "RXN-17022"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17022

`reaction.ecocyc.RXN-17022`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17022`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Myristoyl-ACPs + CPD-18379 -> CPD0-1425 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Myristoyl-ACPs + CPD-18379 -> CPD0-1425 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by plsC (protein.P26647). Substrates: 1-myristoyl-sn-glycerol 3-phosphate (molecule.ecocyc.CPD-18379). Products: 1,2-dimyristoyl-sn-glycerol 3-phosphate (molecule.ecocyc.CPD0-1425).

## Annotation

Myristoyl-ACPs + CPD-18379 -> CPD0-1425 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P26647|protein.P26647]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1425|molecule.ecocyc.CPD0-1425]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-18379|molecule.ecocyc.CPD-18379]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17022`

## Notes

Myristoyl-ACPs + CPD-18379 -> CPD0-1425 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT
