---
entity_id: "reaction.ecocyc.2.7.9.3-RXN"
entity_type: "reaction"
name: "2.7.9.3-RXN"
source_database: "EcoCyc"
source_id: "2.7.9.3-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Selenophosphate synthetase"
  - "Selenophosphate synthase"
  - "Selenium donor protein"
---

# 2.7.9.3-RXN

`reaction.ecocyc.2.7.9.3-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.7.9.3-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + SE-2 + ATP -> Pi + SEPO3 + AMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + SE-2 + ATP -> Pi + SEPO3 + AMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by selenide, water dikinase (complex.ecocyc.CPLX0-7957). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), selenide (molecule.ecocyc.SE-2). Products: AMP (molecule.C00020), Selenophosphoric acid (molecule.C05172), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY0-901` L-selenocysteine biosynthesis I (bacteria) (EcoCyc)

## Annotation

WATER + SE-2 + ATP -> Pi + SEPO3 + AMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-901` L-selenocysteine biosynthesis I (bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7957|complex.ecocyc.CPLX0-7957]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05172|molecule.C05172]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.SE-2|molecule.ecocyc.SE-2]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:2.7.9.3-RXN`

## Notes

WATER + SE-2 + ATP -> Pi + SEPO3 + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
