---
entity_id: "reaction.ecocyc.TETHYDPICSUCC-RXN"
entity_type: "reaction"
name: "TETHYDPICSUCC-RXN"
source_database: "EcoCyc"
source_id: "TETHYDPICSUCC-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TETHYDPICSUCC-RXN

`reaction.ecocyc.TETHYDPICSUCC-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TETHYDPICSUCC-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third reaction in the biosynthesis of lysine and diaminopimelate. EcoCyc reaction equation: WATER + DELTA1-PIPERIDEINE-2-6-DICARBOXYLATE + SUC-COA -> N-SUCCINYL-2-AMINO-6-KETOPIMELATE + CO-A; direction=LEFT-TO-RIGHT. This is the third reaction in the biosynthesis of lysine and diaminopimelate.

## Biological Role

Catalyzed by tetrahydrodipicolinate succinylase (complex.ecocyc.CPLX0-3181). Substrates: H2O (molecule.C00001), Succinyl-CoA (molecule.C00091), 2,3,4,5-Tetrahydrodipicolinate (molecule.C03972). Products: CoA (molecule.C00010), N-Succinyl-2-L-amino-6-oxoheptanedioate (molecule.C04462).

## Enriched Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)

## Annotation

This is the third reaction in the biosynthesis of lysine and diaminopimelate.

## Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3181|complex.ecocyc.CPLX0-3181]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04462|molecule.C04462]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00091|molecule.C00091]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03972|molecule.C03972]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TETHYDPICSUCC-RXN`

## Notes

WATER + DELTA1-PIPERIDEINE-2-6-DICARBOXYLATE + SUC-COA -> N-SUCCINYL-2-AMINO-6-KETOPIMELATE + CO-A; direction=LEFT-TO-RIGHT
