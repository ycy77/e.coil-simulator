---
entity_id: "reaction.ecocyc.TRANS-RXN-108I"
entity_type: "reaction"
name: "uridine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-108I"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# uridine:proton symport

`reaction.ecocyc.TRANS-RXN-108I`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-108I`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + URIDINE -> PROTON + URIDINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + URIDINE -> PROTON + URIDINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nupC (protein.P0AFF2), nupG (protein.P0AFF4). Substrates: H+ (molecule.C00080), Uridine (molecule.C00299). Products: H+ (molecule.C00080), Uridine (molecule.C00299).

## Annotation

PROTON + URIDINE -> PROTON + URIDINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFF4|protein.P0AFF4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00299|molecule.C00299]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00299|molecule.C00299]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-20899|molecule.ecocyc.CPD-20899]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-8179|molecule.ecocyc.CPD-8179]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-108I`

## Notes

PROTON + URIDINE -> PROTON + URIDINE; direction=LEFT-TO-RIGHT
