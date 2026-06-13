---
entity_id: "reaction.ecocyc.FUCPALDOL-RXN"
entity_type: "reaction"
name: "FUCPALDOL-RXN"
source_database: "EcoCyc"
source_id: "FUCPALDOL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# FUCPALDOL-RXN

`reaction.ecocyc.FUCPALDOL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FUCPALDOL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The third step in fucose catabolism. EcoCyc reaction equation: FUCULOSE-1P -> LACTALD + DIHYDROXY-ACETONE-PHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT. The third step in fucose catabolism.

## Biological Role

Catalyzed by L-fuculose-phosphate aldolase (complex.ecocyc.CPLX0-7633). Substrates: L-Fuculose 1-phosphate (molecule.C01099). Products: Glycerone phosphate (molecule.C00111), (S)-Lactaldehyde (molecule.C00424).

## Enriched Pathways

- `ecocyc.FUCCAT-PWY` L-fucose degradation I (EcoCyc)

## Annotation

The third step in fucose catabolism.

## Pathways

- `ecocyc.FUCCAT-PWY` L-fucose degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7633|complex.ecocyc.CPLX0-7633]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00424|molecule.C00424]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01099|molecule.C01099]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1102|molecule.ecocyc.CPD0-1102]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:FUCPALDOL-RXN`

## Notes

FUCULOSE-1P -> LACTALD + DIHYDROXY-ACETONE-PHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT
