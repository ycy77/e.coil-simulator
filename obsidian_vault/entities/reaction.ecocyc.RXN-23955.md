---
entity_id: "reaction.ecocyc.RXN-23955"
entity_type: "reaction"
name: "RXN-23955"
source_database: "EcoCyc"
source_id: "RXN-23955"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23955

`reaction.ecocyc.RXN-23955`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23955`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Thr-tRNAVal + WATER -> VAL-tRNAs + THR + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Thr-tRNAVal + WATER -> VAL-tRNAs + THR + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by valS (protein.P07118). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), L-Threonine (molecule.C00188).

## Annotation

Thr-tRNAVal + WATER -> VAL-tRNAs + THR + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P07118|protein.P07118]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23955`

## Notes

Thr-tRNAVal + WATER -> VAL-tRNAs + THR + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
