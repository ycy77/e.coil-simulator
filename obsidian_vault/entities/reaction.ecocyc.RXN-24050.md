---
entity_id: "reaction.ecocyc.RXN-24050"
entity_type: "reaction"
name: "RXN-24050"
source_database: "EcoCyc"
source_id: "RXN-24050"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24050

`reaction.ecocyc.RXN-24050`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24050`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-24126 + L-1-PHOSPHATIDYL-GLYCEROL + WATER -> CPD-21605 + GLYCEROL + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-24126 + L-1-PHOSPHATIDYL-GLYCEROL + WATER -> CPD-21605 + GLYCEROL + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), Phosphatidylglycerol (molecule.C00344), enterobacterial common antigen (molecule.ecocyc.CPD-24126). Products: H+ (molecule.C00080), Glycerol (molecule.C00116), di-trans,poly-cis-Undecaprenyl diphosphate (molecule.C04574), enterobacterial common antigen-phosphatidylglycerol (molecule.ecocyc.CPD-21605).

## Annotation

CPD-24126 + L-1-PHOSPHATIDYL-GLYCEROL + WATER -> CPD-21605 + GLYCEROL + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00116|molecule.C00116]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04574|molecule.C04574]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21605|molecule.ecocyc.CPD-21605]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00344|molecule.C00344]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-24126|molecule.ecocyc.CPD-24126]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24050`

## Notes

CPD-24126 + L-1-PHOSPHATIDYL-GLYCEROL + WATER -> CPD-21605 + GLYCEROL + UNDECAPRENYL-DIPHOSPHATE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
