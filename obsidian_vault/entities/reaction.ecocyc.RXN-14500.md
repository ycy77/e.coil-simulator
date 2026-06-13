---
entity_id: "reaction.ecocyc.RXN-14500"
entity_type: "reaction"
name: "RXN-14500"
source_database: "EcoCyc"
source_id: "RXN-14500"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL|CCO-PERI-BAC|CCO-EXTRACELLULAR"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14500

`reaction.ecocyc.RXN-14500`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14500`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL|CCO-PERI-BAC|CCO-EXTRACELLULAR

## Enriched Summary

CPD-15373 -> D-mannopyranose; direction=REVERSIBLE EcoCyc reaction equation: CPD-15373 -> D-mannopyranose; direction=REVERSIBLE.

## Biological Role

Substrates: aldehydo-D-mannose (molecule.ecocyc.CPD-15373). Products: D-mannopyranose (molecule.ecocyc.D-mannopyranose).

## Annotation

CPD-15373 -> D-mannopyranose; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.D-mannopyranose|molecule.ecocyc.D-mannopyranose]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15373|molecule.ecocyc.CPD-15373]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14500`

## Notes

CPD-15373 -> D-mannopyranose; direction=REVERSIBLE
