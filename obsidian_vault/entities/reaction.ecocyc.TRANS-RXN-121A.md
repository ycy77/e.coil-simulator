---
entity_id: "reaction.ecocyc.TRANS-RXN-121A"
entity_type: "reaction"
name: "malate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-121A"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# malate:proton symport

`reaction.ecocyc.TRANS-RXN-121A`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-121A`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + MAL -> PROTON + MAL; direction=REVERSIBLE EcoCyc reaction equation: PROTON + MAL -> PROTON + MAL; direction=REVERSIBLE.

## Biological Role

Catalyzed by dctA (protein.P0A830). Substrates: H+ (molecule.C00080), (S)-Malate (molecule.C00149). Products: H+ (molecule.C00080), (S)-Malate (molecule.C00149).

## Annotation

PROTON + MAL -> PROTON + MAL; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A830|protein.P0A830]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00149|molecule.C00149]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-121A`

## Notes

PROTON + MAL -> PROTON + MAL; direction=REVERSIBLE
