---
entity_id: "reaction.ecocyc.UDPSUGARHYDRO-RXN"
entity_type: "reaction"
name: "UDPSUGARHYDRO-RXN"
source_database: "EcoCyc"
source_id: "UDPSUGARHYDRO-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDPSUGARHYDRO-RXN

`reaction.ecocyc.UDPSUGARHYDRO-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UDPSUGARHYDRO-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

UDP-sugar + WATER -> UMP + Alpha-D-aldose-1-phosphates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: UDP-sugar + WATER -> UMP + Alpha-D-aldose-1-phosphates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ushA (protein.P07024). Substrates: H2O (molecule.C00001), a UDP-sugar (molecule.ecocyc.UDP-sugar). Products: H+ (molecule.C00080), UMP (molecule.C00105), an α-D-aldose 1-phosphate (molecule.ecocyc.Alpha-D-aldose-1-phosphates).

## Annotation

UDP-sugar + WATER -> UMP + Alpha-D-aldose-1-phosphates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `activates` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P07024|protein.P07024]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00105|molecule.C00105]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Alpha-D-aldose-1-phosphates|molecule.ecocyc.Alpha-D-aldose-1-phosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.UDP-sugar|molecule.ecocyc.UDP-sugar]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00394|molecule.C00394]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00498|molecule.C00498]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00501|molecule.C00501]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:UDPSUGARHYDRO-RXN`

## Notes

UDP-sugar + WATER -> UMP + Alpha-D-aldose-1-phosphates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
