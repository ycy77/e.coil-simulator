---
entity_id: "reaction.ecocyc.RXN-21025"
entity_type: "reaction"
name: "RXN-21025"
source_database: "EcoCyc"
source_id: "RXN-21025"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21025

`reaction.ecocyc.RXN-21025`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21025`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Thiarsahydroxy-ArsC + GLUTATHIONE + PROTON -> Thiarsahydroxy-SG-ArsC + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Thiarsahydroxy-ArsC + GLUTATHIONE + PROTON -> Thiarsahydroxy-SG-ArsC + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Glutathione (molecule.C00051), H+ (molecule.C00080), thiarsahydroxy-[arsenate reductase] (molecule.ecocyc.Thiarsahydroxy-ArsC). Products: H2O (molecule.C00001), S-glutathionyl-thiarsahydroxy-[arsenate reductase] (molecule.ecocyc.Thiarsahydroxy-SG-ArsC).

## Annotation

Thiarsahydroxy-ArsC + GLUTATHIONE + PROTON -> Thiarsahydroxy-SG-ArsC + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Thiarsahydroxy-SG-ArsC|molecule.ecocyc.Thiarsahydroxy-SG-ArsC]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Thiarsahydroxy-ArsC|molecule.ecocyc.Thiarsahydroxy-ArsC]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21025`

## Notes

Thiarsahydroxy-ArsC + GLUTATHIONE + PROTON -> Thiarsahydroxy-SG-ArsC + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
