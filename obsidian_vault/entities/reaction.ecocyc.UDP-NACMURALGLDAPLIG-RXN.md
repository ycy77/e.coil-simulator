---
entity_id: "reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN"
entity_type: "reaction"
name: "UDP-NACMURALGLDAPLIG-RXN"
source_database: "EcoCyc"
source_id: "UDP-NACMURALGLDAPLIG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDP-NACMURALGLDAPLIG-RXN

`reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UDP-NACMURALGLDAPLIG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fifth step in peptidoglycan biosynthesis. EcoCyc reaction equation: MESO-DIAMINOPIMELATE + UDP-AA-GLUTAMATE + ATP -> PROTON + UDP-AAGM-DIAMINOHEPTANEDIOATE + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the fifth step in peptidoglycan biosynthesis.

## Biological Role

Catalyzed by murE (protein.P22188). Substrates: ATP (molecule.C00002), meso-2,6-Diaminoheptanedioate (molecule.C00680), UDP-N-acetylmuramoyl-L-alanyl-D-glutamate (molecule.C00692). Products: ADP (molecule.C00008), H+ (molecule.C00080), UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimelate (molecule.C04877), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6387` UDP-N-acetylmuramoyl-pentapeptide biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Annotation

This is the fifth step in peptidoglycan biosynthesis.

## Pathways

- `ecocyc.PWY-6387` UDP-N-acetylmuramoyl-pentapeptide biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (18)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P22188|protein.P22188]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04877|molecule.C04877]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00680|molecule.C00680]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00692|molecule.C00692]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00043|molecule.C00043]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01050|molecule.C01050]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01212|molecule.C01212]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C04877|molecule.C04877]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1328|molecule.ecocyc.CPD0-1328]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1329|molecule.ecocyc.CPD0-1329]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1330|molecule.ecocyc.CPD0-1330]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:UDP-NACMURALGLDAPLIG-RXN`

## Notes

MESO-DIAMINOPIMELATE + UDP-AA-GLUTAMATE + ATP -> PROTON + UDP-AAGM-DIAMINOHEPTANEDIOATE + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
