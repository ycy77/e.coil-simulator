---
entity_id: "reaction.ecocyc.RXN-14477"
entity_type: "reaction"
name: "RXN-14477"
source_database: "EcoCyc"
source_id: "RXN-14477"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14477

`reaction.ecocyc.RXN-14477`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14477`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ENTEROBACTIN + WATER -> CPD0-2483 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ENTEROBACTIN + WATER -> CPD0-2483 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), Enterochelin (molecule.C05821). Products: H+ (molecule.C00080), N-(2,3-dihydroxybenzoyl)-L-serine trimer (molecule.ecocyc.CPD0-2483).

## Annotation

ENTEROBACTIN + WATER -> CPD0-2483 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2483|molecule.ecocyc.CPD0-2483]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05821|molecule.C05821]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14477`

## Notes

ENTEROBACTIN + WATER -> CPD0-2483 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
