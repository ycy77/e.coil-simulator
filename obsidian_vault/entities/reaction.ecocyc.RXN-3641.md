---
entity_id: "reaction.ecocyc.RXN-3641"
entity_type: "reaction"
name: "RXN-3641"
source_database: "EcoCyc"
source_id: "RXN-3641"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-3641

`reaction.ecocyc.RXN-3641`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-3641`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SUC-COA + ACETYL-COA -> 3-KETO-ADIPYL-COA + CO-A; direction=REVERSIBLE EcoCyc reaction equation: SUC-COA + ACETYL-COA -> 3-KETO-ADIPYL-COA + CO-A; direction=REVERSIBLE.

## Biological Role

Catalyzed by paaJ (protein.P0C7L2). Substrates: Acetyl-CoA (molecule.C00024), Succinyl-CoA (molecule.C00091). Products: CoA (molecule.C00010), 3-Oxoadipyl-CoA (molecule.C02232).

## Enriched Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Annotation

SUC-COA + ACETYL-COA -> 3-KETO-ADIPYL-COA + CO-A; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0C7L2|protein.P0C7L2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02232|molecule.C02232]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00091|molecule.C00091]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-3641`

## Notes

SUC-COA + ACETYL-COA -> 3-KETO-ADIPYL-COA + CO-A; direction=REVERSIBLE
