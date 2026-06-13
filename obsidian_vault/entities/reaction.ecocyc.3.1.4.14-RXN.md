---
entity_id: "reaction.ecocyc.3.1.4.14-RXN"
entity_type: "reaction"
name: "3.1.4.14-RXN"
source_database: "EcoCyc"
source_id: "3.1.4.14-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.1.4.14-RXN

`reaction.ecocyc.3.1.4.14-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.1.4.14-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

All-holo-ACPs + WATER -> PANTETHEINE-P + All-apo-ACPs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: All-holo-ACPs + WATER -> PANTETHEINE-P + All-apo-ACPs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by acpH (protein.P21515). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), Pantetheine 4'-phosphate (molecule.C01134).

## Enriched Pathways

- `ecocyc.PWY-6012` acyl carrier protein metabolism (EcoCyc)

## Annotation

All-holo-ACPs + WATER -> PANTETHEINE-P + All-apo-ACPs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6012` acyl carrier protein metabolism (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P21515|protein.P21515]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01134|molecule.C01134]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.1.4.14-RXN`

## Notes

All-holo-ACPs + WATER -> PANTETHEINE-P + All-apo-ACPs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
