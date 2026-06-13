---
entity_id: "reaction.ecocyc.RXN-15341"
entity_type: "reaction"
name: "RXN-15341"
source_database: "EcoCyc"
source_id: "RXN-15341"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15341

`reaction.ecocyc.RXN-15341`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15341`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1958 + FMNH2 + OXYGEN-MOLECULE -> CPD-16549 + SO3 + WATER + FMN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1958 + FMNH2 + OXYGEN-MOLECULE -> CPD-16549 + SO3 + WATER + FMN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Oxygen (molecule.C00007), Reduced FMN (molecule.C01847), 3-(N-morpholino)propanesulfonate (molecule.ecocyc.CPD0-1958). Products: H2O (molecule.C00001), FMN (molecule.C00061), H+ (molecule.C00080), Sulfite (molecule.C00094), 3-(N-morpholino)propanal (molecule.ecocyc.CPD-16549).

## Annotation

CPD0-1958 + FMNH2 + OXYGEN-MOLECULE -> CPD-16549 + SO3 + WATER + FMN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-16549|molecule.ecocyc.CPD-16549]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01847|molecule.C01847]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1958|molecule.ecocyc.CPD0-1958]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15341`

## Notes

CPD0-1958 + FMNH2 + OXYGEN-MOLECULE -> CPD-16549 + SO3 + WATER + FMN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
