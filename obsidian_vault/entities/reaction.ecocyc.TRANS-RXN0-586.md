---
entity_id: "reaction.ecocyc.TRANS-RXN0-586"
entity_type: "reaction"
name: "sulfate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-586"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# sulfate:proton symport

`reaction.ecocyc.TRANS-RXN0-586`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-586`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

SULFATE + PROTON -> SULFATE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: SULFATE + PROTON -> SULFATE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by cysZ (protein.P0A6J3). Substrates: Sulfate (molecule.C00059), H+ (molecule.C00080). Products: Sulfate (molecule.C00059), H+ (molecule.C00080).

## Annotation

SULFATE + PROTON -> SULFATE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A6J3|protein.P0A6J3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00059|molecule.C00059]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00059|molecule.C00059]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN0-586`

## Notes

SULFATE + PROTON -> SULFATE + PROTON; direction=REVERSIBLE
