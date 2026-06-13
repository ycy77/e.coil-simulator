---
entity_id: "reaction.ecocyc.TRANS-RXN-72"
entity_type: "reaction"
name: "L-threonine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-72"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-threonine:proton symport

`reaction.ecocyc.TRANS-RXN-72`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-72`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + THR -> PROTON + THR; direction=REVERSIBLE EcoCyc reaction equation: PROTON + THR -> PROTON + THR; direction=REVERSIBLE.

## Biological Role

Catalyzed by tdcC (protein.P0AAD8), thrP (protein.P27837). Substrates: H+ (molecule.C00080), L-Threonine (molecule.C00188). Products: H+ (molecule.C00080), L-Threonine (molecule.C00188).

## Annotation

PROTON + THR -> PROTON + THR; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AAD8|protein.P0AAD8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P27837|protein.P27837]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-72`

## Notes

PROTON + THR -> PROTON + THR; direction=REVERSIBLE
