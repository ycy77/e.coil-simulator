---
entity_id: "reaction.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-RXN"
entity_type: "reaction"
name: "ACETYL-COA-CARBOXYLTRANSFER-RXN"
source_database: "EcoCyc"
source_id: "ACETYL-COA-CARBOXYLTRANSFER-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACETYL-COA-CARBOXYLTRANSFER-RXN

`reaction.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACETYL-COA-CARBOXYLTRANSFER-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + ACETYL-COA + HCO3 -> ADP + Pi + MALONYL-COA + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + ACETYL-COA + HCO3 -> ADP + Pi + MALONYL-COA + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), Acetyl-CoA (molecule.C00024), HCO3- (molecule.C00288). Products: ADP (molecule.C00008), H+ (molecule.C00080), Malonyl-CoA (molecule.C00083), phosphate (molecule.ecocyc.Pi).

## Annotation

ATP + ACETYL-COA + HCO3 -> ADP + Pi + MALONYL-COA + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00083|molecule.C00083]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ACETYL-COA-CARBOXYLTRANSFER-RXN`

## Notes

ATP + ACETYL-COA + HCO3 -> ADP + Pi + MALONYL-COA + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
