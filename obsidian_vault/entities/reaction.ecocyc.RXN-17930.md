---
entity_id: "reaction.ecocyc.RXN-17930"
entity_type: "reaction"
name: "RXN-17930"
source_database: "EcoCyc"
source_id: "RXN-17930"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17930

`reaction.ecocyc.RXN-17930`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17930`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + RNA-3-prime-P-cyclase-L-histidine -> RNA-3-prime-P-cyclase-L-His-adenylate + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + RNA-3-prime-P-cyclase-L-histidine -> RNA-3-prime-P-cyclase-L-His-adenylate + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), an [RNA 3'-phosphate cyclase]-L-histidine (molecule.ecocyc.RNA-3-prime-P-cyclase-L-histidine). Products: Diphosphate (molecule.C00013), an [RNA 3'-phosphate cyclase]-Nτ-(5'-adenylyl)-L-histidine (molecule.ecocyc.RNA-3-prime-P-cyclase-L-His-adenylate).

## Annotation

ATP + RNA-3-prime-P-cyclase-L-histidine -> RNA-3-prime-P-cyclase-L-His-adenylate + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.RNA-3-prime-P-cyclase-L-His-adenylate|molecule.ecocyc.RNA-3-prime-P-cyclase-L-His-adenylate]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.RNA-3-prime-P-cyclase-L-histidine|molecule.ecocyc.RNA-3-prime-P-cyclase-L-histidine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17930`

## Notes

ATP + RNA-3-prime-P-cyclase-L-histidine -> RNA-3-prime-P-cyclase-L-His-adenylate + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
