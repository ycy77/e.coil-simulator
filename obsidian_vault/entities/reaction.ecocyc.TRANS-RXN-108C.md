---
entity_id: "reaction.ecocyc.TRANS-RXN-108C"
entity_type: "reaction"
name: "deoxyadenosine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-108C"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# deoxyadenosine:proton symport

`reaction.ecocyc.TRANS-RXN-108C`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-108C`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + DEOXYADENOSINE -> PROTON + DEOXYADENOSINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + DEOXYADENOSINE -> PROTON + DEOXYADENOSINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nupC (protein.P0AFF2), nupG (protein.P0AFF4). Substrates: H+ (molecule.C00080), Deoxyadenosine (molecule.C00559). Products: H+ (molecule.C00080), Deoxyadenosine (molecule.C00559).

## Annotation

PROTON + DEOXYADENOSINE -> PROTON + DEOXYADENOSINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFF4|protein.P0AFF4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00559|molecule.C00559]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00559|molecule.C00559]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-108C`

## Notes

PROTON + DEOXYADENOSINE -> PROTON + DEOXYADENOSINE; direction=LEFT-TO-RIGHT
