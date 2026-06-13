---
entity_id: "reaction.ecocyc.ARGDECARBOX-RXN"
entity_type: "reaction"
name: "ARGDECARBOX-RXN"
source_database: "EcoCyc"
source_id: "ARGDECARBOX-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ARGDECARBOX-RXN

`reaction.ecocyc.ARGDECARBOX-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ARGDECARBOX-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

This is the first step in the biosynthesis of spermidine from arginine. EcoCyc reaction equation: PROTON + ARG -> CARBON-DIOXIDE + AGMATHINE; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first step in the biosynthesis of spermidine from arginine.

## Biological Role

Catalyzed by biosynthetic arginine decarboxylase (complex.ecocyc.ARGDECARBOXBIO-CPLX), arginine decarboxylase, degradative (complex.ecocyc.ARGDECARBOXDEG-CPLX). Substrates: L-Arginine (molecule.C00062), H+ (molecule.C00080). Products: CO2 (molecule.C00011), Agmatine (molecule.C00179).

## Enriched Pathways

- `ecocyc.PWY-40` putrescine biosynthesis I (EcoCyc)
- `ecocyc.PWY0-1299` arginine dependent acid resistance (EcoCyc)
- `ecocyc.PWY0-823` L-arginine degradation III (arginine decarboxylase/agmatinase pathway) (EcoCyc)

## Annotation

This is the first step in the biosynthesis of spermidine from arginine.

## Pathways

- `ecocyc.PWY-40` putrescine biosynthesis I (EcoCyc)
- `ecocyc.PWY0-1299` arginine dependent acid resistance (EcoCyc)
- `ecocyc.PWY0-823` L-arginine degradation III (arginine decarboxylase/agmatinase pathway) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (20)

- `catalyzes` <-- [[complex.ecocyc.ARGDECARBOXBIO-CPLX|complex.ecocyc.ARGDECARBOXBIO-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ARGDECARBOXDEG-CPLX|complex.ecocyc.ARGDECARBOXDEG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00179|molecule.C00179]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00062|molecule.C00062]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00077|molecule.C00077]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1659|molecule.ecocyc.CPD0-1659]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1660|molecule.ecocyc.CPD0-1660]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1661|molecule.ecocyc.CPD0-1661]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1662|molecule.ecocyc.CPD0-1662]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1663|molecule.ecocyc.CPD0-1663]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1664|molecule.ecocyc.CPD0-1664]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Guanido-Compounds|molecule.ecocyc.Guanido-Compounds]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Ureido-Compounds|molecule.ecocyc.Ureido-Compounds]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[protein.P0A7P5|protein.P0A7P5]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[protein.P0A7U7|protein.P0A7U7]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ARGDECARBOX-RXN`

## Notes

PROTON + ARG -> CARBON-DIOXIDE + AGMATHINE; direction=PHYSIOL-LEFT-TO-RIGHT
