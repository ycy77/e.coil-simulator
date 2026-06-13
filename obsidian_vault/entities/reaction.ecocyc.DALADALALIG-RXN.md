---
entity_id: "reaction.ecocyc.DALADALALIG-RXN"
entity_type: "reaction"
name: "DALADALALIG-RXN"
source_database: "EcoCyc"
source_id: "DALADALALIG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DALADALALIG-RXN

`reaction.ecocyc.DALADALALIG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DALADALALIG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes D-alanyl-D-alanine an essential component of the peptidoglycan layer of the cell wall. EcoCyc reaction equation: D-ALANINE + ATP -> PROTON + D-ALA-D-ALA + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction synthesizes D-alanyl-D-alanine an essential component of the peptidoglycan layer of the cell wall.

## Biological Role

Catalyzed by D-alanine—D-alanine ligase B (complex.ecocyc.DALADALALIGB-CPLX), ddlA (protein.P0A6J8). Substrates: ATP (molecule.C00002), D-Alanine (molecule.C00133). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-Alanyl-D-alanine (molecule.C00993), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6387` UDP-N-acetylmuramoyl-pentapeptide biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Annotation

This reaction synthesizes D-alanyl-D-alanine an essential component of the peptidoglycan layer of the cell wall.

## Pathways

- `ecocyc.PWY-6387` UDP-N-acetylmuramoyl-pentapeptide biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.DALADALALIGB-CPLX|complex.ecocyc.DALADALALIGB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A6J8|protein.P0A6J8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00993|molecule.C00993]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00993|molecule.C00993]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Aminoalkylphosphinates|molecule.ecocyc.Aminoalkylphosphinates]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-2482|molecule.ecocyc.CPD-2482]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2648|molecule.ecocyc.CPD0-2648]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DALADALALIG-RXN`

## Notes

D-ALANINE + ATP -> PROTON + D-ALA-D-ALA + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
