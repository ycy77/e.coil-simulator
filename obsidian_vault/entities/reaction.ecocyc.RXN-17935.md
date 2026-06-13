---
entity_id: "reaction.ecocyc.RXN-17935"
entity_type: "reaction"
name: "RXN-17935"
source_database: "EcoCyc"
source_id: "RXN-17935"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17935

`reaction.ecocyc.RXN-17935`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17935`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GTP + RNA-Ligase-L-histidine -> RNA-Ligase-L-histidine-guanylate + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GTP + RNA-Ligase-L-histidine -> RNA-Ligase-L-histidine-guanylate + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: GTP (molecule.C00044), an [RNA ligase]-L-histidine (molecule.ecocyc.RNA-Ligase-L-histidine). Products: Diphosphate (molecule.C00013), an [RNA ligase]-Nτ-(5'-guanosyl-phosphono)-L-histidine (molecule.ecocyc.RNA-Ligase-L-histidine-guanylate).

## Annotation

GTP + RNA-Ligase-L-histidine -> RNA-Ligase-L-histidine-guanylate + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.RNA-Ligase-L-histidine-guanylate|molecule.ecocyc.RNA-Ligase-L-histidine-guanylate]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.RNA-Ligase-L-histidine|molecule.ecocyc.RNA-Ligase-L-histidine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17935`

## Notes

GTP + RNA-Ligase-L-histidine -> RNA-Ligase-L-histidine-guanylate + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
