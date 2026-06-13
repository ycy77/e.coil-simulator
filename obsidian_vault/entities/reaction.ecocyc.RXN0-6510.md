---
entity_id: "reaction.ecocyc.RXN0-6510"
entity_type: "reaction"
name: "RXN0-6510"
source_database: "EcoCyc"
source_id: "RXN0-6510"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6510

`reaction.ecocyc.RXN0-6510`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6510`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2362 -> CPD0-2363; direction=REVERSIBLE EcoCyc reaction equation: CPD0-2362 -> CPD0-2363; direction=REVERSIBLE.

## Biological Role

Catalyzed by paaG (protein.P77467). Substrates: 2-(1,2-Epoxy-1,2-dihydrophenyl)acetyl-CoA (molecule.C20062). Products: 2-Oxepin-2(3H)-ylideneacetyl-CoA (molecule.C19975).

## Enriched Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Annotation

CPD0-2362 -> CPD0-2363; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-321` phenylacetate degradation I (aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P77467|protein.P77467]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C19975|molecule.C19975]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C20062|molecule.C20062]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6510`

## Notes

CPD0-2362 -> CPD0-2363; direction=REVERSIBLE
