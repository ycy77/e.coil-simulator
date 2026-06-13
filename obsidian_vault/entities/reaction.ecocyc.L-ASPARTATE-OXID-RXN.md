---
entity_id: "reaction.ecocyc.L-ASPARTATE-OXID-RXN"
entity_type: "reaction"
name: "L-ASPARTATE-OXID-RXN"
source_database: "EcoCyc"
source_id: "L-ASPARTATE-OXID-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-ASPARTATE-OXID-RXN

`reaction.ecocyc.L-ASPARTATE-OXID-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:L-ASPARTATE-OXID-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

First reaction in quinolinate biosynthesis, required for the de novo biosynthesis of NAD. EcoCyc reaction equation: OXYGEN-MOLECULE + L-ASPARTATE -> PROTON + HYDROGEN-PEROXIDE + IMINOASPARTATE; direction=PHYSIOL-LEFT-TO-RIGHT. First reaction in quinolinate biosynthesis, required for the de novo biosynthesis of NAD.

## Biological Role

Catalyzed by nadB (protein.P10902). Substrates: Oxygen (molecule.C00007), L-Aspartate (molecule.C00049). Products: Hydrogen peroxide (molecule.C00027), H+ (molecule.C00080), Iminoaspartate (molecule.C05840).

## Enriched Pathways

- `ecocyc.PYRIDNUCSYN-PWY` NAD de novo biosynthesis I (EcoCyc)

## Annotation

First reaction in quinolinate biosynthesis, required for the de novo biosynthesis of NAD.

## Pathways

- `ecocyc.PYRIDNUCSYN-PWY` NAD de novo biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P10902|protein.P10902]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05840|molecule.C05840]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00552|molecule.C00552]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C05840|molecule.C05840]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-8829|molecule.ecocyc.CPD-8829]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:L-ASPARTATE-OXID-RXN`

## Notes

OXYGEN-MOLECULE + L-ASPARTATE -> PROTON + HYDROGEN-PEROXIDE + IMINOASPARTATE; direction=PHYSIOL-LEFT-TO-RIGHT
