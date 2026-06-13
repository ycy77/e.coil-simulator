---
entity_id: "reaction.ecocyc.RXN0-6427"
entity_type: "reaction"
name: "RXN0-6427"
source_database: "EcoCyc"
source_id: "RXN0-6427"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6427

`reaction.ecocyc.RXN0-6427`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6427`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GDP-TP + WATER -> GTP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GDP-TP + WATER -> GTP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by spoT (protein.P0AG24). Substrates: H2O (molecule.C00001), Guanosine 3'-diphosphate 5'-triphosphate (molecule.C04494). Products: Diphosphate (molecule.C00013), GTP (molecule.C00044).

## Enriched Pathways

- `ecocyc.PPGPPMET-PWY` ppGpp metabolism (EcoCyc)

## Annotation

GDP-TP + WATER -> GTP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PPGPPMET-PWY` ppGpp metabolism (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `activates` <-- [[protein.P0AFX4|protein.P0AFX4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P0AG24|protein.P0AG24]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04494|molecule.C04494]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6427`

## Notes

GDP-TP + WATER -> GTP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
