---
entity_id: "reaction.ecocyc.RXN-20002"
entity_type: "reaction"
name: "RXN-20002"
source_database: "EcoCyc"
source_id: "RXN-20002"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-20002

`reaction.ecocyc.RXN-20002`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-20002`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ENTEROBACTIN + FE+3 -> FERRIC-ENTEROBACTIN-COMPLEX + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ENTEROBACTIN + FE+3 -> FERRIC-ENTEROBACTIN-COMPLEX + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Enterochelin (molecule.C05821), Fe3+ (molecule.C14819). Products: H+ (molecule.C00080), Fe-enterobactin (molecule.C06230).

## Annotation

ENTEROBACTIN + FE+3 -> FERRIC-ENTEROBACTIN-COMPLEX + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06230|molecule.C06230]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05821|molecule.C05821]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C14819|molecule.C14819]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-20002`

## Notes

ENTEROBACTIN + FE+3 -> FERRIC-ENTEROBACTIN-COMPLEX + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
