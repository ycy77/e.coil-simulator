---
entity_id: "reaction.ecocyc.RXN-13853"
entity_type: "reaction"
name: "RXN-13853"
source_database: "EcoCyc"
source_id: "RXN-13853"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13853

`reaction.ecocyc.RXN-13853`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13853`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Hydroxylaminoaromatic-Compounds + NAD-P-OR-NOP + WATER -> Nitroaromatic-Compounds + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: Hydroxylaminoaromatic-Compounds + NAD-P-OR-NOP + WATER -> Nitroaromatic-Compounds + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by NAD(P)H-dependent nitroreductase NfsB (complex.ecocyc.DIHYDROPTERIREDUCT-CPLX). Substrates: H2O (molecule.C00001), a hydroxylaminoaromatic compound (molecule.ecocyc.Hydroxylaminoaromatic-Compounds), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP), a nitroaromatic compound (molecule.ecocyc.Nitroaromatic-Compounds).

## Annotation

Hydroxylaminoaromatic-Compounds + NAD-P-OR-NOP + WATER -> Nitroaromatic-Compounds + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.DIHYDROPTERIREDUCT-CPLX|complex.ecocyc.DIHYDROPTERIREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Nitroaromatic-Compounds|molecule.ecocyc.Nitroaromatic-Compounds]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hydroxylaminoaromatic-Compounds|molecule.ecocyc.Hydroxylaminoaromatic-Compounds]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13853`

## Notes

Hydroxylaminoaromatic-Compounds + NAD-P-OR-NOP + WATER -> Nitroaromatic-Compounds + NADH-P-OR-NOP + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
