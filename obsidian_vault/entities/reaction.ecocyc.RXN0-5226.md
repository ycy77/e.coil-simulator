---
entity_id: "reaction.ecocyc.RXN0-5226"
entity_type: "reaction"
name: "RXN0-5226"
source_database: "EcoCyc"
source_id: "RXN0-5226"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5226

`reaction.ecocyc.RXN0-5226`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5226`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1081 + WATER -> N-acetyl-D-glucosamine + CPD0-882; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1081 + WATER -> N-acetyl-D-glucosamine + CPD0-882; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nagZ (protein.P75949). Substrates: H2O (molecule.C00001), N-acetyl-β-D-glucosamine-1,6-anhydro-N-acetyl-β-D-muramate (molecule.ecocyc.CPD0-1081). Products: N-Acetyl-D-glucosamine (molecule.C00140), 1,6-Anhydro-N-acetyl-beta-muramate (molecule.C19769).

## Enriched Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Annotation

CPD0-1081 + WATER -> N-acetyl-D-glucosamine + CPD0-882; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P75949|protein.P75949]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00140|molecule.C00140]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C19769|molecule.C19769]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1081|molecule.ecocyc.CPD0-1081]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C02713|molecule.C02713]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1512|molecule.ecocyc.CPD0-1512]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1888|molecule.ecocyc.CPD0-1888]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ACETYL-BETA-D-GLUCOSAMINE|molecule.ecocyc.N-ACETYL-BETA-D-GLUCOSAMINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5226`

## Notes

CPD0-1081 + WATER -> N-acetyl-D-glucosamine + CPD0-882; direction=PHYSIOL-LEFT-TO-RIGHT
