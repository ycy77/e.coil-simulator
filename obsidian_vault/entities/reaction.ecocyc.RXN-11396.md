---
entity_id: "reaction.ecocyc.RXN-11396"
entity_type: "reaction"
name: "RXN-11396"
source_database: "EcoCyc"
source_id: "RXN-11396"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11396

`reaction.ecocyc.RXN-11396`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11396`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

8-Oxo-dGTP + WATER -> PROTON + CPD-12365 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 8-Oxo-dGTP + WATER -> PROTON + CPD-12365 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mutT (protein.P08337). Substrates: H2O (molecule.C00001), 8-oxo-dGTP (molecule.ecocyc.8-Oxo-dGTP). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), 8-oxo-dGMP (molecule.ecocyc.CPD-12365).

## Annotation

8-Oxo-dGTP + WATER -> PROTON + CPD-12365 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P08337|protein.P08337]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-12365|molecule.ecocyc.CPD-12365]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.8-Oxo-dGTP|molecule.ecocyc.8-Oxo-dGTP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11396`

## Notes

8-Oxo-dGTP + WATER -> PROTON + CPD-12365 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
