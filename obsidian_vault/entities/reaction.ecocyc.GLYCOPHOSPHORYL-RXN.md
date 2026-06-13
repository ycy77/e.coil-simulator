---
entity_id: "reaction.ecocyc.GLYCOPHOSPHORYL-RXN"
entity_type: "reaction"
name: "GLYCOPHOSPHORYL-RXN"
source_database: "EcoCyc"
source_id: "GLYCOPHOSPHORYL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYCOPHOSPHORYL-RXN

`reaction.ecocyc.GLYCOPHOSPHORYL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYCOPHOSPHORYL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a substrate-specific reaction of the general phosphorylase reaction. It is part of the catabolic pathway for glycogen. EcoCyc reaction equation: Glycogens + Pi -> CPD0-971 + GLC-1-P; direction=PHYSIOL-LEFT-TO-RIGHT. This is a substrate-specific reaction of the general phosphorylase reaction. It is part of the catabolic pathway for glycogen.

## Biological Role

Catalyzed by glycogen phosphorylase (complex.ecocyc.GLYCOPHOSPHORYL-CPLX). Substrates: a glycogen (molecule.ecocyc.Glycogens), phosphate (molecule.ecocyc.Pi). Products: an α-limit dextrin (molecule.ecocyc.CPD0-971), α-D-glucopyranose 1-phosphate (molecule.ecocyc.GLC-1-P).

## Enriched Pathways

- `ecocyc.GLYCOCAT-PWY` glycogen degradation I (EcoCyc)

## Annotation

This is a substrate-specific reaction of the general phosphorylase reaction. It is part of the catabolic pathway for glycogen.

## Pathways

- `ecocyc.GLYCOCAT-PWY` glycogen degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (22)

- `activates` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.F-|molecule.ecocyc.F-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.NA2SO4|molecule.ecocyc.NA2SO4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[protein.P0AA04|protein.P0AA04]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.GLYCOPHOSPHORYL-CPLX|complex.ecocyc.GLYCOPHOSPHORYL-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-971|molecule.ecocyc.CPD0-971]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.GLC-1-P|molecule.ecocyc.GLC-1-P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Glycogens|molecule.ecocyc.Glycogens]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00029|molecule.C00029]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00221|molecule.C00221]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00244|molecule.C00244]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00498|molecule.C00498]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00842|molecule.C00842]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01326|molecule.C01326]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-1486|molecule.ecocyc.CPD-1486]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-387|molecule.ecocyc.CPD-387]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1463|molecule.ecocyc.CPD0-1463]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLYCOPHOSPHORYL-RXN`

## Notes

Glycogens + Pi -> CPD0-971 + GLC-1-P; direction=PHYSIOL-LEFT-TO-RIGHT
