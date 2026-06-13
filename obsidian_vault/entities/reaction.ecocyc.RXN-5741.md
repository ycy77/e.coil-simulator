---
entity_id: "reaction.ecocyc.RXN-5741"
entity_type: "reaction"
name: "RXN-5741"
source_database: "EcoCyc"
source_id: "RXN-5741"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-5741

`reaction.ecocyc.RXN-5741`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-5741`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-195 + ACP + ATP -> Octanoyl-ACPs + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-195 + ACP + ATP -> Octanoyl-ACPs + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by aas (protein.P31119). Substrates: ATP (molecule.C00002), Octanoic acid (molecule.C06423). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

CPD-195 + ACP + ATP -> Octanoyl-ACPs + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P31119|protein.P31119]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06423|molecule.C06423]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-5741`

## Notes

CPD-195 + ACP + ATP -> Octanoyl-ACPs + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
