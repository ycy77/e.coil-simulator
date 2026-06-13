---
entity_id: "reaction.ecocyc.TRANS-RXN-475"
entity_type: "reaction"
name: "deoxyguanosine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-475"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# deoxyguanosine:proton symport

`reaction.ecocyc.TRANS-RXN-475`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-475`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

DEOXYGUANOSINE + PROTON -> DEOXYGUANOSINE + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: DEOXYGUANOSINE + PROTON -> DEOXYGUANOSINE + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nupG (protein.P0AFF4). Substrates: H+ (molecule.C00080), Deoxyguanosine (molecule.C00330). Products: H+ (molecule.C00080), Deoxyguanosine (molecule.C00330).

## Annotation

DEOXYGUANOSINE + PROTON -> DEOXYGUANOSINE + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AFF4|protein.P0AFF4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00330|molecule.C00330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00330|molecule.C00330]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-475`

## Notes

DEOXYGUANOSINE + PROTON -> DEOXYGUANOSINE + PROTON; direction=LEFT-TO-RIGHT
