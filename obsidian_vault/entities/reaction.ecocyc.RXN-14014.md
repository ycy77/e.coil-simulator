---
entity_id: "reaction.ecocyc.RXN-14014"
entity_type: "reaction"
name: "RXN-14014"
source_database: "EcoCyc"
source_id: "RXN-14014"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14014

`reaction.ecocyc.RXN-14014`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14014`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DELTA1-PIPERIDEINE-2-6-DICARBOXYLATE + NAD-P-OR-NOP + WATER -> CPD-14443 + NADH-P-OR-NOP + PROTON; direction=RIGHT-TO-LEFT EcoCyc reaction equation: DELTA1-PIPERIDEINE-2-6-DICARBOXYLATE + NAD-P-OR-NOP + WATER -> CPD-14443 + NADH-P-OR-NOP + PROTON; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by 4-hydroxy-tetrahydrodipicolinate reductase (complex.ecocyc.DIHYDROPICRED-CPLX). Substrates: H2O (molecule.C00001), 2,3,4,5-Tetrahydrodipicolinate (molecule.C03972), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), (2S,4S)-4-Hydroxy-2,3,4,5-tetrahydrodipicolinate (molecule.C20258), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Enriched Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)

## Annotation

DELTA1-PIPERIDEINE-2-6-DICARBOXYLATE + NAD-P-OR-NOP + WATER -> CPD-14443 + NADH-P-OR-NOP + PROTON; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.DIHYDROPICRED-CPLX|complex.ecocyc.DIHYDROPICRED-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C20258|molecule.C20258]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03972|molecule.C03972]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-14014`

## Notes

DELTA1-PIPERIDEINE-2-6-DICARBOXYLATE + NAD-P-OR-NOP + WATER -> CPD-14443 + NADH-P-OR-NOP + PROTON; direction=RIGHT-TO-LEFT
