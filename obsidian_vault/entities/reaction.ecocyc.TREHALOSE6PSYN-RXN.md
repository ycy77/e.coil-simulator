---
entity_id: "reaction.ecocyc.TREHALOSE6PSYN-RXN"
entity_type: "reaction"
name: "TREHALOSE6PSYN-RXN"
source_database: "EcoCyc"
source_id: "TREHALOSE6PSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TREHALOSE6PSYN-RXN

`reaction.ecocyc.TREHALOSE6PSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TREHALOSE6PSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction in one pathway of trehalose biosynthesis. EcoCyc reaction equation: CPD-12575 + D-glucopyranose-6-phosphate -> PROTON + UDP + TREHALOSE-6P; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first reaction in one pathway of trehalose biosynthesis.

## Biological Role

Catalyzed by trehalose-6-phosphate synthase (complex.ecocyc.CPLX0-13749). Substrates: UDP-glucose (molecule.C00029), D-Glucose 6-phosphate (molecule.C00092). Products: UDP (molecule.C00015), H+ (molecule.C00080), alpha,alpha'-Trehalose 6-phosphate (molecule.C00689).

## Enriched Pathways

- `ecocyc.TRESYN-PWY` trehalose biosynthesis I (EcoCyc)

## Annotation

This is the first reaction in one pathway of trehalose biosynthesis.

## Pathways

- `ecocyc.TRESYN-PWY` trehalose biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-13749|complex.ecocyc.CPLX0-13749]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00689|molecule.C00689]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00029|molecule.C00029]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00092|molecule.C00092]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TREHALOSE6PSYN-RXN`

## Notes

CPD-12575 + D-glucopyranose-6-phosphate -> PROTON + UDP + TREHALOSE-6P; direction=PHYSIOL-LEFT-TO-RIGHT
