---
entity_id: "reaction.ecocyc.DIHYDROFOLATESYNTH-RXN"
entity_type: "reaction"
name: "DIHYDROFOLATESYNTH-RXN"
source_database: "EcoCyc"
source_id: "DIHYDROFOLATESYNTH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "DIHYDROFOLATE SYNTHETASE"
---

# DIHYDROFOLATESYNTH-RXN

`reaction.ecocyc.DIHYDROFOLATESYNTH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIHYDROFOLATESYNTH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLT + 7-8-DIHYDROPTEROATE + ATP -> PROTON + DIHYDROFOLATE + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLT + 7-8-DIHYDROPTEROATE + ATP -> PROTON + DIHYDROFOLATE + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by folC (protein.P08192). Substrates: ATP (molecule.C00002), L-Glutamate (molecule.C00025), Dihydropteroate (molecule.C00921). Products: ADP (molecule.C00008), H+ (molecule.C00080), Dihydrofolate (molecule.C00415), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6614` tetrahydrofolate biosynthesis I (EcoCyc)

## Annotation

GLT + 7-8-DIHYDROPTEROATE + ATP -> PROTON + DIHYDROFOLATE + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6614` tetrahydrofolate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[protein.P08192|protein.P08192]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00415|molecule.C00415]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00921|molecule.C00921]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00415|molecule.C00415]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1251|molecule.ecocyc.CPD0-1251]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1252|molecule.ecocyc.CPD0-1252]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1253|molecule.ecocyc.CPD0-1253]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DIHYDROFOLATESYNTH-RXN`

## Notes

GLT + 7-8-DIHYDROPTEROATE + ATP -> PROTON + DIHYDROFOLATE + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
