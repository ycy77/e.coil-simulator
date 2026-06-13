---
entity_id: "reaction.ecocyc.DIENOYLCOAREDUCT-RXN"
entity_type: "reaction"
name: "DIENOYLCOAREDUCT-RXN"
source_database: "EcoCyc"
source_id: "DIENOYLCOAREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIENOYLCOAREDUCT-RXN

`reaction.ecocyc.DIENOYLCOAREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIENOYLCOAREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is a part of the β-oxidation of unsaturated fatty acids. EcoCyc reaction equation: T2-DECENOYL-COA + NADP -> PROTON + T2-C4-DECADIENYL-COA + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction is a part of the β-oxidation of unsaturated fatty acids.

## Biological Role

Catalyzed by fadH (protein.P42593). Substrates: NADP+ (molecule.C00006), trans-Dec-2-enoyl-CoA (molecule.C05275). Products: NADPH (molecule.C00005), H+ (molecule.C00080), (2E,4Z)-deca-2,4-dienoyl-CoA (molecule.ecocyc.T2-C4-DECADIENYL-COA).

## Annotation

This reaction is a part of the β-oxidation of unsaturated fatty acids.

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P42593|protein.P42593]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.T2-C4-DECADIENYL-COA|molecule.ecocyc.T2-C4-DECADIENYL-COA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05275|molecule.C05275]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.T2-C4-DECADIENYL-COA|molecule.ecocyc.T2-C4-DECADIENYL-COA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DIENOYLCOAREDUCT-RXN`

## Notes

T2-DECENOYL-COA + NADP -> PROTON + T2-C4-DECADIENYL-COA + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT
