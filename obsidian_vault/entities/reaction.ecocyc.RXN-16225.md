---
entity_id: "reaction.ecocyc.RXN-16225"
entity_type: "reaction"
name: "RXN-16225"
source_database: "EcoCyc"
source_id: "RXN-16225"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16225

`reaction.ecocyc.RXN-16225`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16225`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

2-Acylglycero-Phosphocholines + WATER -> Carboxylates + L-1-GLYCERO-PHOSPHORYLCHOLINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 2-Acylglycero-Phosphocholines + WATER -> Carboxylates + L-1-GLYCERO-PHOSPHORYLCHOLINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), 2-Acyl-sn-glycero-3-phosphocholine (molecule.C04233). Products: H+ (molecule.C00080), sn-Glycero-3-phosphocholine (molecule.C00670), a carboxylate (molecule.ecocyc.Carboxylates).

## Annotation

2-Acylglycero-Phosphocholines + WATER -> Carboxylates + L-1-GLYCERO-PHOSPHORYLCHOLINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00670|molecule.C00670]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Carboxylates|molecule.ecocyc.Carboxylates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04233|molecule.C04233]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16225`

## Notes

2-Acylglycero-Phosphocholines + WATER -> Carboxylates + L-1-GLYCERO-PHOSPHORYLCHOLINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
