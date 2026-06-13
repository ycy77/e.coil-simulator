---
entity_id: "reaction.ecocyc.RXN-23850"
entity_type: "reaction"
name: "RXN-23850"
source_database: "EcoCyc"
source_id: "RXN-23850"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23850

`reaction.ecocyc.RXN-23850`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23850`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NITRIC-OXIDE + WATER + Acceptor -> NITRITE + Donor-H1 + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: NITRIC-OXIDE + WATER + Acceptor -> NITRITE + Donor-H1 + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by ytfE (protein.P69506). Substrates: H2O (molecule.C00001), Nitric oxide (molecule.C00533). Products: H+ (molecule.C00080), Nitrite (molecule.C00088).

## Annotation

NITRIC-OXIDE + WATER + Acceptor -> NITRITE + Donor-H1 + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P69506|protein.P69506]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00533|molecule.C00533]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23850`

## Notes

NITRIC-OXIDE + WATER + Acceptor -> NITRITE + Donor-H1 + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
