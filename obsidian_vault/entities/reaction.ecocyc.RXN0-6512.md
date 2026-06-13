---
entity_id: "reaction.ecocyc.RXN0-6512"
entity_type: "reaction"
name: "RXN0-6512"
source_database: "EcoCyc"
source_id: "RXN0-6512"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6512

`reaction.ecocyc.RXN0-6512`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6512`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TRANS-23-DEHYDROADIPYL-COA + ACETYL-COA -> CPD0-2364 + CO-A; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: TRANS-23-DEHYDROADIPYL-COA + ACETYL-COA -> CPD0-2364 + CO-A; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by paaJ (protein.P0C7L2). Substrates: Acetyl-CoA (molecule.C00024), 5-Carboxy-2-pentenoyl-CoA (molecule.C14144). Products: CoA (molecule.C00010), 3-Oxo-5,6-dehydrosuberyl-CoA (molecule.C19945).

## Enriched Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Annotation

TRANS-23-DEHYDROADIPYL-COA + ACETYL-COA -> CPD0-2364 + CO-A; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0C7L2|protein.P0C7L2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C19945|molecule.C19945]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C14144|molecule.C14144]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6512`

## Notes

TRANS-23-DEHYDROADIPYL-COA + ACETYL-COA -> CPD0-2364 + CO-A; direction=PHYSIOL-RIGHT-TO-LEFT
