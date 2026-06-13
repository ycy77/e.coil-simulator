---
entity_id: "reaction.ecocyc.2.9.1.1-RXN"
entity_type: "reaction"
name: "2.9.1.1-RXN"
source_database: "EcoCyc"
source_id: "2.9.1.1-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Selenocysteine synthase"
  - "L-selenocysteinyl-tRNA(Sel) synthase"
  - "L-selenocysteinyl-tRNA(Sec) synthase"
  - "Cysteinyl-tRNA(Sel)-selenium transferase"
  - "Cysteinyl-tRNA(Sec)-selenium transferase"
---

# 2.9.1.1-RXN

`reaction.ecocyc.2.9.1.1-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.9.1.1-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SEPO3 + L-seryl-SEC-tRNAs -> Pi + Charged-SEC-tRNAs; direction=LEFT-TO-RIGHT EcoCyc reaction equation: SEPO3 + L-seryl-SEC-tRNAs -> Pi + Charged-SEC-tRNAs; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by selenocysteine synthase (complex.ecocyc.CPLX0-1141). Substrates: Selenophosphoric acid (molecule.C05172). Products: phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY0-901` L-selenocysteine biosynthesis I (bacteria) (EcoCyc)

## Annotation

SEPO3 + L-seryl-SEC-tRNAs -> Pi + Charged-SEC-tRNAs; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-901` L-selenocysteine biosynthesis I (bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1141|complex.ecocyc.CPLX0-1141]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05172|molecule.C05172]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.BOROHYDRIDE|molecule.ecocyc.BOROHYDRIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-13584|molecule.ecocyc.CPD-13584]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:2.9.1.1-RXN`

## Notes

SEPO3 + L-seryl-SEC-tRNAs -> Pi + Charged-SEC-tRNAs; direction=LEFT-TO-RIGHT
