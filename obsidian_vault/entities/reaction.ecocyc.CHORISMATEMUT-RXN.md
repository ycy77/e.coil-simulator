---
entity_id: "reaction.ecocyc.CHORISMATEMUT-RXN"
entity_type: "reaction"
name: "CHORISMATEMUT-RXN"
source_database: "EcoCyc"
source_id: "CHORISMATEMUT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CHORISMATEMUT-RXN

`reaction.ecocyc.CHORISMATEMUT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CHORISMATEMUT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the first step after the chorismate branch point in the biosynthesis of both phenylalanine and tyrosine. EcoCyc reaction equation: CHORISMATE -> PREPHENATE; direction=LEFT-TO-RIGHT. This reaction is the first step after the chorismate branch point in the biosynthesis of both phenylalanine and tyrosine.

## Biological Role

Catalyzed by fused chorismate mutase/prephenate dehydratase (complex.ecocyc.CHORISMUTPREPHENDEHYDRAT-CPLX), fused chorismate mutase/prephenate dehydrogenase (complex.ecocyc.CHORISMUTPREPHENDEHYDROG-CPLX). Substrates: Chorismate (molecule.C00251). Products: Prephenate (molecule.C00254).

## Enriched Pathways

- `ecocyc.PHESYN` L-phenylalanine biosynthesis I (EcoCyc)
- `ecocyc.TYRSYN` L-tyrosine biosynthesis I (EcoCyc)

## Annotation

This reaction is the first step after the chorismate branch point in the biosynthesis of both phenylalanine and tyrosine.

## Pathways

- `ecocyc.PHESYN` L-phenylalanine biosynthesis I (EcoCyc)
- `ecocyc.TYRSYN` L-tyrosine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.CHORISMUTPREPHENDEHYDRAT-CPLX|complex.ecocyc.CHORISMUTPREPHENDEHYDRAT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CHORISMUTPREPHENDEHYDROG-CPLX|complex.ecocyc.CHORISMUTPREPHENDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00254|molecule.C00254]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00251|molecule.C00251]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00079|molecule.C00079]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00158|molecule.C00158]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00254|molecule.C00254]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C03196|molecule.C03196]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-12153|molecule.ecocyc.CPD-12153]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CHORISMATEMUT-RXN`

## Notes

CHORISMATE -> PREPHENATE; direction=LEFT-TO-RIGHT
