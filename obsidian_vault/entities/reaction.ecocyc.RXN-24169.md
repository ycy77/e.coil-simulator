---
entity_id: "reaction.ecocyc.RXN-24169"
entity_type: "reaction"
name: "RXN-24169"
source_database: "EcoCyc"
source_id: "RXN-24169"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24169

`reaction.ecocyc.RXN-24169`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24169`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

CPD-9115 + WATER -> CPD-258 + D-galactopyranose + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-9115 + WATER -> CPD-258 + D-galactopyranose + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by β-galactosidase (complex.ecocyc.BETAGALACTOSID-CPLX), bglX (protein.P33363). Substrates: H2O (molecule.C00001), 2-nitrophenyl β-D-galactoside (molecule.ecocyc.CPD-9115). Products: H+ (molecule.C00080), D-Galactose (molecule.C00124), 2-nitrophenol (molecule.ecocyc.CPD-258).

## Annotation

CPD-9115 + WATER -> CPD-258 + D-galactopyranose + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.BETAGALACTOSID-CPLX|complex.ecocyc.BETAGALACTOSID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P33363|protein.P33363]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00124|molecule.C00124]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-258|molecule.ecocyc.CPD-258]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-9115|molecule.ecocyc.CPD-9115]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00124|molecule.C00124]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-24169`

## Notes

CPD-9115 + WATER -> CPD-258 + D-galactopyranose + PROTON; direction=LEFT-TO-RIGHT
