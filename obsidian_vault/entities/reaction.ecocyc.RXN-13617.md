---
entity_id: "reaction.ecocyc.RXN-13617"
entity_type: "reaction"
name: "RXN-13617"
source_database: "EcoCyc"
source_id: "RXN-13617"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13617

`reaction.ecocyc.RXN-13617`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13617`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-196 + ACETYL-COA -> CPD0-2123 + CO-A; direction=REVERSIBLE EcoCyc reaction equation: CPD-196 + ACETYL-COA -> CPD0-2123 + CO-A; direction=REVERSIBLE.

## Biological Role

Substrates: Acetyl-CoA (molecule.C00024), Octanoyl-CoA (molecule.C01944). Products: CoA (molecule.C00010), 3-Oxodecanoyl-CoA (molecule.C05265).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

CPD-196 + ACETYL-COA -> CPD0-2123 + CO-A; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05265|molecule.C05265]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01944|molecule.C01944]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13617`

## Notes

CPD-196 + ACETYL-COA -> CPD0-2123 + CO-A; direction=REVERSIBLE
