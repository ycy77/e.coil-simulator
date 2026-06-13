---
entity_id: "reaction.ecocyc.RXN0-724"
entity_type: "reaction"
name: "RXN0-724"
source_database: "EcoCyc"
source_id: "RXN0-724"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-724

`reaction.ecocyc.RXN0-724`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-724`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FORMATE + UTP + PROTON -> DUTP + CARBON-DIOXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FORMATE + UTP + PROTON -> DUTP + CARBON-DIOXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by anaerobic ribonucleoside-triphosphate reductase (complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX). Substrates: Formate (molecule.C00058), UTP (molecule.C00075), H+ (molecule.C00080). Products: H2O (molecule.C00001), CO2 (molecule.C00011), dUTP (molecule.C00460).

## Enriched Pathways

- `ecocyc.PWY-7187` pyrimidine deoxyribonucleotides de novo biosynthesis II (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Annotation

FORMATE + UTP + PROTON -> DUTP + CARBON-DIOXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7187` pyrimidine deoxyribonucleotides de novo biosynthesis II (EcoCyc)
- `ecocyc.PWY0-166` superpathway of pyrimidine deoxyribonucleotides de novo biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX|complex.ecocyc.RIBONUCLEOSIDE-TRIP-REDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00460|molecule.C00460]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00131|molecule.C00131]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-724`

## Notes

FORMATE + UTP + PROTON -> DUTP + CARBON-DIOXIDE + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
