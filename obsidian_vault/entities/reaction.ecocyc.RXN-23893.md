---
entity_id: "reaction.ecocyc.RXN-23893"
entity_type: "reaction"
name: "RXN-23893"
source_database: "EcoCyc"
source_id: "RXN-23893"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23893

`reaction.ecocyc.RXN-23893`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23893`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-21003 + TRP-tRNAs -> Charged-TRP-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-21003 + TRP-tRNAs -> Charged-TRP-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: (L-tryptophanyl)adenylate (molecule.ecocyc.CPD-21003). Products: AMP (molecule.C00020), H+ (molecule.C00080).

## Annotation

CPD-21003 + TRP-tRNAs -> Charged-TRP-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21003|molecule.ecocyc.CPD-21003]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23893`

## Notes

CPD-21003 + TRP-tRNAs -> Charged-TRP-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
