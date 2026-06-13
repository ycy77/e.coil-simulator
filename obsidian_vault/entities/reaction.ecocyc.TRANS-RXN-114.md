---
entity_id: "reaction.ecocyc.TRANS-RXN-114"
entity_type: "reaction"
name: "phosphate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-114"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# phosphate:proton symport

`reaction.ecocyc.TRANS-RXN-114`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-114`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + Pi -> PROTON + Pi; direction=REVERSIBLE EcoCyc reaction equation: PROTON + Pi -> PROTON + Pi; direction=REVERSIBLE.

## Biological Role

Catalyzed by pitA (protein.P0AFJ7), pitB (protein.P43676). Substrates: H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi). Products: H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

PROTON + Pi -> PROTON + Pi; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AFJ7|protein.P0AFJ7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P43676|protein.P43676]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-114`

## Notes

PROTON + Pi -> PROTON + Pi; direction=REVERSIBLE
