---
entity_id: "reaction.ecocyc.ACETYLORNDEACET-RXN"
entity_type: "reaction"
name: "ACETYLORNDEACET-RXN"
source_database: "EcoCyc"
source_id: "ACETYLORNDEACET-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACETYLORNDEACET-RXN

`reaction.ecocyc.ACETYLORNDEACET-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACETYLORNDEACET-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fifth step in arginine biosynthesis. EcoCyc reaction equation: N-ALPHA-ACETYLORNITHINE + WATER -> L-ORNITHINE + ACET; direction=LEFT-TO-RIGHT. This is the fifth step in arginine biosynthesis.

## Biological Role

Catalyzed by acetylornithine deacetylase (complex.ecocyc.ACETYLORNDEACET-CPLX). Substrates: H2O (molecule.C00001), N-Acetylornithine (molecule.C00437). Products: Acetate (molecule.C00033), L-Ornithine (molecule.C00077).

## Enriched Pathways

- `ecocyc.GLUTORN-PWY` L-ornithine biosynthesis I (EcoCyc)

## Annotation

This is the fifth step in arginine biosynthesis.

## Pathways

- `ecocyc.GLUTORN-PWY` L-ornithine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (18)

- `activates` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.ACETYLORNDEACET-CPLX|complex.ecocyc.ACETYLORNDEACET-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00077|molecule.C00077]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00437|molecule.C00437]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00077|molecule.C00077]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1641|molecule.ecocyc.CPD0-1641]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.NaF|molecule.ecocyc.NaF]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Sulfhydryl-Reagents|molecule.ecocyc.Sulfhydryl-Reagents]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ACETYLORNDEACET-RXN`

## Notes

N-ALPHA-ACETYLORNITHINE + WATER -> L-ORNITHINE + ACET; direction=LEFT-TO-RIGHT
