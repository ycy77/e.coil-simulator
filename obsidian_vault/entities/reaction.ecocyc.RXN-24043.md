---
entity_id: "reaction.ecocyc.RXN-24043"
entity_type: "reaction"
name: "RXN-24043"
source_database: "EcoCyc"
source_id: "RXN-24043"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24043

`reaction.ecocyc.RXN-24043`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24043`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-4211 + Oxidized-flavodoxins + WATER -> HYDROXY-METHYL-BUTENYL-DIP + Reduced-flavodoxins; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: CPD-4211 + Oxidized-flavodoxins + WATER -> HYDROXY-METHYL-BUTENYL-DIP + Reduced-flavodoxins; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by 4-hydroxy-3-methylbut-2-enyl diphosphate reductase (complex.ecocyc.CPLX0-7564). Substrates: H2O (molecule.C00001), Dimethylallyl diphosphate (molecule.C00235). Products: 1-Hydroxy-2-methyl-2-butenyl 4-diphosphate (molecule.C11811).

## Enriched Pathways

- `ecocyc.NONMEVIPP-PWY` methylerythritol phosphate pathway I (EcoCyc)

## Annotation

CPD-4211 + Oxidized-flavodoxins + WATER -> HYDROXY-METHYL-BUTENYL-DIP + Reduced-flavodoxins; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.NONMEVIPP-PWY` methylerythritol phosphate pathway I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `activates` <-- [[molecule.ecocyc.PAMIDRONATE|molecule.ecocyc.PAMIDRONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7564|complex.ecocyc.CPLX0-7564]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C11811|molecule.C11811]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00235|molecule.C00235]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-24043`

## Notes

CPD-4211 + Oxidized-flavodoxins + WATER -> HYDROXY-METHYL-BUTENYL-DIP + Reduced-flavodoxins; direction=PHYSIOL-RIGHT-TO-LEFT
