---
entity_id: "reaction.ecocyc.DEOXYGUANPHOSPHOR-RXN"
entity_type: "reaction"
name: "DEOXYGUANPHOSPHOR-RXN"
source_database: "EcoCyc"
source_id: "DEOXYGUANPHOSPHOR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DEOXYGUANPHOSPHOR-RXN

`reaction.ecocyc.DEOXYGUANPHOSPHOR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DEOXYGUANPHOSPHOR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DEOXYGUANOSINE + Pi -> GUANINE + DEOXY-D-RIBOSE-1-PHOSPHATE; direction=REVERSIBLE EcoCyc reaction equation: DEOXYGUANOSINE + Pi -> GUANINE + DEOXY-D-RIBOSE-1-PHOSPHATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by purine nucleoside phosphorylase (complex.ecocyc.DEOD-CPLX). Substrates: Deoxyguanosine (molecule.C00330), phosphate (molecule.ecocyc.Pi). Products: Guanine (molecule.C00242), 2-Deoxy-D-ribose 1-phosphate (molecule.C00672).

## Enriched Pathways

- `ecocyc.PWY-7179` purine deoxyribonucleosides degradation I (EcoCyc)

## Annotation

DEOXYGUANOSINE + Pi -> GUANINE + DEOXY-D-RIBOSE-1-PHOSPHATE; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-7179` purine deoxyribonucleosides degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.DEOD-CPLX|complex.ecocyc.DEOD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00242|molecule.C00242]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00672|molecule.C00672]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00330|molecule.C00330]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00212|molecule.C00212]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DEOXYGUANPHOSPHOR-RXN`

## Notes

DEOXYGUANOSINE + Pi -> GUANINE + DEOXY-D-RIBOSE-1-PHOSPHATE; direction=REVERSIBLE
