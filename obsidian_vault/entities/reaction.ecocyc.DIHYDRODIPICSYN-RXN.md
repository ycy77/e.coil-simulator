---
entity_id: "reaction.ecocyc.DIHYDRODIPICSYN-RXN"
entity_type: "reaction"
name: "DIHYDRODIPICSYN-RXN"
source_database: "EcoCyc"
source_id: "DIHYDRODIPICSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIHYDRODIPICSYN-RXN

`reaction.ecocyc.DIHYDRODIPICSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIHYDRODIPICSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction of the diaminopimelate-lysine biosynthetic pathway. EcoCyc reaction equation: PYRUVATE + L-ASPARTATE-SEMIALDEHYDE -> CPD-14443 + WATER + PROTON; direction=LEFT-TO-RIGHT. This is the first reaction of the diaminopimelate-lysine biosynthetic pathway.

## Biological Role

Catalyzed by 4-hydroxy-tetrahydrodipicolinate synthase (complex.ecocyc.DIHYDRODIPICSYN-CPLX). Substrates: Pyruvate (molecule.C00022), L-Aspartate 4-semialdehyde (molecule.C00441). Products: H2O (molecule.C00001), H+ (molecule.C00080), (2S,4S)-4-Hydroxy-2,3,4,5-tetrahydrodipicolinate (molecule.C20258).

## Enriched Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)

## Annotation

This is the first reaction of the diaminopimelate-lysine biosynthetic pathway.

## Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `catalyzes` <-- [[complex.ecocyc.DIHYDRODIPICSYN-CPLX|complex.ecocyc.DIHYDRODIPICSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20258|molecule.C20258]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00441|molecule.C00441]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00168|molecule.C00168]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00232|molecule.C00232]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C16588|molecule.C16588]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.3-BROMOPYRUVATE|molecule.ecocyc.3-BROMOPYRUVATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-26607|molecule.ecocyc.CPD-26607]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-4841|molecule.ecocyc.CPD-4841]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.S-2-AMINOETHYL-L-CYSTEINE|molecule.ecocyc.S-2-AMINOETHYL-L-CYSTEINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DIHYDRODIPICSYN-RXN`

## Notes

PYRUVATE + L-ASPARTATE-SEMIALDEHYDE -> CPD-14443 + WATER + PROTON; direction=LEFT-TO-RIGHT
