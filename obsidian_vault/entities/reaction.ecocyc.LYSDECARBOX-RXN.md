---
entity_id: "reaction.ecocyc.LYSDECARBOX-RXN"
entity_type: "reaction"
name: "LYSDECARBOX-RXN"
source_database: "EcoCyc"
source_id: "LYSDECARBOX-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# LYSDECARBOX-RXN

`reaction.ecocyc.LYSDECARBOX-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LYSDECARBOX-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + LYS -> CARBON-DIOXIDE + CADAVERINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + LYS -> CARBON-DIOXIDE + CADAVERINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lysine decarboxylase 2 (complex.ecocyc.LDC2-CPLX), lysine decarboxylase 1 (complex.ecocyc.LYSDECARBOX-CPLX). Substrates: L-Lysine (molecule.C00047), H+ (molecule.C00080). Products: CO2 (molecule.C00011), Cadaverine (molecule.C01672).

## Enriched Pathways

- `ecocyc.PWY0-1303` aminopropylcadaverine biosynthesis (EcoCyc)
- `ecocyc.PWY0-1601` cadaverine biosynthesis (EcoCyc)
- `ecocyc.PWY0-461` L-lysine degradation I (EcoCyc)

## Annotation

PROTON + LYS -> CARBON-DIOXIDE + CADAVERINE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1303` aminopropylcadaverine biosynthesis (EcoCyc)
- `ecocyc.PWY0-1601` cadaverine biosynthesis (EcoCyc)
- `ecocyc.PWY0-461` L-lysine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.LDC2-CPLX|complex.ecocyc.LDC2-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.LYSDECARBOX-CPLX|complex.ecocyc.LYSDECARBOX-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01672|molecule.C01672]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C02378|molecule.C02378]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C04494|molecule.C04494]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:LYSDECARBOX-RXN`

## Notes

PROTON + LYS -> CARBON-DIOXIDE + CADAVERINE; direction=LEFT-TO-RIGHT
