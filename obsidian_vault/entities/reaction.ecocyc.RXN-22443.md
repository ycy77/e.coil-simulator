---
entity_id: "reaction.ecocyc.RXN-22443"
entity_type: "reaction"
name: "RXN-22443"
source_database: "EcoCyc"
source_id: "RXN-22443"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22443

`reaction.ecocyc.RXN-22443`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22443`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FMNH2 + OXYGEN-MOLECULE -> CPD-24463 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FMNH2 + OXYGEN-MOLECULE -> CPD-24463 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Oxygen (molecule.C00007), Reduced FMN (molecule.C01847). Products: H+ (molecule.C00080), FMN-N5-peroxide (molecule.ecocyc.CPD-24463).

## Annotation

FMNH2 + OXYGEN-MOLECULE -> CPD-24463 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-24463|molecule.ecocyc.CPD-24463]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01847|molecule.C01847]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22443`

## Notes

FMNH2 + OXYGEN-MOLECULE -> CPD-24463 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
