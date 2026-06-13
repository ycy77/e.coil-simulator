---
entity_id: "reaction.ecocyc.RXN0-1382"
entity_type: "reaction"
name: "RXN0-1382"
source_database: "EcoCyc"
source_id: "RXN0-1382"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1382

`reaction.ecocyc.RXN0-1382`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1382`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FORMYL-COA + OXALATE -> FORMATE + OXALYL-COA; direction=REVERSIBLE EcoCyc reaction equation: FORMYL-COA + OXALATE -> FORMATE + OXALYL-COA; direction=REVERSIBLE.

## Biological Role

Catalyzed by formyl-CoA transferase (complex.ecocyc.CPLX0-1142). Substrates: Oxalate (molecule.C00209), Formyl-CoA (molecule.C00798). Products: Formate (molecule.C00058), Oxalyl-CoA (molecule.C00313).

## Annotation

FORMYL-COA + OXALATE -> FORMATE + OXALYL-COA; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1142|complex.ecocyc.CPLX0-1142]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00313|molecule.C00313]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00209|molecule.C00209]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00798|molecule.C00798]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00209|molecule.C00209]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-1382`

## Notes

FORMYL-COA + OXALATE -> FORMATE + OXALYL-COA; direction=REVERSIBLE
