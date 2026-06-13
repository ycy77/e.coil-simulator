---
entity_id: "reaction.ecocyc.DAHPSYN-RXN"
entity_type: "reaction"
name: "DAHPSYN-RXN"
source_database: "EcoCyc"
source_id: "DAHPSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DAHPSYN-RXN

`reaction.ecocyc.DAHPSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DAHPSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The first committed step in the biosynthesis of aromatic compounds EcoCyc reaction equation: PHOSPHO-ENOL-PYRUVATE + ERYTHROSE-4P + WATER -> 3-DEOXY-D-ARABINO-HEPTULOSONATE-7-P + Pi; direction=LEFT-TO-RIGHT. The first committed step in the biosynthesis of aromatic compounds

## Biological Role

Catalyzed by 3-deoxy-7-phosphoheptulonate synthase (complex.ecocyc.AROF-CPLX), 3-deoxy-7-phosphoheptulonate synthase (complex.ecocyc.AROG-CPLX), 3-deoxy-7-phosphoheptulonate synthase (complex.ecocyc.AROH-CPLX). Substrates: H2O (molecule.C00001), Phosphoenolpyruvate (molecule.C00074), D-Erythrose 4-phosphate (molecule.C00279). Products: 2-Dehydro-3-deoxy-D-arabino-heptonate 7-phosphate (molecule.C04691), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6164` 3-dehydroquinate biosynthesis I (EcoCyc)

## Annotation

The first committed step in the biosynthesis of aromatic compounds

## Pathways

- `ecocyc.PWY-6164` 3-dehydroquinate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (21)

- `activates` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.AROF-CPLX|complex.ecocyc.AROF-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.AROG-CPLX|complex.ecocyc.AROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.AROH-CPLX|complex.ecocyc.AROH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04691|molecule.C04691]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00279|molecule.C00279]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00078|molecule.C00078]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00079|molecule.C00079]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00631|molecule.C00631]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01159|molecule.C01159]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C04691|molecule.C04691]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1554|molecule.ecocyc.CPD0-1554]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1555|molecule.ecocyc.CPD0-1555]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1557|molecule.ecocyc.CPD0-1557]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1558|molecule.ecocyc.CPD0-1558]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DAHPSYN-RXN`

## Notes

PHOSPHO-ENOL-PYRUVATE + ERYTHROSE-4P + WATER -> 3-DEOXY-D-ARABINO-HEPTULOSONATE-7-P + Pi; direction=LEFT-TO-RIGHT
