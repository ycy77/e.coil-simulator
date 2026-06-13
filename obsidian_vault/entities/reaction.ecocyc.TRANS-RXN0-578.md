---
entity_id: "reaction.ecocyc.TRANS-RXN0-578"
entity_type: "reaction"
name: "TRANS-RXN0-578"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-578"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-578

`reaction.ecocyc.TRANS-RXN0-578`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-578`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

GUANINE + PROTON -> GUANINE + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: GUANINE + PROTON -> GUANINE + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ghxP (protein.P0AF52), ghxQ (protein.Q46817). Substrates: H+ (molecule.C00080), Guanine (molecule.C00242). Products: H+ (molecule.C00080), Guanine (molecule.C00242).

## Annotation

GUANINE + PROTON -> GUANINE + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AF52|protein.P0AF52]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q46817|protein.Q46817]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00242|molecule.C00242]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00242|molecule.C00242]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-578`

## Notes

GUANINE + PROTON -> GUANINE + PROTON; direction=LEFT-TO-RIGHT
