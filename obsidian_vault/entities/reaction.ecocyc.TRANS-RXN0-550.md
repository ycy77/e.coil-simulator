---
entity_id: "reaction.ecocyc.TRANS-RXN0-550"
entity_type: "reaction"
name: "arsenate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-550"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# arsenate:proton symport

`reaction.ecocyc.TRANS-RXN0-550`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-550`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ARSENATE + PROTON -> PROTON + ARSENATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ARSENATE + PROTON -> PROTON + ARSENATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pitA (protein.P0AFJ7), pitB (protein.P43676). Substrates: H+ (molecule.C00080), arsenate (molecule.ecocyc.ARSENATE). Products: H+ (molecule.C00080), arsenate (molecule.ecocyc.ARSENATE).

## Enriched Pathways

- `ecocyc.PWY-4621-1` arsenic detoxification VI (E. coli) (EcoCyc)

## Annotation

ARSENATE + PROTON -> PROTON + ARSENATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-4621-1` arsenic detoxification VI (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AFJ7|protein.P0AFJ7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P43676|protein.P43676]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.ARSENATE|molecule.ecocyc.ARSENATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.ARSENATE|molecule.ecocyc.ARSENATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-550`

## Notes

ARSENATE + PROTON -> PROTON + ARSENATE; direction=PHYSIOL-LEFT-TO-RIGHT
