---
entity_id: "reaction.ecocyc.AMYLOMALT-RXN"
entity_type: "reaction"
name: "AMYLOMALT-RXN"
source_database: "EcoCyc"
source_id: "AMYLOMALT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# AMYLOMALT-RXN

`reaction.ecocyc.AMYLOMALT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:AMYLOMALT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes maltodextrins of longer length. In general the reaction transfers a segment of a 1,4-α-D-glucan to a new 4-position in an acceptor, which may be glucose or 1,4-α-D-glucan. EcoCyc reaction equation: MALTOTETRAOSE + Glucopyranose -> MALTOTRIOSE + MALTOSE; direction=REVERSIBLE. This reaction synthesizes maltodextrins of longer length. In general the reaction transfers a segment of a 1,4-α-D-glucan to a new 4-position in an acceptor, which may be glucose or 1,4-α-D-glucan.

## Biological Role

Catalyzed by malQ (protein.P15977). Substrates: D-Glucose (molecule.C00031), maltotetraose (molecule.ecocyc.MALTOTETRAOSE). Products: Maltose (molecule.C00208), Maltotriose (molecule.C01835).

## Enriched Pathways

- `ecocyc.GLYCOCAT-PWY` glycogen degradation I (EcoCyc)

## Annotation

This reaction synthesizes maltodextrins of longer length. In general the reaction transfers a segment of a 1,4-α-D-glucan to a new 4-position in an acceptor, which may be glucose or 1,4-α-D-glucan.

## Pathways

- `ecocyc.GLYCOCAT-PWY` glycogen degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (16)

- `catalyzes` <-- [[protein.P15977|protein.P15977]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00208|molecule.C00208]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01835|molecule.C01835]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MALTOTETRAOSE|molecule.ecocyc.MALTOTETRAOSE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-3570|molecule.ecocyc.CPD-3570]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-3582|molecule.ecocyc.CPD-3582]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1667|molecule.ecocyc.CPD0-1667]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1668|molecule.ecocyc.CPD0-1668]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1669|molecule.ecocyc.CPD0-1669]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:AMYLOMALT-RXN`

## Notes

MALTOTETRAOSE + Glucopyranose -> MALTOTRIOSE + MALTOSE; direction=REVERSIBLE
