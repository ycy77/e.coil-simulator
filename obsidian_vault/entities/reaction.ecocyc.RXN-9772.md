---
entity_id: "reaction.ecocyc.RXN-9772"
entity_type: "reaction"
name: "L-aspartate : fumarate oxidoreductase (deaminating)"
source_database: "EcoCyc"
source_id: "RXN-9772"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-aspartate : fumarate oxidoreductase (deaminating)

`reaction.ecocyc.RXN-9772`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9772`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-ASPARTATE + FUM -> PROTON + IMINOASPARTATE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-ASPARTATE + FUM -> PROTON + IMINOASPARTATE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nadB (protein.P10902). Substrates: L-Aspartate (molecule.C00049), Fumarate (molecule.C00122). Products: Succinate (molecule.C00042), H+ (molecule.C00080), Iminoaspartate (molecule.C05840).

## Annotation

L-ASPARTATE + FUM -> PROTON + IMINOASPARTATE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P10902|protein.P10902]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05840|molecule.C05840]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9772`

## Notes

L-ASPARTATE + FUM -> PROTON + IMINOASPARTATE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT
