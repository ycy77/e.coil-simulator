---
entity_id: "reaction.ecocyc.TRANS-RXN0-481"
entity_type: "reaction"
name: "TRANS-RXN0-481"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-481"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-481

`reaction.ecocyc.TRANS-RXN0-481`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-481`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NICOTINAMIDE_RIBOSE -> NICOTINAMIDE_RIBOSE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: NICOTINAMIDE_RIBOSE -> NICOTINAMIDE_RIBOSE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pnuC (protein.P0AFK2). Substrates: Nicotinamide-beta-riboside (molecule.C03150). Products: Nicotinamide-beta-riboside (molecule.C03150).

## Annotation

NICOTINAMIDE_RIBOSE -> NICOTINAMIDE_RIBOSE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0AFK2|protein.P0AFK2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C03150|molecule.C03150]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03150|molecule.C03150]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-481`

## Notes

NICOTINAMIDE_RIBOSE -> NICOTINAMIDE_RIBOSE; direction=LEFT-TO-RIGHT
