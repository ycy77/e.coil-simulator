---
entity_id: "reaction.ecocyc.H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN"
entity_type: "reaction"
name: "H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN"
source_database: "EcoCyc"
source_id: "H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN

`reaction.ecocyc.H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a reaction in the biosynthesis of folic acid. EcoCyc reaction equation: DIHYDRONEOPTERIN-P3 + WATER -> PROTON + DIHYDRONEOPTERIN-P + PPI; direction=LEFT-TO-RIGHT. This is a reaction in the biosynthesis of folic acid.

## Biological Role

Catalyzed by nudB (protein.P0AFC0). Substrates: H2O (molecule.C00001), 7,8-Dihydroneopterin 3'-triphosphate (molecule.C04895). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), Dihydroneopterin phosphate (molecule.C05925).

## Enriched Pathways

- `ecocyc.PWY-6147` 6-hydroxymethyl-dihydropterin diphosphate biosynthesis I (EcoCyc)

## Annotation

This is a reaction in the biosynthesis of folic acid.

## Pathways

- `ecocyc.PWY-6147` 6-hydroxymethyl-dihydropterin diphosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0AFC0|protein.P0AFC0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05925|molecule.C05925]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04895|molecule.C04895]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00459|molecule.C00459]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C05925|molecule.C05925]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:H2NEOPTERINP3PYROPHOSPHOHYDRO-RXN`

## Notes

DIHYDRONEOPTERIN-P3 + WATER -> PROTON + DIHYDRONEOPTERIN-P + PPI; direction=LEFT-TO-RIGHT
