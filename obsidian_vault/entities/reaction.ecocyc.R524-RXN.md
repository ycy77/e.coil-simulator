---
entity_id: "reaction.ecocyc.R524-RXN"
entity_type: "reaction"
name: "R524-RXN"
source_database: "EcoCyc"
source_id: "R524-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Cyanate hydrolase"
  - "Cyanase"
  - "Cyanate aminohydrolase"
---

# R524-RXN

`reaction.ecocyc.R524-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:R524-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-69 + HCO3 + PROTON -> CARBAMATE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-69 + HCO3 + PROTON -> CARBAMATE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by cyanase (complex.ecocyc.CYANLY-CPLX). Substrates: H+ (molecule.C00080), HCO3- (molecule.C00288), Cyanate (molecule.C01417). Products: CO2 (molecule.C00011), Carbamate (molecule.C01563).

## Enriched Pathways

- `ecocyc.CYANCAT-PWY` cyanate degradation (EcoCyc)

## Annotation

CPD-69 + HCO3 + PROTON -> CARBAMATE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.CYANCAT-PWY` cyanate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (16)

- `catalyzes` <-- [[complex.ecocyc.CYANLY-CPLX|complex.ecocyc.CYANLY-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01563|molecule.C01563]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01417|molecule.C01417]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00088|molecule.C00088]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00209|molecule.C00209]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00244|molecule.C00244]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00288|molecule.C00288]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01417|molecule.C01417]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.BR-|molecule.ecocyc.BR-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CL-|molecule.ecocyc.CL-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-2841|molecule.ecocyc.CPD-2841]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:R524-RXN`

## Notes

CPD-69 + HCO3 + PROTON -> CARBAMATE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
