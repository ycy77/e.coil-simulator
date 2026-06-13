---
entity_id: "reaction.ecocyc.METHGLYSYN-RXN"
entity_type: "reaction"
name: "METHGLYSYN-RXN"
source_database: "EcoCyc"
source_id: "METHGLYSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# METHGLYSYN-RXN

`reaction.ecocyc.METHGLYSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:METHGLYSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DIHYDROXY-ACETONE-PHOSPHATE -> METHYL-GLYOXAL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DIHYDROXY-ACETONE-PHOSPHATE -> METHYL-GLYOXAL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by methylglyoxal synthase (complex.ecocyc.METHGLYSYN-CPLX). Substrates: Glycerone phosphate (molecule.C00111). Products: Methylglyoxal (molecule.C00546), phosphate (molecule.ecocyc.Pi).

## Annotation

DIHYDROXY-ACETONE-PHOSPHATE -> METHYL-GLYOXAL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.METHGLYSYN-CPLX|complex.ecocyc.METHGLYSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00546|molecule.C00546]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00197|molecule.C00197]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00988|molecule.C00988]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.ARSENATE|molecule.ecocyc.ARSENATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1102|molecule.ecocyc.CPD0-1102]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:METHGLYSYN-RXN`

## Notes

DIHYDROXY-ACETONE-PHOSPHATE -> METHYL-GLYOXAL + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
