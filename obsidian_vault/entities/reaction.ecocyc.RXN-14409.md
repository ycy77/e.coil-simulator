---
entity_id: "reaction.ecocyc.RXN-14409"
entity_type: "reaction"
name: "RXN-14409"
source_database: "EcoCyc"
source_id: "RXN-14409"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL|CCO-PERI-BAC|CCO-EXTRACELLULAR"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14409

`reaction.ecocyc.RXN-14409`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14409`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL|CCO-PERI-BAC|CCO-EXTRACELLULAR

## Enriched Summary

CPD-15590 -> D-galactopyranose; direction=REVERSIBLE EcoCyc reaction equation: CPD-15590 -> D-galactopyranose; direction=REVERSIBLE.

## Biological Role

Substrates: aldehydo-D-galactose (molecule.ecocyc.CPD-15590). Products: D-Galactose (molecule.C00124).

## Annotation

CPD-15590 -> D-galactopyranose; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00124|molecule.C00124]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15590|molecule.ecocyc.CPD-15590]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14409`

## Notes

CPD-15590 -> D-galactopyranose; direction=REVERSIBLE
