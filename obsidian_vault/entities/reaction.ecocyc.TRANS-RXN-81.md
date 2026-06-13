---
entity_id: "reaction.ecocyc.TRANS-RXN-81"
entity_type: "reaction"
name: "fructuronate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-81"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# fructuronate:proton symport

`reaction.ecocyc.TRANS-RXN-81`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-81`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

FRUCTURONATE + PROTON -> FRUCTURONATE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: FRUCTURONATE + PROTON -> FRUCTURONATE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by gntP (protein.P0AC94). Substrates: H+ (molecule.C00080), D-Fructuronate (molecule.C00905). Products: H+ (molecule.C00080), D-Fructuronate (molecule.C00905).

## Annotation

FRUCTURONATE + PROTON -> FRUCTURONATE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AC94|protein.P0AC94]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00905|molecule.C00905]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00905|molecule.C00905]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-81`

## Notes

FRUCTURONATE + PROTON -> FRUCTURONATE + PROTON; direction=REVERSIBLE
