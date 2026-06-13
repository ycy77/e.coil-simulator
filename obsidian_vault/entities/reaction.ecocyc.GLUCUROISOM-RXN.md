---
entity_id: "reaction.ecocyc.GLUCUROISOM-RXN"
entity_type: "reaction"
name: "GLUCUROISOM-RXN"
source_database: "EcoCyc"
source_id: "GLUCUROISOM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUCUROISOM-RXN

`reaction.ecocyc.GLUCUROISOM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUCUROISOM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of the glucuronate pathway. EcoCyc reaction equation: CPD-15530 -> FRUCTURONATE; direction=REVERSIBLE. Part of the glucuronate pathway.

## Biological Role

Catalyzed by uxaC (protein.P0A8G3). Substrates: aldehydo-D-glucuronate (molecule.ecocyc.CPD-15530). Products: D-Fructuronate (molecule.C00905).

## Enriched Pathways

- `ecocyc.PWY-7247` β-D-glucuronide and D-glucuronate degradation (EcoCyc)

## Annotation

Part of the glucuronate pathway.

## Pathways

- `ecocyc.PWY-7247` β-D-glucuronide and D-glucuronate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[protein.P0A8G3|protein.P0A8G3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00905|molecule.C00905]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15530|molecule.ecocyc.CPD-15530]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.2-MERCAPTOETHANOL|molecule.ecocyc.2-MERCAPTOETHANOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1610|molecule.ecocyc.CPD0-1610]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUCUROISOM-RXN`

## Notes

CPD-15530 -> FRUCTURONATE; direction=REVERSIBLE
