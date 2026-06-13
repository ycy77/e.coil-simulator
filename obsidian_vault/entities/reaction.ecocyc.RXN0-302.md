---
entity_id: "reaction.ecocyc.RXN0-302"
entity_type: "reaction"
name: "RXN0-302"
source_database: "EcoCyc"
source_id: "RXN0-302"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-302

`reaction.ecocyc.RXN0-302`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-302`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-PHOSPHO-4-CYTIDINE-5-DIPHOSPHO-2-C-MET -> CMP + 2C-METH-D-ERYTHRITOL-CYCLODIPHOSPHATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 2-PHOSPHO-4-CYTIDINE-5-DIPHOSPHO-2-C-MET -> CMP + 2C-METH-D-ERYTHRITOL-CYCLODIPHOSPHATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase (complex.ecocyc.CPLX0-721). Substrates: 2-Phospho-4-(cytidine 5'-diphospho)-2-C-methyl-D-erythritol (molecule.C11436). Products: CMP (molecule.C00055), 2-C-Methyl-D-erythritol 2,4-cyclodiphosphate (molecule.C11453).

## Enriched Pathways

- `ecocyc.NONMEVIPP-PWY` methylerythritol phosphate pathway I (EcoCyc)

## Annotation

2-PHOSPHO-4-CYTIDINE-5-DIPHOSPHO-2-C-MET -> CMP + 2C-METH-D-ERYTHRITOL-CYCLODIPHOSPHATE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.NONMEVIPP-PWY` methylerythritol phosphate pathway I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-721|complex.ecocyc.CPLX0-721]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C11453|molecule.C11453]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C11436|molecule.C11436]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-302`

## Notes

2-PHOSPHO-4-CYTIDINE-5-DIPHOSPHO-2-C-MET -> CMP + 2C-METH-D-ERYTHRITOL-CYCLODIPHOSPHATE; direction=LEFT-TO-RIGHT
