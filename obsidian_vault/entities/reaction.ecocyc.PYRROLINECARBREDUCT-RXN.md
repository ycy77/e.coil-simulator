---
entity_id: "reaction.ecocyc.PYRROLINECARBREDUCT-RXN"
entity_type: "reaction"
name: "PYRROLINECARBREDUCT-RXN"
source_database: "EcoCyc"
source_id: "PYRROLINECARBREDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PYRROLINECARBREDUCT-RXN

`reaction.ecocyc.PYRROLINECARBREDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PYRROLINECARBREDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD-P-OR-NOP + PRO -> NADH-P-OR-NOP + L-DELTA1-PYRROLINE_5-CARBOXYLATE + PROTON; direction=RIGHT-TO-LEFT EcoCyc reaction equation: NAD-P-OR-NOP + PRO -> NADH-P-OR-NOP + L-DELTA1-PYRROLINE_5-CARBOXYLATE + PROTON; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by pyrroline-5-carboxylate reductase (complex.ecocyc.PYRROLINECARBREDUCT-CPLX). Substrates: L-Proline (molecule.C00148), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP). Products: H+ (molecule.C00080), (S)-1-Pyrroline-5-carboxylate (molecule.C03912), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP).

## Enriched Pathways

- `ecocyc.PROSYN-PWY` L-proline biosynthesis I (from L-glutamate) (EcoCyc)

## Annotation

NAD-P-OR-NOP + PRO -> NADH-P-OR-NOP + L-DELTA1-PYRROLINE_5-CARBOXYLATE + PROTON; direction=RIGHT-TO-LEFT

## Pathways

- `ecocyc.PROSYN-PWY` L-proline biosynthesis I (from L-glutamate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.PYRROLINECARBREDUCT-CPLX|complex.ecocyc.PYRROLINECARBREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03912|molecule.C03912]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00148|molecule.C00148]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00148|molecule.C00148]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PYRROLINECARBREDUCT-RXN`

## Notes

NAD-P-OR-NOP + PRO -> NADH-P-OR-NOP + L-DELTA1-PYRROLINE_5-CARBOXYLATE + PROTON; direction=RIGHT-TO-LEFT
