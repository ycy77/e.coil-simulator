---
entity_id: "reaction.ecocyc.RXN0-723"
entity_type: "reaction"
name: "RXN0-723"
source_database: "EcoCyc"
source_id: "RXN0-723"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-723

`reaction.ecocyc.RXN0-723`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-723`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FORMATE + CTP + PROTON -> DCTP + CARBON-DIOXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FORMATE + CTP + PROTON -> DCTP + CARBON-DIOXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by anaerobic ribonucleoside-triphosphate reductase (complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX). Substrates: Formate (molecule.C00058), CTP (molecule.C00063), H+ (molecule.C00080). Products: H2O (molecule.C00001), CO2 (molecule.C00011), dCTP (molecule.C00458).

## Enriched Pathways

- `ecocyc.PWY-7187` pyrimidine deoxyribonucleotides de novo biosynthesis II (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Annotation

FORMATE + CTP + PROTON -> DCTP + CARBON-DIOXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7187` pyrimidine deoxyribonucleotides de novo biosynthesis II (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `activates` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX|complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00458|molecule.C00458]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00063|molecule.C00063]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00131|molecule.C00131]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-723`

## Notes

FORMATE + CTP + PROTON -> DCTP + CARBON-DIOXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
