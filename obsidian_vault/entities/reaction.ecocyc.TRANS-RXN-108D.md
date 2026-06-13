---
entity_id: "reaction.ecocyc.TRANS-RXN-108D"
entity_type: "reaction"
name: "deoxycytidine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-108D"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# deoxycytidine:proton symport

`reaction.ecocyc.TRANS-RXN-108D`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-108D`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + DEOXYCYTIDINE -> PROTON + DEOXYCYTIDINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + DEOXYCYTIDINE -> PROTON + DEOXYCYTIDINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nupC (protein.P0AFF2), nupG (protein.P0AFF4). Substrates: H+ (molecule.C00080), Deoxycytidine (molecule.C00881). Products: H+ (molecule.C00080), Deoxycytidine (molecule.C00881).

## Annotation

PROTON + DEOXYCYTIDINE -> PROTON + DEOXYCYTIDINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFF4|protein.P0AFF4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00881|molecule.C00881]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00881|molecule.C00881]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-19916|molecule.ecocyc.CPD-19916]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-108D`

## Notes

PROTON + DEOXYCYTIDINE -> PROTON + DEOXYCYTIDINE; direction=LEFT-TO-RIGHT
