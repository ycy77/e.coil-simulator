---
entity_id: "reaction.ecocyc.RXN-16000"
entity_type: "reaction"
name: "RXN-16000"
source_database: "EcoCyc"
source_id: "RXN-16000"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16000

`reaction.ecocyc.RXN-16000`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16000`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-ALLO-THREONINE + NADP -> AMINO-OXOBUT + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-ALLO-THREONINE + NADP -> AMINO-OXOBUT + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-hydroxy acid dehydrogenase YdfG (complex.ecocyc.CPLX0-1962). Substrates: NADP+ (molecule.C00006), L-Allothreonine (molecule.C05519). Products: NADPH (molecule.C00005), H+ (molecule.C00080), L-2-Amino-3-oxobutanoic acid (molecule.C03508).

## Annotation

L-ALLO-THREONINE + NADP -> AMINO-OXOBUT + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1962|complex.ecocyc.CPLX0-1962]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03508|molecule.C03508]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05519|molecule.C05519]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16000`

## Notes

L-ALLO-THREONINE + NADP -> AMINO-OXOBUT + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
