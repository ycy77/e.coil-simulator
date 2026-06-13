---
entity_id: "reaction.ecocyc.RXN-22914"
entity_type: "reaction"
name: "RXN-22914"
source_database: "EcoCyc"
source_id: "RXN-22914"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22914

`reaction.ecocyc.RXN-22914`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22914`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

4-P-PANTOTHENATE + CTP + PROTON -> CPD-25382 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 4-P-PANTOTHENATE + CTP + PROTON -> CPD-25382 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: CTP (molecule.C00063), H+ (molecule.C00080), D-4'-Phosphopantothenate (molecule.C03492). Products: Diphosphate (molecule.C00013), (R)-4'-phosphopantothenoyl-cytidylate (molecule.ecocyc.CPD-25382).

## Annotation

4-P-PANTOTHENATE + CTP + PROTON -> CPD-25382 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-25382|molecule.ecocyc.CPD-25382]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03492|molecule.C03492]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22914`

## Notes

4-P-PANTOTHENATE + CTP + PROTON -> CPD-25382 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
