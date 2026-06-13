---
entity_id: "reaction.ecocyc.TRANS-RXN-108H"
entity_type: "reaction"
name: "thymidine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-108H"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# thymidine:proton symport

`reaction.ecocyc.TRANS-RXN-108H`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-108H`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + THYMIDINE -> PROTON + THYMIDINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + THYMIDINE -> PROTON + THYMIDINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nupC (protein.P0AFF2), nupG (protein.P0AFF4). Substrates: H+ (molecule.C00080), Thymidine (molecule.C00214). Products: H+ (molecule.C00080), Thymidine (molecule.C00214).

## Annotation

PROTON + THYMIDINE -> PROTON + THYMIDINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFF4|protein.P0AFF4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00214|molecule.C00214]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00214|molecule.C00214]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-108H`

## Notes

PROTON + THYMIDINE -> PROTON + THYMIDINE; direction=LEFT-TO-RIGHT
