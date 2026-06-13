---
entity_id: "reaction.ecocyc.D-PPENTOMUT-RXN"
entity_type: "reaction"
name: "D-deoxyribose 1,5-phosphomutase"
source_database: "EcoCyc"
source_id: "D-PPENTOMUT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-deoxyribose 1,5-phosphomutase

`reaction.ecocyc.D-PPENTOMUT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:D-PPENTOMUT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in the catabolism of ribo- and deoxyribonucleosides. EcoCyc reaction equation: DEOXY-D-RIBOSE-1-PHOSPHATE -> DEOXY-RIBOSE-5P; direction=REVERSIBLE. This reaction is involved in the catabolism of ribo- and deoxyribonucleosides.

## Biological Role

Catalyzed by deoB (protein.P0A6K6). Substrates: 2-Deoxy-D-ribose 1-phosphate (molecule.C00672). Products: 2-Deoxy-D-ribose 5-phosphate (molecule.C00673).

## Enriched Pathways

- `ecocyc.PWY-7180` 2-deoxy-α-D-ribose 1-phosphate degradation (EcoCyc)

## Annotation

This reaction is involved in the catabolism of ribo- and deoxyribonucleosides.

## Pathways

- `ecocyc.PWY-7180` 2-deoxy-α-D-ribose 1-phosphate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `activates` <-- [[molecule.C01151|molecule.C01151]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CPD-16577|molecule.ecocyc.CPD-16577]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P0A6K6|protein.P0A6K6]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00673|molecule.C00673]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00672|molecule.C00672]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00059|molecule.C00059]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C14819|molecule.C14819]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:D-PPENTOMUT-RXN`

## Notes

DEOXY-D-RIBOSE-1-PHOSPHATE -> DEOXY-RIBOSE-5P; direction=REVERSIBLE
