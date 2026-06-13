---
entity_id: "reaction.ecocyc.RXN-24170"
entity_type: "reaction"
name: "RXN-24170"
source_database: "EcoCyc"
source_id: "RXN-24170"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24170

`reaction.ecocyc.RXN-24170`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24170`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

CPD-21655 + WATER -> CPD-258 + Glucopyranose + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-21655 + WATER -> CPD-258 + Glucopyranose + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by bglX (protein.P33363). Substrates: H2O (molecule.C00001), 2-nitrophenyl-β-D-glucopyranoside (molecule.ecocyc.CPD-21655). Products: D-Glucose (molecule.C00031), H+ (molecule.C00080), 2-nitrophenol (molecule.ecocyc.CPD-258).

## Annotation

CPD-21655 + WATER -> CPD-258 + Glucopyranose + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P33363|protein.P33363]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-258|molecule.ecocyc.CPD-258]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21655|molecule.ecocyc.CPD-21655]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24170`

## Notes

CPD-21655 + WATER -> CPD-258 + Glucopyranose + PROTON; direction=LEFT-TO-RIGHT
