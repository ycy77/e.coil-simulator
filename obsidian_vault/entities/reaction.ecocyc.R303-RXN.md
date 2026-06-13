---
entity_id: "reaction.ecocyc.R303-RXN"
entity_type: "reaction"
name: "R303-RXN"
source_database: "EcoCyc"
source_id: "R303-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# R303-RXN

`reaction.ecocyc.R303-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:R303-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Hydroxylaminoaromatic-Compounds + NADP + WATER -> Nitroaromatic-Compounds + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: Hydroxylaminoaromatic-Compounds + NADP + WATER -> Nitroaromatic-Compounds + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by NADPH-dependent nitroreductase / NADPH-dependent quinone reductase (complex.ecocyc.CPLX0-244). Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006), a hydroxylaminoaromatic compound (molecule.ecocyc.Hydroxylaminoaromatic-Compounds). Products: NADPH (molecule.C00005), H+ (molecule.C00080), a nitroaromatic compound (molecule.ecocyc.Nitroaromatic-Compounds).

## Annotation

Hydroxylaminoaromatic-Compounds + NADP + WATER -> Nitroaromatic-Compounds + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-244|complex.ecocyc.CPLX0-244]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Nitroaromatic-Compounds|molecule.ecocyc.Nitroaromatic-Compounds]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hydroxylaminoaromatic-Compounds|molecule.ecocyc.Hydroxylaminoaromatic-Compounds]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-14493|molecule.ecocyc.CPD-14493]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-17769|molecule.ecocyc.CPD-17769]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DICOUMAROL|molecule.ecocyc.DICOUMAROL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:R303-RXN`

## Notes

Hydroxylaminoaromatic-Compounds + NADP + WATER -> Nitroaromatic-Compounds + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
