---
entity_id: "reaction.ecocyc.LYSOPHOSPHOLIPASE-RXN"
entity_type: "reaction"
name: "LYSOPHOSPHOLIPASE-RXN"
source_database: "EcoCyc"
source_id: "LYSOPHOSPHOLIPASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "PHOSPHOLIPASE B"
  - "LYSOLECITHINASE"
  - "LECITHINASE B"
---

# LYSOPHOSPHOLIPASE-RXN

`reaction.ecocyc.LYSOPHOSPHOLIPASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LYSOPHOSPHOLIPASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

2-Lysophosphatidylcholines + WATER -> Carboxylates + L-1-GLYCERO-PHOSPHORYLCHOLINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 2-Lysophosphatidylcholines + WATER -> Carboxylates + L-1-GLYCERO-PHOSPHORYLCHOLINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by multifunctional acyl-CoA thioesterase I and protease I and lysophospholipase L1 (complex.ecocyc.CPLX0-7630). Substrates: H2O (molecule.C00001), 1-Acyl-sn-glycero-3-phosphocholine (molecule.C04230). Products: H+ (molecule.C00080), sn-Glycero-3-phosphocholine (molecule.C00670), a carboxylate (molecule.ecocyc.Carboxylates).

## Annotation

2-Lysophosphatidylcholines + WATER -> Carboxylates + L-1-GLYCERO-PHOSPHORYLCHOLINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7630|complex.ecocyc.CPLX0-7630]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00670|molecule.C00670]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Carboxylates|molecule.ecocyc.Carboxylates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04230|molecule.C04230]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.DIISOPROPYL-FLUOROPHOSPHATE|molecule.ecocyc.DIISOPROPYL-FLUOROPHOSPHATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:LYSOPHOSPHOLIPASE-RXN`

## Notes

2-Lysophosphatidylcholines + WATER -> Carboxylates + L-1-GLYCERO-PHOSPHORYLCHOLINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
