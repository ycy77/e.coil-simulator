---
entity_id: "reaction.ecocyc.RXN0-7046"
entity_type: "reaction"
name: "RXN0-7046"
source_database: "EcoCyc"
source_id: "RXN0-7046"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7046

`reaction.ecocyc.RXN0-7046`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7046`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-264 + WATER -> 3-HYDROXYBENZOATE + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-264 + WATER -> 3-HYDROXYBENZOATE + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by proofreading thioesterase in enterobactin biosynthesis (complex.ecocyc.CPLX0-7766). Substrates: H2O (molecule.C00001), 3-hydroxybenzoyl-CoA (molecule.ecocyc.CPD-264). Products: CoA (molecule.C00010), H+ (molecule.C00080), 3-Hydroxybenzoate (molecule.C00587).

## Annotation

CPD-264 + WATER -> 3-HYDROXYBENZOATE + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7766|complex.ecocyc.CPLX0-7766]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00587|molecule.C00587]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-264|molecule.ecocyc.CPD-264]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7046`

## Notes

CPD-264 + WATER -> 3-HYDROXYBENZOATE + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
