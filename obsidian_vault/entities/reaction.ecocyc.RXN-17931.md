---
entity_id: "reaction.ecocyc.RXN-17931"
entity_type: "reaction"
name: "RXN-17931"
source_database: "EcoCyc"
source_id: "RXN-17931"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17931

`reaction.ecocyc.RXN-17931`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17931`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RNA-3-prime-P-cyclase-L-His-adenylate + 3-Prime-Phosphate-Terminated-RNAs + PROTON -> RNA-with-3-prime-pp-5-prime-A-cap + RNA-3-prime-P-cyclase-L-histidine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: RNA-3-prime-P-cyclase-L-His-adenylate + 3-Prime-Phosphate-Terminated-RNAs + PROTON -> RNA-with-3-prime-pp-5-prime-A-cap + RNA-3-prime-P-cyclase-L-histidine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), an [RNA 3'-phosphate cyclase]-Nτ-(5'-adenylyl)-L-histidine (molecule.ecocyc.RNA-3-prime-P-cyclase-L-His-adenylate). Products: an [RNA 3'-phosphate cyclase]-L-histidine (molecule.ecocyc.RNA-3-prime-P-cyclase-L-histidine).

## Annotation

RNA-3-prime-P-cyclase-L-His-adenylate + 3-Prime-Phosphate-Terminated-RNAs + PROTON -> RNA-with-3-prime-pp-5-prime-A-cap + RNA-3-prime-P-cyclase-L-histidine; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.RNA-3-prime-P-cyclase-L-histidine|molecule.ecocyc.RNA-3-prime-P-cyclase-L-histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.RNA-3-prime-P-cyclase-L-His-adenylate|molecule.ecocyc.RNA-3-prime-P-cyclase-L-His-adenylate]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17931`

## Notes

RNA-3-prime-P-cyclase-L-His-adenylate + 3-Prime-Phosphate-Terminated-RNAs + PROTON -> RNA-with-3-prime-pp-5-prime-A-cap + RNA-3-prime-P-cyclase-L-histidine; direction=PHYSIOL-LEFT-TO-RIGHT
