---
entity_id: "reaction.ecocyc.RXN-12896"
entity_type: "reaction"
name: "RXN-12896"
source_database: "EcoCyc"
source_id: "RXN-12896"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12896

`reaction.ecocyc.RXN-12896`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12896`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-22331 + WATER -> CPD-22332 + CARBAMATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-22331 + WATER -> CPD-22332 + CARBAMATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rutB (protein.P75897). Substrates: H2O (molecule.C00001), (Z)-2-methylureidoacrylate (molecule.ecocyc.CPD-22331). Products: H+ (molecule.C00080), Carbamate (molecule.C01563), (Z)-2-methylaminoacrylate (molecule.ecocyc.CPD-22332).

## Annotation

CPD-22331 + WATER -> CPD-22332 + CARBAMATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P75897|protein.P75897]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01563|molecule.C01563]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-22332|molecule.ecocyc.CPD-22332]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-22331|molecule.ecocyc.CPD-22331]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12896`

## Notes

CPD-22331 + WATER -> CPD-22332 + CARBAMATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
