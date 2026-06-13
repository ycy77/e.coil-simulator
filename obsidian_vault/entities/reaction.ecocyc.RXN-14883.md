---
entity_id: "reaction.ecocyc.RXN-14883"
entity_type: "reaction"
name: "RXN-14883"
source_database: "EcoCyc"
source_id: "RXN-14883"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL|CCO-PERI-BAC|CCO-EXTRACELLULAR"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14883

`reaction.ecocyc.RXN-14883`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14883`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL|CCO-PERI-BAC|CCO-EXTRACELLULAR

## Enriched Summary

CPD-15818 -> D-Ribopyranose; direction=REVERSIBLE EcoCyc reaction equation: CPD-15818 -> D-Ribopyranose; direction=REVERSIBLE.

## Biological Role

Substrates: aldehydo-D-ribose (molecule.ecocyc.CPD-15818). Products: D-ribopyranose (molecule.ecocyc.D-Ribopyranose).

## Annotation

CPD-15818 -> D-Ribopyranose; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.D-Ribopyranose|molecule.ecocyc.D-Ribopyranose]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15818|molecule.ecocyc.CPD-15818]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14883`

## Notes

CPD-15818 -> D-Ribopyranose; direction=REVERSIBLE
