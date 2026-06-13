---
entity_id: "reaction.ecocyc.RXN-23937"
entity_type: "reaction"
name: "RXN-23937"
source_database: "EcoCyc"
source_id: "RXN-23937"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23937

`reaction.ecocyc.RXN-23937`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23937`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-9993 + ALA-tRNAs -> glycyl-tRNAAla + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-9993 + ALA-tRNAs -> glycyl-tRNAAla + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: (glycyl)adenylate (molecule.ecocyc.CPD-9993). Products: AMP (molecule.C00020).

## Annotation

CPD-9993 + ALA-tRNAs -> glycyl-tRNAAla + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-9993|molecule.ecocyc.CPD-9993]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23937`

## Notes

CPD-9993 + ALA-tRNAs -> glycyl-tRNAAla + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
