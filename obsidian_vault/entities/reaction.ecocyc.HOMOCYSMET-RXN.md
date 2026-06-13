---
entity_id: "reaction.ecocyc.HOMOCYSMET-RXN"
entity_type: "reaction"
name: "HOMOCYSMET-RXN"
source_database: "EcoCyc"
source_id: "HOMOCYSMET-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HOMOCYSMET-RXN

`reaction.ecocyc.HOMOCYSMET-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HOMOCYSMET-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the terminal step in methionine biosynthesis, one of two possible similar reactions which are catalyzed by two unique enzymes. Both effect homocysteine methylation. EcoCyc reaction equation: CPD-1302 + HOMO-CYS -> MET + CPD-1301; direction=LEFT-TO-RIGHT. This is the terminal step in methionine biosynthesis, one of two possible similar reactions which are catalyzed by two unique enzymes. Both effect homocysteine methylation.

## Biological Role

Catalyzed by metE (protein.P25665). Substrates: L-Homocysteine (molecule.C00155), 5-methyltetrahydropteroyl tri-L-glutamate (molecule.ecocyc.CPD-1302). Products: L-Methionine (molecule.C00073), tetrahydropteroyl tri-L-glutamate (molecule.ecocyc.CPD-1301).

## Enriched Pathways

- `ecocyc.HOMOSER-METSYN-PWY` L-methionine biosynthesis I (EcoCyc)
- `ecocyc.PWY-6151` S-adenosyl-L-methionine salvage I (EcoCyc)

## Annotation

This is the terminal step in methionine biosynthesis, one of two possible similar reactions which are catalyzed by two unique enzymes. Both effect homocysteine methylation.

## Pathways

- `ecocyc.HOMOSER-METSYN-PWY` L-methionine biosynthesis I (EcoCyc)
- `ecocyc.PWY-6151` S-adenosyl-L-methionine salvage I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P25665|protein.P25665]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-1301|molecule.ecocyc.CPD-1301]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00155|molecule.C00155]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-1302|molecule.ecocyc.CPD-1302]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1472|molecule.ecocyc.CPD0-1472]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1473|molecule.ecocyc.CPD0-1473]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1474|molecule.ecocyc.CPD0-1474]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:HOMOCYSMET-RXN`

## Notes

CPD-1302 + HOMO-CYS -> MET + CPD-1301; direction=LEFT-TO-RIGHT
