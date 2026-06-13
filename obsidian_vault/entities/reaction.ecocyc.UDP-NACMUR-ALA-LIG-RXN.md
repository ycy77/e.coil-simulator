---
entity_id: "reaction.ecocyc.UDP-NACMUR-ALA-LIG-RXN"
entity_type: "reaction"
name: "UDP-NACMUR-ALA-LIG-RXN"
source_database: "EcoCyc"
source_id: "UDP-NACMUR-ALA-LIG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDP-NACMUR-ALA-LIG-RXN

`reaction.ecocyc.UDP-NACMUR-ALA-LIG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UDP-NACMUR-ALA-LIG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third step in peptidoglycan biosynthesis. EcoCyc reaction equation: L-ALPHA-ALANINE + UDP-N-ACETYLMURAMATE + ATP -> PROTON + CPD0-1456 + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the third step in peptidoglycan biosynthesis.

## Biological Role

Catalyzed by UDP-N-acetylmuramate—L-alanine ligase (complex.ecocyc.CPLX0-8014). Substrates: ATP (molecule.C00002), L-Alanine (molecule.C00041), UDP-N-acetylmuramate (molecule.C01050). Products: ADP (molecule.C00008), H+ (molecule.C00080), UDP-N-acetylmuramoyl-L-alanine (molecule.C01212), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6387` UDP-N-acetylmuramoyl-pentapeptide biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Annotation

This is the third step in peptidoglycan biosynthesis.

## Pathways

- `ecocyc.PWY-6387` UDP-N-acetylmuramoyl-pentapeptide biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8014|complex.ecocyc.CPLX0-8014]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01212|molecule.C01212]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01050|molecule.C01050]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CHLORALAN-CPD|molecule.ecocyc.CHLORALAN-CPD]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1335|molecule.ecocyc.CPD0-1335]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1336|molecule.ecocyc.CPD0-1336]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:UDP-NACMUR-ALA-LIG-RXN`

## Notes

L-ALPHA-ALANINE + UDP-N-ACETYLMURAMATE + ATP -> PROTON + CPD0-1456 + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
