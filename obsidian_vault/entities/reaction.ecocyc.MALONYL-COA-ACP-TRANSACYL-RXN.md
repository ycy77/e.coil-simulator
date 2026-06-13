---
entity_id: "reaction.ecocyc.MALONYL-COA-ACP-TRANSACYL-RXN"
entity_type: "reaction"
name: "MALONYL-COA-ACP-TRANSACYL-RXN"
source_database: "EcoCyc"
source_id: "MALONYL-COA-ACP-TRANSACYL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MALONYL-COA-ACP-TRANSACYL-RXN

`reaction.ecocyc.MALONYL-COA-ACP-TRANSACYL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MALONYL-COA-ACP-TRANSACYL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction prepares malonate for use in the biosynthesis of fatty acids. The energy-rich bonds in acyl-CoAs and acyl-ACPs are identical. EcoCyc reaction equation: ACP + MALONYL-COA -> MALONYL-ACP + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction prepares malonate for use in the biosynthesis of fatty acids. The energy-rich bonds in acyl-CoAs and acyl-ACPs are identical.

## Biological Role

Catalyzed by fabD (protein.P0AAI9). Substrates: Malonyl-CoA (molecule.C00083). Products: CoA (molecule.C00010).

## Enriched Pathways

- `ecocyc.PWY-4381` fatty acid biosynthesis initiation (type II) (EcoCyc)

## Annotation

This reaction prepares malonate for use in the biosynthesis of fatty acids. The energy-rich bonds in acyl-CoAs and acyl-ACPs are identical.

## Pathways

- `ecocyc.PWY-4381` fatty acid biosynthesis initiation (type II) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0AAI9|protein.P0AAI9]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00083|molecule.C00083]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETAMIDE|molecule.ecocyc.IODOACETAMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:MALONYL-COA-ACP-TRANSACYL-RXN`

## Notes

ACP + MALONYL-COA -> MALONYL-ACP + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
