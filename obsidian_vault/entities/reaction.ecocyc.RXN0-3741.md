---
entity_id: "reaction.ecocyc.RXN0-3741"
entity_type: "reaction"
name: "RXN0-3741"
source_database: "EcoCyc"
source_id: "RXN0-3741"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3741

`reaction.ecocyc.RXN0-3741`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3741`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

Deoxy-Ribonucleoside-Monophosphates + WATER -> Deoxy-Ribonucleosides + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Deoxy-Ribonucleoside-Monophosphates + WATER -> Deoxy-Ribonucleosides + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by acid phosphatase / phosphotransferase (complex.ecocyc.APHA-CPLX), dCMP phosphohydrolase (complex.ecocyc.CPLX0-7625), ushA (protein.P07024), yfdR (protein.P76514). Substrates: H2O (molecule.C00001), a 2'-deoxyribonucleoside 5'-monophosphate (molecule.ecocyc.Deoxy-Ribonucleoside-Monophosphates). Products: a 2'-deoxyribonucleoside (molecule.ecocyc.Deoxy-Ribonucleosides), phosphate (molecule.ecocyc.Pi).

## Annotation

Deoxy-Ribonucleoside-Monophosphates + WATER -> Deoxy-Ribonucleosides + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `catalyzes` <-- [[complex.ecocyc.APHA-CPLX|complex.ecocyc.APHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7625|complex.ecocyc.CPLX0-7625]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P07024|protein.P07024]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76514|protein.P76514]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Deoxy-Ribonucleosides|molecule.ecocyc.Deoxy-Ribonucleosides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Deoxy-Ribonucleoside-Monophosphates|molecule.ecocyc.Deoxy-Ribonucleoside-Monophosphates]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00131|molecule.C00131]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00286|molecule.C00286]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00458|molecule.C00458]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00459|molecule.C00459]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-3741`

## Notes

Deoxy-Ribonucleoside-Monophosphates + WATER -> Deoxy-Ribonucleosides + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
