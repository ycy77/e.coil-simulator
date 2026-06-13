---
entity_id: "reaction.ecocyc.RXN-12565"
entity_type: "reaction"
name: "RXN-12565"
source_database: "EcoCyc"
source_id: "RXN-12565"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12565

`reaction.ecocyc.RXN-12565`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12565`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

BUTYRYL-COA + ACETYL-COA -> K-HEXANOYL-COA + CO-A; direction=REVERSIBLE EcoCyc reaction equation: BUTYRYL-COA + ACETYL-COA -> K-HEXANOYL-COA + CO-A; direction=REVERSIBLE.

## Biological Role

Substrates: Acetyl-CoA (molecule.C00024), Butanoyl-CoA (molecule.C00136). Products: CoA (molecule.C00010), 3-Oxohexanoyl-CoA (molecule.C05269).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

BUTYRYL-COA + ACETYL-COA -> K-HEXANOYL-COA + CO-A; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05269|molecule.C05269]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00136|molecule.C00136]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12565`

## Notes

BUTYRYL-COA + ACETYL-COA -> K-HEXANOYL-COA + CO-A; direction=REVERSIBLE
