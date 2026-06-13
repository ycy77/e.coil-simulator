---
entity_id: "reaction.ecocyc.RXN-24049"
entity_type: "reaction"
name: "RXN-24049"
source_database: "EcoCyc"
source_id: "RXN-24049"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24049

`reaction.ecocyc.RXN-24049`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24049`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Hydroxylaminoaromatic-Compounds + NADP -> Nitrosoaromatic-Compounds + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: Hydroxylaminoaromatic-Compounds + NADP -> Nitrosoaromatic-Compounds + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Substrates: NADP+ (molecule.C00006), a hydroxylaminoaromatic compound (molecule.ecocyc.Hydroxylaminoaromatic-Compounds). Products: NADPH (molecule.C00005), H+ (molecule.C00080), a nitrosoaromatic compound (molecule.ecocyc.Nitrosoaromatic-Compounds).

## Annotation

Hydroxylaminoaromatic-Compounds + NADP -> Nitrosoaromatic-Compounds + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Nitrosoaromatic-Compounds|molecule.ecocyc.Nitrosoaromatic-Compounds]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Hydroxylaminoaromatic-Compounds|molecule.ecocyc.Hydroxylaminoaromatic-Compounds]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24049`

## Notes

Hydroxylaminoaromatic-Compounds + NADP -> Nitrosoaromatic-Compounds + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
