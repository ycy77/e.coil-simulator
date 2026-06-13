---
entity_id: "reaction.ecocyc.RXN-23895"
entity_type: "reaction"
name: "RXN-23895"
source_database: "EcoCyc"
source_id: "RXN-23895"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23895

`reaction.ecocyc.RXN-23895`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23895`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-12085 + CYS-tRNAs -> Charged-CYS-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-12085 + CYS-tRNAs -> Charged-CYS-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: (L-cysteinyl)adenylate (molecule.ecocyc.CPD-12085). Products: AMP (molecule.C00020), H+ (molecule.C00080).

## Annotation

CPD-12085 + CYS-tRNAs -> Charged-CYS-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12085|molecule.ecocyc.CPD-12085]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23895`

## Notes

CPD-12085 + CYS-tRNAs -> Charged-CYS-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
