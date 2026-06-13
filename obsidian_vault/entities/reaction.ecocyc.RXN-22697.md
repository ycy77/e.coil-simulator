---
entity_id: "reaction.ecocyc.RXN-22697"
entity_type: "reaction"
name: "RXN-22697"
source_database: "EcoCyc"
source_id: "RXN-22697"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22697

`reaction.ecocyc.RXN-22697`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22697`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Cysteine-Desulfurase-persulfide + MOCS3-Cysteine -> Cysteine-Desulfurase-L-cysteine + MOCS3-Cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-Cysteine-Desulfurase-persulfide + MOCS3-Cysteine -> Cysteine-Desulfurase-L-cysteine + MOCS3-Cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: an [L-cysteine desulfurase]-S-sulfanyl-L-cysteine (molecule.ecocyc.L-Cysteine-Desulfurase-persulfide), a [molybdopterin synthase sulfurtransferase]-L-cysteine (molecule.ecocyc.MOCS3-Cysteine). Products: an [L-cysteine desulfurase]-L-cysteine (molecule.ecocyc.Cysteine-Desulfurase-L-cysteine), a [molybdopterin synthase sulfurtransferase]-S-sulfanyl-L-cysteine (molecule.ecocyc.MOCS3-Cysteine-Persulfide).

## Annotation

L-Cysteine-Desulfurase-persulfide + MOCS3-Cysteine -> Cysteine-Desulfurase-L-cysteine + MOCS3-Cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.ecocyc.Cysteine-Desulfurase-L-cysteine|molecule.ecocyc.Cysteine-Desulfurase-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MOCS3-Cysteine-Persulfide|molecule.ecocyc.MOCS3-Cysteine-Persulfide]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.L-Cysteine-Desulfurase-persulfide|molecule.ecocyc.L-Cysteine-Desulfurase-persulfide]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MOCS3-Cysteine|molecule.ecocyc.MOCS3-Cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22697`

## Notes

L-Cysteine-Desulfurase-persulfide + MOCS3-Cysteine -> Cysteine-Desulfurase-L-cysteine + MOCS3-Cysteine-Persulfide; direction=PHYSIOL-LEFT-TO-RIGHT
