---
entity_id: "reaction.ecocyc.PRPPSYN-RXN"
entity_type: "reaction"
name: "PRPPSYN-RXN"
source_database: "EcoCyc"
source_id: "PRPPSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PRPPSYN-RXN

`reaction.ecocyc.PRPPSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PRPPSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction synthesizes phosphoribosylpyrophosphate (PRPP). EcoCyc reaction equation: RIBOSE-5P + ATP -> PROTON + PRPP + AMP; direction=LEFT-TO-RIGHT. This reaction synthesizes phosphoribosylpyrophosphate (PRPP).

## Biological Role

Catalyzed by ribose-phosphate diphosphokinase (complex.ecocyc.CPLX0-8299). Substrates: ATP (molecule.C00002), D-Ribose 5-phosphate (molecule.C00117). Products: AMP (molecule.C00020), H+ (molecule.C00080), 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119).

## Enriched Pathways

- `ecocyc.PWY0-662` PRPP biosynthesis (EcoCyc)

## Annotation

This reaction synthesizes phosphoribosylpyrophosphate (PRPP).

## Pathways

- `ecocyc.PWY0-662` PRPP biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `activates` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8299|complex.ecocyc.CPLX0-8299]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00119|molecule.C00119]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00117|molecule.C00117]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1651|molecule.ecocyc.CPD0-1651]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PRPPSYN-RXN`

## Notes

RIBOSE-5P + ATP -> PROTON + PRPP + AMP; direction=LEFT-TO-RIGHT
