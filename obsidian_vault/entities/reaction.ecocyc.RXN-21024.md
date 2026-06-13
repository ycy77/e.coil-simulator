---
entity_id: "reaction.ecocyc.RXN-21024"
entity_type: "reaction"
name: "RXN-21024"
source_database: "EcoCyc"
source_id: "RXN-21024"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21024

`reaction.ecocyc.RXN-21024`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21024`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Arsenate-Reductase-Cysteines + ARSENATE + PROTON -> Thiarsahydroxy-ArsC + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Arsenate-Reductase-Cysteines + ARSENATE + PROTON -> Thiarsahydroxy-ArsC + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), arsenate (molecule.ecocyc.ARSENATE), an [arsenate reductase]-L-cysteine (molecule.ecocyc.Arsenate-Reductase-Cysteines). Products: H2O (molecule.C00001), thiarsahydroxy-[arsenate reductase] (molecule.ecocyc.Thiarsahydroxy-ArsC).

## Annotation

Arsenate-Reductase-Cysteines + ARSENATE + PROTON -> Thiarsahydroxy-ArsC + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Thiarsahydroxy-ArsC|molecule.ecocyc.Thiarsahydroxy-ArsC]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.ARSENATE|molecule.ecocyc.ARSENATE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Arsenate-Reductase-Cysteines|molecule.ecocyc.Arsenate-Reductase-Cysteines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21024`

## Notes

Arsenate-Reductase-Cysteines + ARSENATE + PROTON -> Thiarsahydroxy-ArsC + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
