---
entity_id: "reaction.ecocyc.RXN-22618"
entity_type: "reaction"
name: "RXN-22618"
source_database: "EcoCyc"
source_id: "RXN-22618"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22618

`reaction.ecocyc.RXN-22618`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22618`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HYDROGEN-PEROXIDE + 1-Cys-Peroxiredoxin-L-cysteine -> 1-Cys-Peroxiredoxin-L-hydroxycysteine + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: HYDROGEN-PEROXIDE + 1-Cys-Peroxiredoxin-L-cysteine -> 1-Cys-Peroxiredoxin-L-hydroxycysteine + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Hydrogen peroxide (molecule.C00027), a [1-Cys-peroxiredoxin]-L-cysteine (molecule.ecocyc.1-Cys-Peroxiredoxin-L-cysteine). Products: H2O (molecule.C00001), a [1-Cys-peroxiredoxin]-S-hydroxy-L-cysteine (molecule.ecocyc.1-Cys-Peroxiredoxin-L-hydroxycysteine).

## Annotation

HYDROGEN-PEROXIDE + 1-Cys-Peroxiredoxin-L-cysteine -> 1-Cys-Peroxiredoxin-L-hydroxycysteine + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.1-Cys-Peroxiredoxin-L-hydroxycysteine|molecule.ecocyc.1-Cys-Peroxiredoxin-L-hydroxycysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.1-Cys-Peroxiredoxin-L-cysteine|molecule.ecocyc.1-Cys-Peroxiredoxin-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22618`

## Notes

HYDROGEN-PEROXIDE + 1-Cys-Peroxiredoxin-L-cysteine -> 1-Cys-Peroxiredoxin-L-hydroxycysteine + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
