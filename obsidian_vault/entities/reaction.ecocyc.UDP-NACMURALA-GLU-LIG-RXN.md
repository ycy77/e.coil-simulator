---
entity_id: "reaction.ecocyc.UDP-NACMURALA-GLU-LIG-RXN"
entity_type: "reaction"
name: "UDP-NACMURALA-GLU-LIG-RXN"
source_database: "EcoCyc"
source_id: "UDP-NACMURALA-GLU-LIG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDP-NACMURALA-GLU-LIG-RXN

`reaction.ecocyc.UDP-NACMURALA-GLU-LIG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UDP-NACMURALA-GLU-LIG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fourth step in peptidoglycan biosynthesis. EcoCyc reaction equation: D-GLT + CPD0-1456 + ATP -> PROTON + UDP-AA-GLUTAMATE + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the fourth step in peptidoglycan biosynthesis.

## Biological Role

Catalyzed by murD (protein.P14900). Substrates: ATP (molecule.C00002), D-Glutamate (molecule.C00217), UDP-N-acetylmuramoyl-L-alanine (molecule.C01212). Products: ADP (molecule.C00008), H+ (molecule.C00080), UDP-N-acetylmuramoyl-L-alanyl-D-glutamate (molecule.C00692), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6387` UDP-N-acetylmuramoyl-pentapeptide biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Annotation

This is the fourth step in peptidoglycan biosynthesis.

## Pathways

- `ecocyc.PWY-6387` UDP-N-acetylmuramoyl-pentapeptide biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[protein.P14900|protein.P14900]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00692|molecule.C00692]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00217|molecule.C00217]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01212|molecule.C01212]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00692|molecule.C00692]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1331|molecule.ecocyc.CPD0-1331]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:UDP-NACMURALA-GLU-LIG-RXN`

## Notes

D-GLT + CPD0-1456 + ATP -> PROTON + UDP-AA-GLUTAMATE + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
