---
entity_id: "reaction.ecocyc.RXN-23946"
entity_type: "reaction"
name: "RXN-23946"
source_database: "EcoCyc"
source_id: "RXN-23946"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23946

`reaction.ecocyc.RXN-23946`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23946`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SERYL-AMP + THR-tRNAs -> Seryl-tRNAThr + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: SERYL-AMP + THR-tRNAs -> Seryl-tRNAThr + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: (L-seryl)adenylate (molecule.ecocyc.SERYL-AMP). Products: AMP (molecule.C00020), H+ (molecule.C00080).

## Annotation

SERYL-AMP + THR-tRNAs -> Seryl-tRNAThr + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.SERYL-AMP|molecule.ecocyc.SERYL-AMP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23946`

## Notes

SERYL-AMP + THR-tRNAs -> Seryl-tRNAThr + AMP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
