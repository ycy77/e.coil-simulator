---
entity_id: "reaction.ecocyc.TRANS-RXN-108F"
entity_type: "reaction"
name: "deoxyuridine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-108F"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# deoxyuridine:proton symport

`reaction.ecocyc.TRANS-RXN-108F`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-108F`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + DEOXYURIDINE -> PROTON + DEOXYURIDINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + DEOXYURIDINE -> PROTON + DEOXYURIDINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nupC (protein.P0AFF2). Substrates: H+ (molecule.C00080), Deoxyuridine (molecule.C00526). Products: H+ (molecule.C00080), Deoxyuridine (molecule.C00526).

## Annotation

PROTON + DEOXYURIDINE -> PROTON + DEOXYURIDINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00526|molecule.C00526]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00526|molecule.C00526]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-108F`

## Notes

PROTON + DEOXYURIDINE -> PROTON + DEOXYURIDINE; direction=LEFT-TO-RIGHT
