---
entity_id: "reaction.ecocyc.RXN-16001"
entity_type: "reaction"
name: "RXN-16001"
source_database: "EcoCyc"
source_id: "RXN-16001"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16001

`reaction.ecocyc.RXN-16001`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16001`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-ALLO-THREONINE + NADP -> AMINO-ACETONE + CARBON-DIOXIDE + NADPH; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-ALLO-THREONINE + NADP -> AMINO-ACETONE + CARBON-DIOXIDE + NADPH; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: NADP+ (molecule.C00006), L-Allothreonine (molecule.C05519). Products: NADPH (molecule.C00005), CO2 (molecule.C00011), Aminoacetone (molecule.C01888).

## Annotation

L-ALLO-THREONINE + NADP -> AMINO-ACETONE + CARBON-DIOXIDE + NADPH; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01888|molecule.C01888]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05519|molecule.C05519]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16001`

## Notes

L-ALLO-THREONINE + NADP -> AMINO-ACETONE + CARBON-DIOXIDE + NADPH; direction=PHYSIOL-LEFT-TO-RIGHT
