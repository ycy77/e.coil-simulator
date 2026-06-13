---
entity_id: "reaction.ecocyc.TRANS-RXN-27"
entity_type: "reaction"
name: "shikimate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-27"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# shikimate:proton symport

`reaction.ecocyc.TRANS-RXN-27`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-27`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + SHIKIMATE -> PROTON + SHIKIMATE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + SHIKIMATE -> PROTON + SHIKIMATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by shiA (protein.P76350). Substrates: H+ (molecule.C00080), Shikimate (molecule.C00493). Products: H+ (molecule.C00080), Shikimate (molecule.C00493).

## Annotation

PROTON + SHIKIMATE -> PROTON + SHIKIMATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P76350|protein.P76350]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00493|molecule.C00493]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00493|molecule.C00493]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-27`

## Notes

PROTON + SHIKIMATE -> PROTON + SHIKIMATE; direction=REVERSIBLE
