---
entity_id: "reaction.ecocyc.TRANS-RXN-20"
entity_type: "reaction"
name: "L-fucose:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-20"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-fucose:proton symport

`reaction.ecocyc.TRANS-RXN-20`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-20`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

L-fucoses + PROTON -> L-fucoses + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: L-fucoses + PROTON -> L-fucoses + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fucP (protein.P11551). Substrates: H+ (molecule.C00080), L-Fucose (molecule.C01019). Products: H+ (molecule.C00080), L-Fucose (molecule.C01019).

## Annotation

L-fucoses + PROTON -> L-fucoses + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P11551|protein.P11551]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01019|molecule.C01019]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01019|molecule.C01019]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-20`

## Notes

L-fucoses + PROTON -> L-fucoses + PROTON; direction=LEFT-TO-RIGHT
