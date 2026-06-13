---
entity_id: "reaction.ecocyc.RXN-23923"
entity_type: "reaction"
name: "RXN-23923"
source_database: "EcoCyc"
source_id: "RXN-23923"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23923

`reaction.ecocyc.RXN-23923`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23923`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-26477 -> CPD-22841 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-26477 -> CPD-22841 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: (L-homocysteinyl)adenylate (molecule.ecocyc.CPD-26477). Products: AMP (molecule.C00020), H+ (molecule.C00080), L-homocysteine thiolactone (molecule.ecocyc.CPD-22841).

## Annotation

CPD-26477 -> CPD-22841 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-22841|molecule.ecocyc.CPD-22841]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-26477|molecule.ecocyc.CPD-26477]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23923`

## Notes

CPD-26477 -> CPD-22841 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
