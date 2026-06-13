---
entity_id: "reaction.ecocyc.RXN0-7332"
entity_type: "reaction"
name: "RXN0-7332"
source_database: "EcoCyc"
source_id: "RXN0-7332"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-ACT"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7332

`reaction.ecocyc.RXN0-7332`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7332`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-ACT

## Enriched Summary

Represents the final reaction in the reverse phosphorelay of the PWY0-1505 "ArcAB signal transduction system". EcoCyc reaction equation: PHOSPHO-ARCB-ASP -> ARCB-CPLX + Pi; direction=LEFT-TO-RIGHT. Represents the final reaction in the reverse phosphorelay of the PWY0-1505 "ArcAB signal transduction system".

## Biological Role

Products: phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY0-1505` ArcAB Two-Component Signal Transduction System, quinone dependent (EcoCyc)

## Annotation

Represents the final reaction in the reverse phosphorelay of the PWY0-1505 "ArcAB signal transduction system".

## Pathways

- `ecocyc.PWY0-1505` ArcAB Two-Component Signal Transduction System, quinone dependent (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:RXN0-7332`

## Notes

PHOSPHO-ARCB-ASP -> ARCB-CPLX + Pi; direction=LEFT-TO-RIGHT
