---
entity_id: "reaction.ecocyc.DIHYDROOROT-RXN"
entity_type: "reaction"
name: "DIHYDROOROT-RXN"
source_database: "EcoCyc"
source_id: "DIHYDROOROT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIHYDROOROT-RXN

`reaction.ecocyc.DIHYDROOROT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIHYDROOROT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third step in pyrimidine biosynthesis. EcoCyc reaction equation: DI-H-OROTATE + WATER -> PROTON + CARBAMYUL-L-ASPARTATE; direction=REVERSIBLE. This is the third step in pyrimidine biosynthesis.

## Biological Role

Catalyzed by dihydroorotase (complex.ecocyc.DIHYDROOROT-CPLX). Substrates: H2O (molecule.C00001), (S)-Dihydroorotate (molecule.C00337). Products: H+ (molecule.C00080), N-Carbamoyl-L-aspartate (molecule.C00438).

## Enriched Pathways

- `ecocyc.PWY-5686` UMP biosynthesis I (EcoCyc)

## Annotation

This is the third step in pyrimidine biosynthesis.

## Pathways

- `ecocyc.PWY-5686` UMP biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.DIHYDROOROT-CPLX|complex.ecocyc.DIHYDROOROT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00438|molecule.C00438]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00337|molecule.C00337]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DIHYDROOROT-RXN`

## Notes

DI-H-OROTATE + WATER -> PROTON + CARBAMYUL-L-ASPARTATE; direction=REVERSIBLE
