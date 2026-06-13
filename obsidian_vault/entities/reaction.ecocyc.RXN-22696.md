---
entity_id: "reaction.ecocyc.RXN-22696"
entity_type: "reaction"
name: "RXN-22696"
source_database: "EcoCyc"
source_id: "RXN-22696"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22696

`reaction.ecocyc.RXN-22696`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22696`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Cysteine-Desulfurase-S-sulfinato-Cys + WATER -> Cysteine-Desulfurase-L-cysteine + SO3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-Cysteine-Desulfurase-S-sulfinato-Cys + WATER -> Cysteine-Desulfurase-L-cysteine + SO3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), an [L-cysteine desulfurase]-S-sulfinato-L-cysteine (molecule.ecocyc.L-Cysteine-Desulfurase-S-sulfinato-Cys). Products: H+ (molecule.C00080), Sulfite (molecule.C00094), an [L-cysteine desulfurase]-L-cysteine (molecule.ecocyc.Cysteine-Desulfurase-L-cysteine).

## Annotation

L-Cysteine-Desulfurase-S-sulfinato-Cys + WATER -> Cysteine-Desulfurase-L-cysteine + SO3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Cysteine-Desulfurase-L-cysteine|molecule.ecocyc.Cysteine-Desulfurase-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.L-Cysteine-Desulfurase-S-sulfinato-Cys|molecule.ecocyc.L-Cysteine-Desulfurase-S-sulfinato-Cys]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22696`

## Notes

L-Cysteine-Desulfurase-S-sulfinato-Cys + WATER -> Cysteine-Desulfurase-L-cysteine + SO3 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
