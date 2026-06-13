---
entity_id: "reaction.ecocyc.RXN-17936"
entity_type: "reaction"
name: "RXN-17936"
source_database: "EcoCyc"
source_id: "RXN-17936"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17936

`reaction.ecocyc.RXN-17936`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17936`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

RNA-Ligase-L-histidine-guanylate + 3-Prime-Phosphate-Terminated-RNAs + PROTON -> RNA-with-3-prime-pp-5-prime-G-cap + RNA-Ligase-L-histidine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: RNA-Ligase-L-histidine-guanylate + 3-Prime-Phosphate-Terminated-RNAs + PROTON -> RNA-with-3-prime-pp-5-prime-G-cap + RNA-Ligase-L-histidine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), an [RNA ligase]-Nτ-(5'-guanosyl-phosphono)-L-histidine (molecule.ecocyc.RNA-Ligase-L-histidine-guanylate). Products: an [RNA ligase]-L-histidine (molecule.ecocyc.RNA-Ligase-L-histidine).

## Annotation

RNA-Ligase-L-histidine-guanylate + 3-Prime-Phosphate-Terminated-RNAs + PROTON -> RNA-with-3-prime-pp-5-prime-G-cap + RNA-Ligase-L-histidine; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.RNA-Ligase-L-histidine|molecule.ecocyc.RNA-Ligase-L-histidine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.RNA-Ligase-L-histidine-guanylate|molecule.ecocyc.RNA-Ligase-L-histidine-guanylate]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17936`

## Notes

RNA-Ligase-L-histidine-guanylate + 3-Prime-Phosphate-Terminated-RNAs + PROTON -> RNA-with-3-prime-pp-5-prime-G-cap + RNA-Ligase-L-histidine; direction=PHYSIOL-LEFT-TO-RIGHT
