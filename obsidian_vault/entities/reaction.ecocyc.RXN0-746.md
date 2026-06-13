---
entity_id: "reaction.ecocyc.RXN0-746"
entity_type: "reaction"
name: "RXN0-746"
source_database: "EcoCyc"
source_id: "RXN0-746"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-746

`reaction.ecocyc.RXN0-746`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-746`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FORMATE + GTP + PROTON -> DGTP + CARBON-DIOXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FORMATE + GTP + PROTON -> DGTP + CARBON-DIOXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by anaerobic ribonucleoside-triphosphate reductase (complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX). Substrates: GTP (molecule.C00044), Formate (molecule.C00058), H+ (molecule.C00080). Products: H2O (molecule.C00001), CO2 (molecule.C00011), dGTP (molecule.C00286).

## Enriched Pathways

- `ecocyc.PWY-7222` guanosine deoxyribonucleotides de novo biosynthesis II (EcoCyc)

## Annotation

FORMATE + GTP + PROTON -> DGTP + CARBON-DIOXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7222` guanosine deoxyribonucleotides de novo biosynthesis II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.C00459|molecule.C00459]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX|complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00286|molecule.C00286]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00131|molecule.C00131]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-746`

## Notes

FORMATE + GTP + PROTON -> DGTP + CARBON-DIOXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
