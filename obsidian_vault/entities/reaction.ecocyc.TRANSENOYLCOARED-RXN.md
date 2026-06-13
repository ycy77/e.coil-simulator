---
entity_id: "reaction.ecocyc.TRANSENOYLCOARED-RXN"
entity_type: "reaction"
name: "TRANSENOYLCOARED-RXN"
source_database: "EcoCyc"
source_id: "TRANSENOYLCOARED-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANSENOYLCOARED-RXN

`reaction.ecocyc.TRANSENOYLCOARED-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANSENOYLCOARED-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction may participate in the chain elongation or degradation of fatty acids. EcoCyc reaction equation: Saturated-Fatty-Acyl-CoA + NADP -> TRANS-D2-ENOYL-COA + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction may participate in the chain elongation or degradation of fatty acids.

## Biological Role

Catalyzed by trans-2-enoyl-CoA reductase (complex.ecocyc.TRANSENOYLCOARED-CPLX). Substrates: NADP+ (molecule.C00006), a 2,3,4-saturated fatty acyl CoA (molecule.ecocyc.Saturated-Fatty-Acyl-CoA). Products: NADPH (molecule.C00005), H+ (molecule.C00080), a (2E)-2-enoyl-CoA (molecule.ecocyc.TRANS-D2-ENOYL-COA).

## Annotation

This reaction may participate in the chain elongation or degradation of fatty acids.

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.TRANSENOYLCOARED-CPLX|complex.ecocyc.TRANSENOYLCOARED-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.TRANS-D2-ENOYL-COA|molecule.ecocyc.TRANS-D2-ENOYL-COA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Saturated-Fatty-Acyl-CoA|molecule.ecocyc.Saturated-Fatty-Acyl-CoA]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Saturated-Fatty-Acyl-CoA|molecule.ecocyc.Saturated-Fatty-Acyl-CoA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANSENOYLCOARED-RXN`

## Notes

Saturated-Fatty-Acyl-CoA + NADP -> TRANS-D2-ENOYL-COA + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
