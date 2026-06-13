---
entity_id: "reaction.ecocyc.SUPEROX-DISMUT-RXN"
entity_type: "reaction"
name: "SUPEROX-DISMUT-RXN"
source_database: "EcoCyc"
source_id: "SUPEROX-DISMUT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL|CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SUPEROX-DISMUT-RXN

`reaction.ecocyc.SUPEROX-DISMUT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SUPEROX-DISMUT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL|CCO-PERI-BAC

## Enriched Summary

This reaction is involved in detoxification. EcoCyc reaction equation: PROTON + SUPER-OXIDE -> HYDROGEN-PEROXIDE + OXYGEN-MOLECULE; direction=LEFT-TO-RIGHT. This reaction is involved in detoxification.

## Biological Role

Catalyzed by superoxide dismutase (Fe) (complex.ecocyc.SUPEROX-DISMUTFE-CPLX), superoxide dismutase (Mn) (complex.ecocyc.SUPEROX-DISMUTMN-CPLX), sodC (protein.P0AGD1). Substrates: H+ (molecule.C00080), superoxide (molecule.ecocyc.SUPER-OXIDE). Products: Oxygen (molecule.C00007), Hydrogen peroxide (molecule.C00027).

## Enriched Pathways

- `ecocyc.DETOX1-PWY` superoxide radicals degradation (EcoCyc)

## Annotation

This reaction is involved in detoxification.

## Pathways

- `ecocyc.DETOX1-PWY` superoxide radicals degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.SUPEROX-DISMUTFE-CPLX|complex.ecocyc.SUPEROX-DISMUTFE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.SUPEROX-DISMUTMN-CPLX|complex.ecocyc.SUPEROX-DISMUTMN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AGD1|protein.P0AGD1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.SUPER-OXIDE|molecule.ecocyc.SUPER-OXIDE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-13584|molecule.ecocyc.CPD-13584]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-2841|molecule.ecocyc.CPD-2841]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DIETHYLDITHIOCARBAMATE|molecule.ecocyc.DIETHYLDITHIOCARBAMATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:SUPEROX-DISMUT-RXN`

## Notes

PROTON + SUPER-OXIDE -> HYDROGEN-PEROXIDE + OXYGEN-MOLECULE; direction=LEFT-TO-RIGHT
