---
entity_id: "reaction.ecocyc.RXN-22643"
entity_type: "reaction"
name: "RXN-22643"
source_database: "EcoCyc"
source_id: "RXN-22643"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22643

`reaction.ecocyc.RXN-22643`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22643`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLUTATHIONE + FUM -> CPD-24871; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLUTATHIONE + FUM -> CPD-24871; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Glutathione (molecule.C00051), Fumarate (molecule.C00122). Products: S-(2-succinyl)-glutathione (molecule.ecocyc.CPD-24871).

## Annotation

GLUTATHIONE + FUM -> CPD-24871; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.CPD-24871|molecule.ecocyc.CPD-24871]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22643`

## Notes

GLUTATHIONE + FUM -> CPD-24871; direction=PHYSIOL-LEFT-TO-RIGHT
