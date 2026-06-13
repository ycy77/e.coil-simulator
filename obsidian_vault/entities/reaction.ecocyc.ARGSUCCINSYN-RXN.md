---
entity_id: "reaction.ecocyc.ARGSUCCINSYN-RXN"
entity_type: "reaction"
name: "ARGSUCCINSYN-RXN"
source_database: "EcoCyc"
source_id: "ARGSUCCINSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ARGSUCCINSYN-RXN

`reaction.ecocyc.ARGSUCCINSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ARGSUCCINSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the seventh step in arginine biosynthesis. The enzyme is also involved in the urea cycle. EcoCyc reaction equation: L-ASPARTATE + L-CITRULLINE + ATP -> PROTON + L-ARGININO-SUCCINATE + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the seventh step in arginine biosynthesis. The enzyme is also involved in the urea cycle.

## Biological Role

Catalyzed by argininosuccinate synthetase (complex.ecocyc.CPLX0-238). Substrates: ATP (molecule.C00002), L-Aspartate (molecule.C00049), L-Citrulline (molecule.C00327). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), N-(L-Arginino)succinate (molecule.C03406).

## Enriched Pathways

- `ecocyc.ARGSYN-PWY` L-arginine biosynthesis I (via L-ornithine) (EcoCyc)

## Annotation

This is the seventh step in arginine biosynthesis. The enzyme is also involved in the urea cycle.

## Pathways

- `ecocyc.ARGSYN-PWY` L-arginine biosynthesis I (via L-ornithine) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-238|complex.ecocyc.CPLX0-238]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03406|molecule.C03406]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00327|molecule.C00327]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ARGSUCCINSYN-RXN`

## Notes

L-ASPARTATE + L-CITRULLINE + ATP -> PROTON + L-ARGININO-SUCCINATE + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
