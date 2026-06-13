---
entity_id: "reaction.ecocyc.RXN-18241"
entity_type: "reaction"
name: "RXN-18241"
source_database: "EcoCyc"
source_id: "RXN-18241"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18241

`reaction.ecocyc.RXN-18241`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18241`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

CPD-606 + WATER -> CYTIDINE + Pi + GLYCEROL-3P + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-606 + WATER -> CYTIDINE + Pi + GLYCEROL-3P + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ushA (protein.P07024). Substrates: H2O (molecule.C00001), CDP-glycerol (molecule.C00513). Products: H+ (molecule.C00080), sn-Glycerol 3-phosphate (molecule.C00093), Cytidine (molecule.C00475), phosphate (molecule.ecocyc.Pi).

## Annotation

CPD-606 + WATER -> CYTIDINE + Pi + GLYCEROL-3P + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P07024|protein.P07024]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00093|molecule.C00093]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00475|molecule.C00475]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00513|molecule.C00513]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18241`

## Notes

CPD-606 + WATER -> CYTIDINE + Pi + GLYCEROL-3P + PROTON; direction=LEFT-TO-RIGHT
