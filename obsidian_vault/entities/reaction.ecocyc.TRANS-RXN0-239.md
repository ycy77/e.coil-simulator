---
entity_id: "reaction.ecocyc.TRANS-RXN0-239"
entity_type: "reaction"
name: "nitrate:nitrite antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-239"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# nitrate:nitrite antiport

`reaction.ecocyc.TRANS-RXN0-239`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-239`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NITRATE + NITRITE -> NITRATE + NITRITE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: NITRATE + NITRITE -> NITRATE + NITRITE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by narK (protein.P10903), narU (protein.P37758). Substrates: Nitrite (molecule.C00088), Nitrate (molecule.C00244). Products: Nitrite (molecule.C00088), Nitrate (molecule.C00244).

## Annotation

NITRATE + NITRITE -> NITRATE + NITRITE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P10903|protein.P10903]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P37758|protein.P37758]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00244|molecule.C00244]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00244|molecule.C00244]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-239`

## Notes

NITRATE + NITRITE -> NITRATE + NITRITE; direction=PHYSIOL-LEFT-TO-RIGHT
