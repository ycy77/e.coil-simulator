---
entity_id: "reaction.ecocyc.RXN-23954"
entity_type: "reaction"
name: "RXN-23954"
source_database: "EcoCyc"
source_id: "RXN-23954"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23954

`reaction.ecocyc.RXN-23954`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23954`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

VAL-tRNAs + THR + ATP -> Thr-tRNAVal + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: VAL-tRNAs + THR + ATP -> Thr-tRNAVal + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by valS (protein.P07118). Substrates: ATP (molecule.C00002), L-Threonine (molecule.C00188). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

VAL-tRNAs + THR + ATP -> Thr-tRNAVal + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P07118|protein.P07118]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23954`

## Notes

VAL-tRNAs + THR + ATP -> Thr-tRNAVal + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
