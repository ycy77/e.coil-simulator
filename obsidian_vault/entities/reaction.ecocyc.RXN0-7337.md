---
entity_id: "reaction.ecocyc.RXN0-7337"
entity_type: "reaction"
name: "RXN0-7337"
source_database: "EcoCyc"
source_id: "RXN0-7337"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7337

`reaction.ecocyc.RXN0-7337`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7337`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Represents the final reaction in the reverse phosphorelay of the BarA/UvrY signal transduction system EcoCyc reaction equation: PHOSPHO-BARA-ASP -> CPLX0-8302 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. Represents the final reaction in the reverse phosphorelay of the BarA/UvrY signal transduction system

## Biological Role

Products: phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY0-1501` BarA UvrY Two-Component Signal Transduction System (EcoCyc)

## Annotation

Represents the final reaction in the reverse phosphorelay of the BarA/UvrY signal transduction system

## Pathways

- `ecocyc.PWY0-1501` BarA UvrY Two-Component Signal Transduction System (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:RXN0-7337`

## Notes

PHOSPHO-BARA-ASP -> CPLX0-8302 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
