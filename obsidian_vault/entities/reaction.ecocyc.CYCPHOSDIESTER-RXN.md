---
entity_id: "reaction.ecocyc.CYCPHOSDIESTER-RXN"
entity_type: "reaction"
name: "CYCPHOSDIESTER-RXN"
source_database: "EcoCyc"
source_id: "CYCPHOSDIESTER-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CYCPHOSDIESTER-RXN

`reaction.ecocyc.CYCPHOSDIESTER-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CYCPHOSDIESTER-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This is the first of two consecutive reactions in the degradation of ribonucleic acids, acting on an intermediate in degradation of RNA, 2',3'-cyclic nucleotides. EcoCyc reaction equation: Cyclic-2-3-Ribonucleoside-Monophosphates + WATER -> 3-Phosphomonucleotides + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first of two consecutive reactions in the degradation of ribonucleic acids, acting on an intermediate in degradation of RNA, 2',3'-cyclic nucleotides.

## Biological Role

Catalyzed by cpdB (protein.P08331). Substrates: H2O (molecule.C00001), a ribonucleoside 2',3'-cyclic phosphate (molecule.ecocyc.Cyclic-2-3-Ribonucleoside-Monophosphates). Products: H+ (molecule.C00080), a ribonucleoside 3'-phosphate (molecule.ecocyc.3-Phosphomonucleotides).

## Annotation

This is the first of two consecutive reactions in the degradation of ribonucleic acids, acting on an intermediate in degradation of RNA, 2',3'-cyclic nucleotides.

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `activates` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P08331|protein.P08331]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.3-Phosphomonucleotides|molecule.ecocyc.3-Phosphomonucleotides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Cyclic-2-3-Ribonucleoside-Monophosphates|molecule.ecocyc.Cyclic-2-3-Ribonucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7082|molecule.ecocyc.CPD-7082]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CYCPHOSDIESTER-RXN`

## Notes

Cyclic-2-3-Ribonucleoside-Monophosphates + WATER -> 3-Phosphomonucleotides + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
