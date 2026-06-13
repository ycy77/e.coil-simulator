---
entity_id: "reaction.ecocyc.RXN-2425"
entity_type: "reaction"
name: "RXN-2425"
source_database: "EcoCyc"
source_id: "RXN-2425"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-2425

`reaction.ecocyc.RXN-2425`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-2425`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-HYDROXYADIPYL-COA -> TRANS-23-DEHYDROADIPYL-COA + WATER; direction=REVERSIBLE EcoCyc reaction equation: 3-HYDROXYADIPYL-COA -> TRANS-23-DEHYDROADIPYL-COA + WATER; direction=REVERSIBLE.

## Biological Role

Catalyzed by paaF (protein.P76082). Substrates: (3S)-3-Hydroxyadipyl-CoA (molecule.C14145). Products: H2O (molecule.C00001), 5-Carboxy-2-pentenoyl-CoA (molecule.C14144).

## Enriched Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Annotation

3-HYDROXYADIPYL-COA -> TRANS-23-DEHYDROADIPYL-COA + WATER; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P76082|protein.P76082]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C14144|molecule.C14144]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C14145|molecule.C14145]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-2425`

## Notes

3-HYDROXYADIPYL-COA -> TRANS-23-DEHYDROADIPYL-COA + WATER; direction=REVERSIBLE
