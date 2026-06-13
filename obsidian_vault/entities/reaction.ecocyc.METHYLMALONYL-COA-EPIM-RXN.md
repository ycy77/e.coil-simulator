---
entity_id: "reaction.ecocyc.METHYLMALONYL-COA-EPIM-RXN"
entity_type: "reaction"
name: "METHYLMALONYL-COA-EPIM-RXN"
source_database: "EcoCyc"
source_id: "METHYLMALONYL-COA-EPIM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# METHYLMALONYL-COA-EPIM-RXN

`reaction.ecocyc.METHYLMALONYL-COA-EPIM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:METHYLMALONYL-COA-EPIM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction of the methylmalonyl pathway of propionate metabolism. EcoCyc reaction equation: METHYL-MALONYL-COA -> D-METHYL-MALONYL-COA; direction=REVERSIBLE. This is the second reaction of the methylmalonyl pathway of propionate metabolism.

## Biological Role

Catalyzed by METHYLMALONYL-COA-EPIM-MONOMER (protein.ecocyc.METHYLMALONYL-COA-EPIM-MONOMER). Substrates: (R)-Methylmalonyl-CoA (molecule.C01213). Products: (S)-Methylmalonyl-CoA (molecule.C00683).

## Enriched Pathways

- `ecocyc.PROPIONMET-PWY` propanoyl CoA degradation I (EcoCyc)

## Annotation

This is the second reaction of the methylmalonyl pathway of propionate metabolism.

## Pathways

- `ecocyc.PROPIONMET-PWY` propanoyl CoA degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.ecocyc.METHYLMALONYL-COA-EPIM-MONOMER|protein.ecocyc.METHYLMALONYL-COA-EPIM-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00683|molecule.C00683]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01213|molecule.C01213]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:METHYLMALONYL-COA-EPIM-RXN`

## Notes

METHYL-MALONYL-COA -> D-METHYL-MALONYL-COA; direction=REVERSIBLE
