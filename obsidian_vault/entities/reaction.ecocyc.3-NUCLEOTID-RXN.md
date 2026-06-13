---
entity_id: "reaction.ecocyc.3-NUCLEOTID-RXN"
entity_type: "reaction"
name: "3-NUCLEOTID-RXN"
source_database: "EcoCyc"
source_id: "3-NUCLEOTID-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-NUCLEOTID-RXN

`reaction.ecocyc.3-NUCLEOTID-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3-NUCLEOTID-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

This is the second of two consecutive reactions in the degradation of ribonucleic acids. EcoCyc reaction equation: 3-Phosphomonucleotides + WATER -> Ribonucleosides + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second of two consecutive reactions in the degradation of ribonucleic acids.

## Biological Role

Catalyzed by acid phosphatase / phosphotransferase (complex.ecocyc.APHA-CPLX), cpdB (protein.P08331), surE (protein.P0A840). Substrates: H2O (molecule.C00001), a ribonucleoside 3'-phosphate (molecule.ecocyc.3-Phosphomonucleotides). Products: phosphate (molecule.ecocyc.Pi), a ribonucleoside (molecule.ecocyc.Ribonucleosides).

## Annotation

This is the second of two consecutive reactions in the degradation of ribonucleic acids.

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `activates` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.APHA-CPLX|complex.ecocyc.APHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P08331|protein.P08331]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A840|protein.P0A840]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Ribonucleosides|molecule.ecocyc.Ribonucleosides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.3-Phosphomonucleotides|molecule.ecocyc.3-Phosphomonucleotides]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7082|molecule.ecocyc.CPD-7082]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3-NUCLEOTID-RXN`

## Notes

3-Phosphomonucleotides + WATER -> Ribonucleosides + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
