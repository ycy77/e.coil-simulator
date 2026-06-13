---
entity_id: "reaction.ecocyc.RXN-16456"
entity_type: "reaction"
name: "RXN-16456"
source_database: "EcoCyc"
source_id: "RXN-16456"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16456

`reaction.ecocyc.RXN-16456`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16456`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15874 + GTP + PROTON -> CPD-15873 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-15874 + GTP + PROTON -> CPD-15873 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: GTP (molecule.C00044), H+ (molecule.C00080), bis(molybdenum cofactor) (molecule.ecocyc.CPD-15874). Products: Diphosphate (molecule.C00013), bis(guanylyl molybdopterin) cofactor (molecule.ecocyc.CPD-15873).

## Enriched Pathways

- `ecocyc.PWY-7639` bis(guanylyl molybdenum cofactor) biosynthesis (EcoCyc)

## Annotation

CPD-15874 + GTP + PROTON -> CPD-15873 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7639` bis(guanylyl molybdenum cofactor) biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15873|molecule.ecocyc.CPD-15873]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15874|molecule.ecocyc.CPD-15874]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16456`

## Notes

CPD-15874 + GTP + PROTON -> CPD-15873 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
