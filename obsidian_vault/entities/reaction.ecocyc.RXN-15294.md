---
entity_id: "reaction.ecocyc.RXN-15294"
entity_type: "reaction"
name: "RXN-15294"
source_database: "EcoCyc"
source_id: "RXN-15294"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15294

`reaction.ecocyc.RXN-15294`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15294`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FE+2 + OXYGEN-MOLECULE + WATER -> CPD-16500 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FE+2 + OXYGEN-MOLECULE + WATER -> CPD-16500 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ferritin iron-storage complex (complex.ecocyc.CPLX0-3969). Substrates: H2O (molecule.C00001), Oxygen (molecule.C00007), Fe2+ (molecule.C14818). Products: H+ (molecule.C00080), [FeO(OH)] monomer (molecule.ecocyc.CPD-16500).

## Annotation

FE+2 + OXYGEN-MOLECULE + WATER -> CPD-16500 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3969|complex.ecocyc.CPLX0-3969]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-16500|molecule.ecocyc.CPD-16500]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-15294`

## Notes

FE+2 + OXYGEN-MOLECULE + WATER -> CPD-16500 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
