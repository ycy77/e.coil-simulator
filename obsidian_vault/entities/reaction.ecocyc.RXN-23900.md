---
entity_id: "reaction.ecocyc.RXN-23900"
entity_type: "reaction"
name: "RXN-23900"
source_database: "EcoCyc"
source_id: "RXN-23900"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23900

`reaction.ecocyc.RXN-23900`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23900`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-9994 + THR-tRNAs -> Charged-THR-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-9994 + THR-tRNAs -> Charged-THR-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: (L-threonyl)adenylate (molecule.ecocyc.CPD-9994). Products: AMP (molecule.C00020), H+ (molecule.C00080).

## Annotation

CPD-9994 + THR-tRNAs -> Charged-THR-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-9994|molecule.ecocyc.CPD-9994]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23900`

## Notes

CPD-9994 + THR-tRNAs -> Charged-THR-tRNAs + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
