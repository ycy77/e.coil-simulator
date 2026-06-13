---
entity_id: "reaction.ecocyc.ACYLPHOSPHATASE-RXN"
entity_type: "reaction"
name: "ACYLPHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "ACYLPHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Acylphosphate phosphohydrolase"
---

# ACYLPHOSPHATASE-RXN

`reaction.ecocyc.ACYLPHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACYLPHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + Acyl-Phosphates -> Pi + Carboxylates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + Acyl-Phosphates -> Pi + Carboxylates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yccX (protein.P0AB65). Substrates: H2O (molecule.C00001), Acyl phosphate (molecule.C02133). Products: H+ (molecule.C00080), a carboxylate (molecule.ecocyc.Carboxylates), phosphate (molecule.ecocyc.Pi).

## Annotation

WATER + Acyl-Phosphates -> Pi + Carboxylates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AB65|protein.P0AB65]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Carboxylates|molecule.ecocyc.Carboxylates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02133|molecule.C02133]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ACYLPHOSPHATASE-RXN`

## Notes

WATER + Acyl-Phosphates -> Pi + Carboxylates + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
