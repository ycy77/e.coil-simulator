---
entity_id: "reaction.ecocyc.PORPHOBILSYNTH-RXN"
entity_type: "reaction"
name: "PORPHOBILSYNTH-RXN"
source_database: "EcoCyc"
source_id: "PORPHOBILSYNTH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "&delta"
  - "-AMINOLEVULINIC ACID DEHYDRATASE"
  - "AMINOLEVULINATE DEHYDRATASE"
---

# PORPHOBILSYNTH-RXN

`reaction.ecocyc.PORPHOBILSYNTH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PORPHOBILSYNTH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of porphyrin biosynthesis. EcoCyc reaction equation: 5-AMINO-LEVULINATE -> PROTON + WATER + PORPHOBILINOGEN; direction=LEFT-TO-RIGHT. This reaction is part of porphyrin biosynthesis.

## Biological Role

Catalyzed by porphobilinogen synthase (complex.ecocyc.PORPHOBILSYNTH-CPLX). Substrates: 5-Aminolevulinate (molecule.C00430). Products: H2O (molecule.C00001), H+ (molecule.C00080), Porphobilinogen (molecule.C00931).

## Enriched Pathways

- `ecocyc.PWY-5188` uroporphyrinogen-III I (from glutamate) (EcoCyc)

## Annotation

This reaction is part of porphyrin biosynthesis.

## Pathways

- `ecocyc.PWY-5188` uroporphyrinogen-III I (from glutamate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.PORPHOBILSYNTH-CPLX|complex.ecocyc.PORPHOBILSYNTH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00931|molecule.C00931]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00430|molecule.C00430]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PORPHOBILSYNTH-RXN`

## Notes

5-AMINO-LEVULINATE -> PROTON + WATER + PORPHOBILINOGEN; direction=LEFT-TO-RIGHT
