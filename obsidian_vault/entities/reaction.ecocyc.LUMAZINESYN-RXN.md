---
entity_id: "reaction.ecocyc.LUMAZINESYN-RXN"
entity_type: "reaction"
name: "LUMAZINESYN-RXN"
source_database: "EcoCyc"
source_id: "LUMAZINESYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# LUMAZINESYN-RXN

`reaction.ecocyc.LUMAZINESYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LUMAZINESYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the sixth step in the biosynthesis of riboflavin. EcoCyc reaction equation: AMINO-RIBOSYLAMINO-1H-3H-PYR-DIONE + DIHYDROXY-BUTANONE-P -> PROTON + DIMETHYL-D-RIBITYL-LUMAZINE + Pi + WATER; direction=LEFT-TO-RIGHT. This reaction is the sixth step in the biosynthesis of riboflavin.

## Biological Role

Catalyzed by 6,7-dimethyl-8-ribityllumazine synthase (complex.ecocyc.LUMAZINESYN-CPLX). Substrates: 5-Amino-6-(1-D-ribitylamino)uracil (molecule.C04732), L-3,4-Dihydroxybutan-2-one 4-phosphate (molecule.C15556). Products: H2O (molecule.C00001), H+ (molecule.C00080), 6,7-Dimethyl-8-(D-ribityl)lumazine (molecule.C04332), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Annotation

This reaction is the sixth step in the biosynthesis of riboflavin.

## Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.LUMAZINESYN-CPLX|complex.ecocyc.LUMAZINESYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04332|molecule.C04332]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04732|molecule.C04732]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C15556|molecule.C15556]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:LUMAZINESYN-RXN`

## Notes

AMINO-RIBOSYLAMINO-1H-3H-PYR-DIONE + DIHYDROXY-BUTANONE-P -> PROTON + DIMETHYL-D-RIBITYL-LUMAZINE + Pi + WATER; direction=LEFT-TO-RIGHT
