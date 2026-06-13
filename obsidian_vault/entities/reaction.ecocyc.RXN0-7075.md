---
entity_id: "reaction.ecocyc.RXN0-7075"
entity_type: "reaction"
name: "RXN0-7075"
source_database: "EcoCyc"
source_id: "RXN0-7075"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7075

`reaction.ecocyc.RXN0-7075`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7075`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACETYL-COA + OXALATE -> OXALYL-COA + ACET; direction=REVERSIBLE EcoCyc reaction equation: ACETYL-COA + OXALATE -> OXALYL-COA + ACET; direction=REVERSIBLE.

## Biological Role

Catalyzed by acetyl-CoA:oxalate CoA-transferase (complex.ecocyc.CPLX0-8032). Substrates: Acetyl-CoA (molecule.C00024), Oxalate (molecule.C00209). Products: Acetate (molecule.C00033), Oxalyl-CoA (molecule.C00313).

## Annotation

ACETYL-COA + OXALATE -> OXALYL-COA + ACET; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8032|complex.ecocyc.CPLX0-8032]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00313|molecule.C00313]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00209|molecule.C00209]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7075`

## Notes

ACETYL-COA + OXALATE -> OXALYL-COA + ACET; direction=REVERSIBLE
