---
entity_id: "reaction.ecocyc.RXN-21270"
entity_type: "reaction"
name: "RXN-21270"
source_database: "EcoCyc"
source_id: "RXN-21270"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21270

`reaction.ecocyc.RXN-21270`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21270`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-11648 + WATER -> CYTIDINE + ACET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-11648 + WATER -> CYTIDINE + ACET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yqfB (protein.P67603). Substrates: H2O (molecule.C00001), N4-acetylcytidine (molecule.ecocyc.CPD-11648). Products: Acetate (molecule.C00033), H+ (molecule.C00080), Cytidine (molecule.C00475).

## Annotation

CPD-11648 + WATER -> CYTIDINE + ACET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P67603|protein.P67603]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00475|molecule.C00475]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-11648|molecule.ecocyc.CPD-11648]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21270`

## Notes

CPD-11648 + WATER -> CYTIDINE + ACET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
