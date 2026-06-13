---
entity_id: "reaction.ecocyc.RXN-14722"
entity_type: "reaction"
name: "RXN-14722"
source_database: "EcoCyc"
source_id: "RXN-14722"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14722

`reaction.ecocyc.RXN-14722`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14722`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

CPD-13211 + WATER -> P-NITROPHENOL + Glucopyranose + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-13211 + WATER -> P-NITROPHENOL + Glucopyranose + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by bglX (protein.P33363). Substrates: H2O (molecule.C00001), 4-nitrophenyl-β-D-glucopyranoside (molecule.ecocyc.CPD-13211). Products: D-Glucose (molecule.C00031), H+ (molecule.C00080), 4-Nitrophenol (molecule.C00870).

## Annotation

CPD-13211 + WATER -> P-NITROPHENOL + Glucopyranose + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P33363|protein.P33363]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00870|molecule.C00870]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-13211|molecule.ecocyc.CPD-13211]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00124|molecule.C00124]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-14722`

## Notes

CPD-13211 + WATER -> P-NITROPHENOL + Glucopyranose + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
