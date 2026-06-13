---
entity_id: "reaction.ecocyc.SUCCDIAMINOPIMDESUCC-RXN"
entity_type: "reaction"
name: "SUCCDIAMINOPIMDESUCC-RXN"
source_database: "EcoCyc"
source_id: "SUCCDIAMINOPIMDESUCC-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SUCCDIAMINOPIMDESUCC-RXN

`reaction.ecocyc.SUCCDIAMINOPIMDESUCC-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SUCCDIAMINOPIMDESUCC-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fifth step in the biosynthesis of diaminopimelate and lysine. EcoCyc reaction equation: WATER + N-SUCCINYLLL-2-6-DIAMINOPIMELATE -> LL-DIAMINOPIMELATE + SUC; direction=LEFT-TO-RIGHT. This is the fifth step in the biosynthesis of diaminopimelate and lysine.

## Biological Role

Catalyzed by succinyl-diaminopimelate desuccinylase (complex.ecocyc.CPLX0-3161). Substrates: H2O (molecule.C00001), N-Succinyl-LL-2,6-diaminoheptanedioate (molecule.C04421). Products: Succinate (molecule.C00042), LL-2,6-Diaminoheptanedioate (molecule.C00666).

## Enriched Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)

## Annotation

This is the fifth step in the biosynthesis of diaminopimelate and lysine.

## Pathways

- `ecocyc.DAPLYSINESYN-PWY` L-lysine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3161|complex.ecocyc.CPLX0-3161]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00666|molecule.C00666]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04421|molecule.C04421]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:SUCCDIAMINOPIMDESUCC-RXN`

## Notes

WATER + N-SUCCINYLLL-2-6-DIAMINOPIMELATE -> LL-DIAMINOPIMELATE + SUC; direction=LEFT-TO-RIGHT
