---
entity_id: "reaction.ecocyc.TRANS-RXN0-530"
entity_type: "reaction"
name: "urate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-530"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# urate:proton symport

`reaction.ecocyc.TRANS-RXN0-530`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-530`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

URATE + PROTON -> URATE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: URATE + PROTON -> URATE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by uacT (protein.Q46821). Substrates: H+ (molecule.C00080), Urate (molecule.C00366). Products: H+ (molecule.C00080), Urate (molecule.C00366).

## Annotation

URATE + PROTON -> URATE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.Q46821|protein.Q46821]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00366|molecule.C00366]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00366|molecule.C00366]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-530`

## Notes

URATE + PROTON -> URATE + PROTON; direction=REVERSIBLE
