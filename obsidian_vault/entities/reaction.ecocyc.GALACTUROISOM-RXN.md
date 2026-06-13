---
entity_id: "reaction.ecocyc.GALACTUROISOM-RXN"
entity_type: "reaction"
name: "GALACTUROISOM-RXN"
source_database: "EcoCyc"
source_id: "GALACTUROISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GALACTUROISOM-RXN

`reaction.ecocyc.GALACTUROISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GALACTUROISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of the galacturonate pathway. EcoCyc reaction equation: CPD-15633 -> D-TAGATURONATE; direction=REVERSIBLE. Part of the galacturonate pathway.

## Biological Role

Catalyzed by uxaC (protein.P0A8G3). Substrates: aldehydo-D-galacturonate (molecule.ecocyc.CPD-15633). Products: D-Tagaturonate (molecule.C00558).

## Enriched Pathways

- `ecocyc.GALACTUROCAT-PWY` D-galacturonate degradation I (EcoCyc)

## Annotation

Part of the galacturonate pathway.

## Pathways

- `ecocyc.GALACTUROCAT-PWY` D-galacturonate degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[protein.P0A8G3|protein.P0A8G3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00558|molecule.C00558]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15633|molecule.ecocyc.CPD-15633]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.2-MERCAPTOETHANOL|molecule.ecocyc.2-MERCAPTOETHANOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1610|molecule.ecocyc.CPD0-1610]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GALACTUROISOM-RXN`

## Notes

CPD-15633 -> D-TAGATURONATE; direction=REVERSIBLE
