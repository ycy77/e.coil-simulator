---
entity_id: "reaction.ecocyc.TRANS-RXN-58"
entity_type: "reaction"
name: "L-lysine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-58"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-lysine:proton symport

`reaction.ecocyc.TRANS-RXN-58`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-58`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + LYS -> PROTON + LYS; direction=REVERSIBLE EcoCyc reaction equation: PROTON + LYS -> PROTON + LYS; direction=REVERSIBLE.

## Biological Role

Catalyzed by lysP (protein.P25737). Substrates: L-Lysine (molecule.C00047), H+ (molecule.C00080). Products: L-Lysine (molecule.C00047), H+ (molecule.C00080).

## Annotation

PROTON + LYS -> PROTON + LYS; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P25737|protein.P25737]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-58`

## Notes

PROTON + LYS -> PROTON + LYS; direction=REVERSIBLE
