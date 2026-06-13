---
entity_id: "reaction.ecocyc.RXN0-6725"
entity_type: "reaction"
name: "RXN0-6725"
source_database: "EcoCyc"
source_id: "RXN0-6725"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6725

`reaction.ecocyc.RXN0-6725`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6725`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

L-1-PHOSPHATIDYL-ETHANOLAMINE + WATER -> Fatty-Acids + 2-LYSOPHOSPHATIDYLETHANOLAMINES + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-1-PHOSPHATIDYL-ETHANOLAMINE + WATER -> Fatty-Acids + 2-LYSOPHOSPHATIDYLETHANOLAMINES + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by outer membrane phospholipase A (complex.ecocyc.CPLX0-7944). Substrates: H2O (molecule.C00001), Phosphatidylethanolamine (molecule.C00350). Products: H+ (molecule.C00080), Fatty acid (molecule.C00162), a 2-lysophosphatidylethanolamine (molecule.ecocyc.2-LYSOPHOSPHATIDYLETHANOLAMINES).

## Annotation

L-1-PHOSPHATIDYL-ETHANOLAMINE + WATER -> Fatty-Acids + 2-LYSOPHOSPHATIDYLETHANOLAMINES + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7944|complex.ecocyc.CPLX0-7944]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00162|molecule.C00162]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.2-LYSOPHOSPHATIDYLETHANOLAMINES|molecule.ecocyc.2-LYSOPHOSPHATIDYLETHANOLAMINES]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00350|molecule.C00350]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6725`

## Notes

L-1-PHOSPHATIDYL-ETHANOLAMINE + WATER -> Fatty-Acids + 2-LYSOPHOSPHATIDYLETHANOLAMINES + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
