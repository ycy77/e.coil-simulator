---
entity_id: "reaction.ecocyc.TRANS-RXN-108E"
entity_type: "reaction"
name: "deoxyinosine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-108E"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# deoxyinosine:proton symport

`reaction.ecocyc.TRANS-RXN-108E`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-108E`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + DEOXYINOSINE -> PROTON + DEOXYINOSINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + DEOXYINOSINE -> PROTON + DEOXYINOSINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nupC (protein.P0AFF2), nupG (protein.P0AFF4). Substrates: H+ (molecule.C00080), Deoxyinosine (molecule.C05512). Products: H+ (molecule.C00080), Deoxyinosine (molecule.C05512).

## Annotation

PROTON + DEOXYINOSINE -> PROTON + DEOXYINOSINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFF4|protein.P0AFF4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05512|molecule.C05512]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05512|molecule.C05512]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-108E`

## Notes

PROTON + DEOXYINOSINE -> PROTON + DEOXYINOSINE; direction=LEFT-TO-RIGHT
