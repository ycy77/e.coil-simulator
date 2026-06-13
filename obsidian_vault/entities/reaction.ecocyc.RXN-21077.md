---
entity_id: "reaction.ecocyc.RXN-21077"
entity_type: "reaction"
name: "RXN-21077"
source_database: "EcoCyc"
source_id: "RXN-21077"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21077

`reaction.ecocyc.RXN-21077`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21077`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Cys-tRNA-Pro + WATER -> PRO-tRNAs + CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Cys-tRNA-Pro + WATER -> PRO-tRNAs + CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ybaK (protein.P0AAR3). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), L-Cysteine (molecule.C00097).

## Annotation

Cys-tRNA-Pro + WATER -> PRO-tRNAs + CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0AAR3|protein.P0AAR3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21077`

## Notes

Cys-tRNA-Pro + WATER -> PRO-tRNAs + CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
