---
entity_id: "reaction.ecocyc.ACECOATRANS-RXN"
entity_type: "reaction"
name: "ACECOATRANS-RXN"
source_database: "EcoCyc"
source_id: "ACECOATRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACECOATRANS-RXN

`reaction.ecocyc.ACECOATRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACECOATRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction functions as an activating mechanism allowing fatty acids to function as carbon sources for growth. In catabolism of fatty acids, the fatty acids are first activated with CoA. EcoCyc reaction equation: Saturated-Fatty-Acyl-CoA + ACET -> CPD66-39 + ACETYL-COA; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction functions as an activating mechanism allowing fatty acids to function as carbon sources for growth. In catabolism of fatty acids, the fatty acids are first activated with CoA.

## Biological Role

Catalyzed by ACECOATRANS-MONOMER (protein.ecocyc.ACECOATRANS-MONOMER). Substrates: Acetate (molecule.C00033), a 2,3,4-saturated fatty acyl CoA (molecule.ecocyc.Saturated-Fatty-Acyl-CoA). Products: Acetyl-CoA (molecule.C00024), a 2,3,4-saturated fatty acid (molecule.ecocyc.CPD66-39).

## Annotation

This reaction functions as an activating mechanism allowing fatty acids to function as carbon sources for growth. In catabolism of fatty acids, the fatty acids are first activated with CoA.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.ecocyc.ACECOATRANS-MONOMER|protein.ecocyc.ACECOATRANS-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD66-39|molecule.ecocyc.CPD66-39]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Saturated-Fatty-Acyl-CoA|molecule.ecocyc.Saturated-Fatty-Acyl-CoA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ACECOATRANS-RXN`

## Notes

Saturated-Fatty-Acyl-CoA + ACET -> CPD66-39 + ACETYL-COA; direction=PHYSIOL-LEFT-TO-RIGHT
