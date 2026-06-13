---
entity_id: "reaction.ecocyc.RXN-22695"
entity_type: "reaction"
name: "RXN-22695"
source_database: "EcoCyc"
source_id: "RXN-22695"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22695

`reaction.ecocyc.RXN-22695`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22695`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-SULFINOALANINE + Cysteine-Desulfurase-L-cysteine -> L-ALPHA-ALANINE + L-Cysteine-Desulfurase-S-sulfinato-Cys; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 3-SULFINOALANINE + Cysteine-Desulfurase-L-cysteine -> L-ALPHA-ALANINE + L-Cysteine-Desulfurase-S-sulfinato-Cys; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: 3-Sulfino-L-alanine (molecule.C00606), an [L-cysteine desulfurase]-L-cysteine (molecule.ecocyc.Cysteine-Desulfurase-L-cysteine). Products: L-Alanine (molecule.C00041), an [L-cysteine desulfurase]-S-sulfinato-L-cysteine (molecule.ecocyc.L-Cysteine-Desulfurase-S-sulfinato-Cys).

## Annotation

3-SULFINOALANINE + Cysteine-Desulfurase-L-cysteine -> L-ALPHA-ALANINE + L-Cysteine-Desulfurase-S-sulfinato-Cys; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.L-Cysteine-Desulfurase-S-sulfinato-Cys|molecule.ecocyc.L-Cysteine-Desulfurase-S-sulfinato-Cys]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00606|molecule.C00606]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Cysteine-Desulfurase-L-cysteine|molecule.ecocyc.Cysteine-Desulfurase-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22695`

## Notes

3-SULFINOALANINE + Cysteine-Desulfurase-L-cysteine -> L-ALPHA-ALANINE + L-Cysteine-Desulfurase-S-sulfinato-Cys; direction=PHYSIOL-LEFT-TO-RIGHT
