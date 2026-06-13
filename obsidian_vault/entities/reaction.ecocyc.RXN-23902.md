---
entity_id: "reaction.ecocyc.RXN-23902"
entity_type: "reaction"
name: "RXN-23902"
source_database: "EcoCyc"
source_id: "RXN-23902"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23902

`reaction.ecocyc.RXN-23902`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23902`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-25317 + VAL-tRNAs -> Charged-VAL-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-25317 + VAL-tRNAs -> Charged-VAL-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: (L-valyl)adenylate (molecule.ecocyc.CPD-25317). Products: AMP (molecule.C00020), H+ (molecule.C00080).

## Annotation

CPD-25317 + VAL-tRNAs -> Charged-VAL-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-25317|molecule.ecocyc.CPD-25317]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23902`

## Notes

CPD-25317 + VAL-tRNAs -> Charged-VAL-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
