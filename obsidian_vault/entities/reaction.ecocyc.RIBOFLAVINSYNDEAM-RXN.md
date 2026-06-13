---
entity_id: "reaction.ecocyc.RIBOFLAVINSYNDEAM-RXN"
entity_type: "reaction"
name: "RIBOFLAVINSYNDEAM-RXN"
source_database: "EcoCyc"
source_id: "RIBOFLAVINSYNDEAM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RIBOFLAVINSYNDEAM-RXN

`reaction.ecocyc.RIBOFLAVINSYNDEAM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:RIBOFLAVINSYNDEAM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of riboflavin biosynthesis. EcoCyc reaction equation: PROTON + WATER + DIAMINO-OH-PHOSPHORIBOSYLAMINO-PYR -> CPD-602 + AMMONIUM; direction=LEFT-TO-RIGHT. This reaction is part of riboflavin biosynthesis.

## Biological Role

Catalyzed by fused diaminohydroxyphosphoribosylaminopyrimidine deaminase / 5-amino-6-(5-phosphoribosylamino)uracil reductase (complex.ecocyc.CPLX0-7659). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), 2,5-Diamino-6-(5-phospho-D-ribosylamino)pyrimidin-4(3H)-one (molecule.C01304). Products: 5-Amino-6-(5'-phosphoribosylamino)uracil (molecule.C01268), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Annotation

This reaction is part of riboflavin biosynthesis.

## Pathways

- `ecocyc.RIBOSYN2-PWY` flavin biosynthesis I (bacteria and plants) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7659|complex.ecocyc.CPLX0-7659]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01268|molecule.C01268]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01304|molecule.C01304]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RIBOFLAVINSYNDEAM-RXN`

## Notes

PROTON + WATER + DIAMINO-OH-PHOSPHORIBOSYLAMINO-PYR -> CPD-602 + AMMONIUM; direction=LEFT-TO-RIGHT
