---
entity_id: "reaction.ecocyc.RXN-19729"
entity_type: "reaction"
name: "RXN-19729"
source_database: "EcoCyc"
source_id: "RXN-19729"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19729

`reaction.ecocyc.RXN-19729`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19729`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Tryptophanyl-tRNA-Trp + WATER -> D-TRYPTOPHAN + TRP-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-Tryptophanyl-tRNA-Trp + WATER -> D-TRYPTOPHAN + TRP-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by D-aminoacyl-tRNA deacylase (complex.ecocyc.CPLX0-3581). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), D-tryptophan (molecule.ecocyc.D-TRYPTOPHAN).

## Annotation

D-Tryptophanyl-tRNA-Trp + WATER -> D-TRYPTOPHAN + TRP-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3581|complex.ecocyc.CPLX0-3581]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.D-TRYPTOPHAN|molecule.ecocyc.D-TRYPTOPHAN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19729`

## Notes

D-Tryptophanyl-tRNA-Trp + WATER -> D-TRYPTOPHAN + TRP-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
