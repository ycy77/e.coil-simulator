---
entity_id: "reaction.ecocyc.RXN-24048"
entity_type: "reaction"
name: "RXN-24048"
source_database: "EcoCyc"
source_id: "RXN-24048"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24048

`reaction.ecocyc.RXN-24048`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24048`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Nitrosoaromatic-Compounds + NADP + WATER -> Nitroaromatic-Compounds + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: Nitrosoaromatic-Compounds + NADP + WATER -> Nitroaromatic-Compounds + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006), a nitrosoaromatic compound (molecule.ecocyc.Nitrosoaromatic-Compounds). Products: NADPH (molecule.C00005), H+ (molecule.C00080), a nitroaromatic compound (molecule.ecocyc.Nitroaromatic-Compounds).

## Annotation

Nitrosoaromatic-Compounds + NADP + WATER -> Nitroaromatic-Compounds + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Nitroaromatic-Compounds|molecule.ecocyc.Nitroaromatic-Compounds]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Nitrosoaromatic-Compounds|molecule.ecocyc.Nitrosoaromatic-Compounds]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24048`

## Notes

Nitrosoaromatic-Compounds + NADP + WATER -> Nitroaromatic-Compounds + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
