---
entity_id: "reaction.ecocyc.5-NUCLEOTID-RXN"
entity_type: "reaction"
name: "5-NUCLEOTID-RXN"
source_database: "EcoCyc"
source_id: "5-NUCLEOTID-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 5-NUCLEOTID-RXN

`reaction.ecocyc.5-NUCLEOTID-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:5-NUCLEOTID-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

This reaction is involved in the hydrolysis of nucleotides. EcoCyc reaction equation: Ribonucleoside-Monophosphates + WATER -> Ribonucleosides + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is involved in the hydrolysis of nucleotides.

## Biological Role

Catalyzed by acid phosphatase / phosphotransferase (complex.ecocyc.APHA-CPLX), ushA (protein.P07024), surE (protein.P0A840), yjjG (protein.P0A8Y1), nagD (protein.P0AF24). Substrates: H2O (molecule.C00001), a ribonucleoside 5'-monophosphate (molecule.ecocyc.Ribonucleoside-Monophosphates). Products: phosphate (molecule.ecocyc.Pi), a ribonucleoside (molecule.ecocyc.Ribonucleosides).

## Annotation

This reaction is involved in the hydrolysis of nucleotides.

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `activates` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.APHA-CPLX|complex.ecocyc.APHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P07024|protein.P07024]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A840|protein.P0A840]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A8Y1|protein.P0A8Y1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AF24|protein.P0AF24]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Ribonucleosides|molecule.ecocyc.Ribonucleosides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ribonucleoside-Monophosphates|molecule.ecocyc.Ribonucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:5-NUCLEOTID-RXN`

## Notes

Ribonucleoside-Monophosphates + WATER -> Ribonucleosides + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
