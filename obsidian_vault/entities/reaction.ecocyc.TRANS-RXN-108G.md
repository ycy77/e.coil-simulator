---
entity_id: "reaction.ecocyc.TRANS-RXN-108G"
entity_type: "reaction"
name: "inosine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-108G"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# inosine:proton symport

`reaction.ecocyc.TRANS-RXN-108G`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-108G`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + INOSINE -> PROTON + INOSINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + INOSINE -> PROTON + INOSINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nupC (protein.P0AFF2), nupG (protein.P0AFF4). Substrates: H+ (molecule.C00080), Inosine (molecule.C00294). Products: H+ (molecule.C00080), Inosine (molecule.C00294).

## Annotation

PROTON + INOSINE -> PROTON + INOSINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFF4|protein.P0AFF4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00294|molecule.C00294]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00294|molecule.C00294]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-108G`

## Notes

PROTON + INOSINE -> PROTON + INOSINE; direction=LEFT-TO-RIGHT
