---
entity_id: "reaction.ecocyc.RXN-12618"
entity_type: "reaction"
name: "RXN-12618"
source_database: "EcoCyc"
source_id: "RXN-12618"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12618

`reaction.ecocyc.RXN-12618`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12618`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

GLUTATHIONE + WATER -> CYS-GLY + GLT; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLUTATHIONE + WATER -> CYS-GLY + GLT; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glutathione hydrolase (complex.ecocyc.CPLX0-7885). Substrates: H2O (molecule.C00001), Glutathione (molecule.C00051). Products: L-Glutamate (molecule.C00025), Cys-Gly (molecule.C01419).

## Annotation

GLUTATHIONE + WATER -> CYS-GLY + GLT; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7885|complex.ecocyc.CPLX0-7885]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01419|molecule.C01419]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12618`

## Notes

GLUTATHIONE + WATER -> CYS-GLY + GLT; direction=PHYSIOL-LEFT-TO-RIGHT
