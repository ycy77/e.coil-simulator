---
entity_id: "reaction.ecocyc.RXN0-4621"
entity_type: "reaction"
name: "RXN0-4621"
source_database: "EcoCyc"
source_id: "RXN0-4621"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4621

`reaction.ecocyc.RXN0-4621`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4621`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-882 + ATP + WATER -> PROTON + CPD0-881 + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-882 + ATP + WATER -> PROTON + CPD0-881 + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by anmK (protein.P77570). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), 1,6-Anhydro-N-acetyl-beta-muramate (molecule.C19769). Products: ADP (molecule.C00008), H+ (molecule.C00080), N-Acetylmuramic acid 6-phosphate (molecule.C16698).

## Enriched Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Annotation

CPD0-882 + ATP + WATER -> PROTON + CPD0-881 + ADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P77570|protein.P77570]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C16698|molecule.C16698]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C19769|molecule.C19769]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-4621`

## Notes

CPD0-882 + ATP + WATER -> PROTON + CPD0-881 + ADP; direction=LEFT-TO-RIGHT
