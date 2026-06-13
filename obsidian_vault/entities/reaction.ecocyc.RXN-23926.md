---
entity_id: "reaction.ecocyc.RXN-23926"
entity_type: "reaction"
name: "RXN-23926"
source_database: "EcoCyc"
source_id: "RXN-23926"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23926

`reaction.ecocyc.RXN-23926`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23926`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-26478 -> CPD-15554 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-26478 -> CPD-15554 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: (L-homoseryl)adenylate (molecule.ecocyc.CPD-26478). Products: AMP (molecule.C00020), H+ (molecule.C00080), L-homoserine lactone (molecule.ecocyc.CPD-15554).

## Annotation

CPD-26478 -> CPD-15554 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15554|molecule.ecocyc.CPD-15554]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-26478|molecule.ecocyc.CPD-26478]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23926`

## Notes

CPD-26478 -> CPD-15554 + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
