---
entity_id: "reaction.ecocyc.RXN-15915"
entity_type: "reaction"
name: "RXN-15915"
source_database: "EcoCyc"
source_id: "RXN-15915"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15915

`reaction.ecocyc.RXN-15915`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15915`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15424 + HypE-Proteins -> HypE-S-carboxamide + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-15424 + HypE-Proteins -> HypE-S-carboxamide + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: (O-carbamoyl)adenylate (molecule.ecocyc.CPD-15424). Products: AMP (molecule.C00020), H+ (molecule.C00080).

## Annotation

CPD-15424 + HypE-Proteins -> HypE-S-carboxamide + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15424|molecule.ecocyc.CPD-15424]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15915`

## Notes

CPD-15424 + HypE-Proteins -> HypE-S-carboxamide + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
