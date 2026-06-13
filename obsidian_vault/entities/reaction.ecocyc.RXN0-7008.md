---
entity_id: "reaction.ecocyc.RXN0-7008"
entity_type: "reaction"
name: "RXN0-7008"
source_database: "EcoCyc"
source_id: "RXN0-7008"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7008

`reaction.ecocyc.RXN0-7008`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7008`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Ubiquinones + PRO -> Ubiquinols + PROTON + L-DELTA1-PYRROLINE_5-CARBOXYLATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Ubiquinones + PRO -> Ubiquinols + PROTON + L-DELTA1-PYRROLINE_5-CARBOXYLATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fused DNA-binding transcriptional repressor / proline dehydrogenase / 1-pyrroline-5-carboxylate dehydrogenase PutA (complex.ecocyc.PUTA-CPLX). Substrates: L-Proline (molecule.C00148), a ubiquinone (molecule.ecocyc.Ubiquinones). Products: H+ (molecule.C00080), Ubiquinol (molecule.C00390), (S)-1-Pyrroline-5-carboxylate (molecule.C03912).

## Enriched Pathways

- `ecocyc.PROUT-PWY-I` proline degradation (EcoCyc)
- `ecocyc.PWY0-1544` proline to cytochrome bo oxidase electron transfer (EcoCyc)

## Annotation

Ubiquinones + PRO -> Ubiquinols + PROTON + L-DELTA1-PYRROLINE_5-CARBOXYLATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PROUT-PWY-I` proline degradation (EcoCyc)
- `ecocyc.PWY0-1544` proline to cytochrome bo oxidase electron transfer (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `catalyzes` <-- [[complex.ecocyc.PUTA-CPLX|complex.ecocyc.PUTA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03912|molecule.C03912]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00148|molecule.C00148]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00186|molecule.C00186]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00256|molecule.C00256]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-19547|molecule.ecocyc.CPD-19547]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-5742|molecule.ecocyc.CPD-5742]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1104|molecule.ecocyc.CPD0-1104]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1572|molecule.ecocyc.CPD0-1572]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-7008`

## Notes

Ubiquinones + PRO -> Ubiquinols + PROTON + L-DELTA1-PYRROLINE_5-CARBOXYLATE; direction=PHYSIOL-LEFT-TO-RIGHT
