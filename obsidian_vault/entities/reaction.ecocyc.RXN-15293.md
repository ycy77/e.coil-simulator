---
entity_id: "reaction.ecocyc.RXN-15293"
entity_type: "reaction"
name: "RXN-15293"
source_database: "EcoCyc"
source_id: "RXN-15293"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15293

`reaction.ecocyc.RXN-15293`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15293`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FE+2 + HYDROGEN-PEROXIDE + WATER -> CPD-16500 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FE+2 + HYDROGEN-PEROXIDE + WATER -> CPD-16500 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), Hydrogen peroxide (molecule.C00027), Fe2+ (molecule.C14818). Products: H+ (molecule.C00080), [FeO(OH)] monomer (molecule.ecocyc.CPD-16500).

## Annotation

FE+2 + HYDROGEN-PEROXIDE + WATER -> CPD-16500 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-16500|molecule.ecocyc.CPD-16500]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15293`

## Notes

FE+2 + HYDROGEN-PEROXIDE + WATER -> CPD-16500 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
