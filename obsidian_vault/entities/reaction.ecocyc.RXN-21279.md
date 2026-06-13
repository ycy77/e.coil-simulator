---
entity_id: "reaction.ecocyc.RXN-21279"
entity_type: "reaction"
name: "RXN-21279"
source_database: "EcoCyc"
source_id: "RXN-21279"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21279

`reaction.ecocyc.RXN-21279`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21279`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

a-5-deoxyribose-5-phosphate-DNA -> 5-Phospho-terminated-DNAs + CPD-22978 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: a-5-deoxyribose-5-phosphate-DNA -> 5-Phospho-terminated-DNAs + CPD-22978 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mutM (protein.P05523). Products: H+ (molecule.C00080), 4-hydroxy-2-pentenal-5-phosphate (molecule.ecocyc.CPD-22978).

## Annotation

a-5-deoxyribose-5-phosphate-DNA -> 5-Phospho-terminated-DNAs + CPD-22978 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P05523|protein.P05523]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-22978|molecule.ecocyc.CPD-22978]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## External IDs

- `EcoCyc:RXN-21279`

## Notes

a-5-deoxyribose-5-phosphate-DNA -> 5-Phospho-terminated-DNAs + CPD-22978 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
