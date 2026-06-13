---
entity_id: "reaction.ecocyc.TRANS-RXN-137"
entity_type: "reaction"
name: "TRANS-RXN-137"
source_database: "EcoCyc"
source_id: "TRANS-RXN-137"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-137

`reaction.ecocyc.TRANS-RXN-137`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-137`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NITRITE -> NITRITE; direction=REVERSIBLE EcoCyc reaction equation: NITRITE -> NITRITE; direction=REVERSIBLE.

## Biological Role

Catalyzed by nirC (protein.P0AC26). Substrates: Nitrite (molecule.C00088). Products: Nitrite (molecule.C00088).

## Annotation

NITRITE -> NITRITE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AC26|protein.P0AC26]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-137`

## Notes

NITRITE -> NITRITE; direction=REVERSIBLE
