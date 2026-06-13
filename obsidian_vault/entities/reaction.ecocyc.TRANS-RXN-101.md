---
entity_id: "reaction.ecocyc.TRANS-RXN-101"
entity_type: "reaction"
name: "sodium:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-101"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# sodium:proton antiport

`reaction.ecocyc.TRANS-RXN-101`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-101`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NA+ + PROTON -> PROTON + NA+; direction=LEFT-TO-RIGHT EcoCyc reaction equation: NA+ + PROTON -> PROTON + NA+; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mdfA (protein.P0AEY8), chaA (protein.P31801). Substrates: H+ (molecule.C00080), Sodium cation (molecule.C01330). Products: H+ (molecule.C00080), Sodium cation (molecule.C01330).

## Annotation

NA+ + PROTON -> PROTON + NA+; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AEY8|protein.P0AEY8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P31801|protein.P31801]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-101`

## Notes

NA+ + PROTON -> PROTON + NA+; direction=LEFT-TO-RIGHT
