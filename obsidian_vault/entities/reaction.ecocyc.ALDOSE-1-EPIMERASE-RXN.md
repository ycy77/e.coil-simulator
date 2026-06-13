---
entity_id: "reaction.ecocyc.ALDOSE-1-EPIMERASE-RXN"
entity_type: "reaction"
name: "ALDOSE-1-EPIMERASE-RXN"
source_database: "EcoCyc"
source_id: "ALDOSE-1-EPIMERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ALDOSE-1-EPIMERASE-RXN

`reaction.ecocyc.ALDOSE-1-EPIMERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALDOSE-1-EPIMERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ALPHA-GLUCOSE -> GLC; direction=REVERSIBLE EcoCyc reaction equation: ALPHA-GLUCOSE -> GLC; direction=REVERSIBLE.

## Biological Role

Substrates: alpha-D-Glucose (molecule.C00267). Products: beta-D-Glucose (molecule.C00221).

## Enriched Pathways

- `ecocyc.PWY0-1466` trehalose degradation VI (periplasmic) (EcoCyc)

## Annotation

ALPHA-GLUCOSE -> GLC; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1466` trehalose degradation VI (periplasmic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00221|molecule.C00221]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00267|molecule.C00267]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ALDOSE-1-EPIMERASE-RXN`

## Notes

ALPHA-GLUCOSE -> GLC; direction=REVERSIBLE
