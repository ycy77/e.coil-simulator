---
entity_id: "reaction.ecocyc.TRANS-RXN-30"
entity_type: "reaction"
name: "xylose:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-30"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# xylose:proton symport

`reaction.ecocyc.TRANS-RXN-30`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-30`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + D-Xylose -> PROTON + D-Xylose; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + D-Xylose -> PROTON + D-Xylose; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by xylE (protein.P0AGF4). Substrates: H+ (molecule.C00080), D-Xylose (molecule.C00181). Products: H+ (molecule.C00080), D-Xylose (molecule.C00181).

## Annotation

PROTON + D-Xylose -> PROTON + D-Xylose; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AGF4|protein.P0AGF4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00181|molecule.C00181]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00181|molecule.C00181]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-30`

## Notes

PROTON + D-Xylose -> PROTON + D-Xylose; direction=LEFT-TO-RIGHT
