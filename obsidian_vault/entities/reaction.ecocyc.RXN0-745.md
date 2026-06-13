---
entity_id: "reaction.ecocyc.RXN0-745"
entity_type: "reaction"
name: "RXN0-745"
source_database: "EcoCyc"
source_id: "RXN0-745"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-745

`reaction.ecocyc.RXN0-745`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-745`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FORMATE + ATP + PROTON -> CARBON-DIOXIDE + DATP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FORMATE + ATP + PROTON -> CARBON-DIOXIDE + DATP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by anaerobic ribonucleoside-triphosphate reductase (complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX). Substrates: ATP (molecule.C00002), Formate (molecule.C00058), H+ (molecule.C00080). Products: H2O (molecule.C00001), CO2 (molecule.C00011), dATP (molecule.C00131).

## Enriched Pathways

- `ecocyc.PWY-7220` adenosine deoxyribonucleotides de novo biosynthesis II (EcoCyc)

## Annotation

FORMATE + ATP + PROTON -> CARBON-DIOXIDE + DATP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7220` adenosine deoxyribonucleotides de novo biosynthesis II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `activates` <-- [[molecule.C00286|molecule.C00286]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX|complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00131|molecule.C00131]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00131|molecule.C00131]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00459|molecule.C00459]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-745`

## Notes

FORMATE + ATP + PROTON -> CARBON-DIOXIDE + DATP + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
