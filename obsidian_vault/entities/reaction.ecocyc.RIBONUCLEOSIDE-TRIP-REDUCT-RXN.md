---
entity_id: "reaction.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-RXN"
entity_type: "reaction"
name: "RIBONUCLEOSIDE-TRIP-REDUCT-RXN"
source_database: "EcoCyc"
source_id: "RIBONUCLEOSIDE-TRIP-REDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RIBONUCLEOSIDE-TRIP-REDUCT-RXN

`reaction.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RIBONUCLEOSIDE-TRIP-REDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes deoxyribonucleoside triphosphates during anaerobic growth. EcoCyc reaction equation: FORMATE + Ribonucleoside-Triphosphates + PROTON -> Deoxy-Ribonucleoside-Triphosphates + CARBON-DIOXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction synthesizes deoxyribonucleoside triphosphates during anaerobic growth.

## Biological Role

Catalyzed by anaerobic ribonucleoside-triphosphate reductase (complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX). Substrates: Formate (molecule.C00058), H+ (molecule.C00080), a ribonucleoside triphosphate (molecule.ecocyc.Ribonucleoside-Triphosphates). Products: H2O (molecule.C00001), CO2 (molecule.C00011), a 2'-deoxyribonucleoside 5'-triphosphate (molecule.ecocyc.Deoxy-Ribonucleoside-Triphosphates).

## Annotation

This reaction synthesizes deoxyribonucleoside triphosphates during anaerobic growth.

## Outgoing Edges (0)

_None._

## Incoming Edges (17)

- `catalyzes` <-- [[complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX|complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Deoxy-Ribonucleoside-Triphosphates|molecule.ecocyc.Deoxy-Ribonucleoside-Triphosphates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ribonucleoside-Triphosphates|molecule.ecocyc.Ribonucleoside-Triphosphates]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00131|molecule.C00131]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1388|molecule.ecocyc.CPD0-1388]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1390|molecule.ecocyc.CPD0-1390]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1391|molecule.ecocyc.CPD0-1391]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIOTHREITOL|molecule.ecocyc.DITHIOTHREITOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RIBONUCLEOSIDE-TRIP-REDUCT-RXN`

## Notes

FORMATE + Ribonucleoside-Triphosphates + PROTON -> Deoxy-Ribonucleoside-Triphosphates + CARBON-DIOXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
