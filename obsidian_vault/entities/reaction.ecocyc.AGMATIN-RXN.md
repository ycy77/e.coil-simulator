---
entity_id: "reaction.ecocyc.AGMATIN-RXN"
entity_type: "reaction"
name: "AGMATIN-RXN"
source_database: "EcoCyc"
source_id: "AGMATIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# AGMATIN-RXN

`reaction.ecocyc.AGMATIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:AGMATIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of putrescine and spermidine biosynthesis. EcoCyc reaction equation: WATER + AGMATHINE -> UREA + PUTRESCINE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of putrescine and spermidine biosynthesis.

## Biological Role

Catalyzed by agmatinase (complex.ecocyc.AGMATIN-CPLX). Substrates: H2O (molecule.C00001), Agmatine (molecule.C00179). Products: Urea (molecule.C00086), Putrescine (molecule.C00134).

## Enriched Pathways

- `ecocyc.PWY-40` putrescine biosynthesis I (EcoCyc)
- `ecocyc.PWY0-823` L-arginine degradation III (arginine decarboxylase/agmatinase pathway) (EcoCyc)

## Annotation

This reaction is part of putrescine and spermidine biosynthesis.

## Pathways

- `ecocyc.PWY-40` putrescine biosynthesis I (EcoCyc)
- `ecocyc.PWY0-823` L-arginine degradation III (arginine decarboxylase/agmatinase pathway) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `catalyzes` <-- [[complex.ecocyc.AGMATIN-CPLX|complex.ecocyc.AGMATIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00086|molecule.C00086]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00179|molecule.C00179]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00062|molecule.C00062]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00077|molecule.C00077]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1470|molecule.ecocyc.CPD0-1470]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EGTA|molecule.ecocyc.EGTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:AGMATIN-RXN`

## Notes

WATER + AGMATHINE -> UREA + PUTRESCINE; direction=PHYSIOL-LEFT-TO-RIGHT
