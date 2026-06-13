---
entity_id: "reaction.ecocyc.RIBOFLAVIN-SYN-RXN"
entity_type: "reaction"
name: "RIBOFLAVIN-SYN-RXN"
source_database: "EcoCyc"
source_id: "RIBOFLAVIN-SYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RIBOFLAVIN-SYN-RXN

`reaction.ecocyc.RIBOFLAVIN-SYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RIBOFLAVIN-SYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Final step of riboflavin synthesis. EcoCyc reaction equation: PROTON + DIMETHYL-D-RIBITYL-LUMAZINE -> AMINO-RIBOSYLAMINO-1H-3H-PYR-DIONE + RIBOFLAVIN; direction=LEFT-TO-RIGHT. Final step of riboflavin synthesis.

## Biological Role

Catalyzed by riboflavin synthase (complex.ecocyc.CPLX0-3952). Substrates: H+ (molecule.C00080), 6,7-Dimethyl-8-(D-ribityl)lumazine (molecule.C04332). Products: Riboflavin (molecule.C00255), 5-Amino-6-(1-D-ribitylamino)uracil (molecule.C04732).

## Enriched Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Annotation

Final step of riboflavin synthesis.

## Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3952|complex.ecocyc.CPLX0-3952]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00255|molecule.C00255]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04732|molecule.C04732]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04332|molecule.C04332]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RIBOFLAVIN-SYN-RXN`

## Notes

PROTON + DIMETHYL-D-RIBITYL-LUMAZINE -> AMINO-RIBOSYLAMINO-1H-3H-PYR-DIONE + RIBOFLAVIN; direction=LEFT-TO-RIGHT
