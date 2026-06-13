---
entity_id: "reaction.ecocyc.PHOSPHOENOLPYRUVATE-PHOSPHATASE-RXN"
entity_type: "reaction"
name: "PHOSPHOENOLPYRUVATE-PHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "PHOSPHOENOLPYRUVATE-PHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PHOSPHOENOLPYRUVATE-PHOSPHATASE-RXN

`reaction.ecocyc.PHOSPHOENOLPYRUVATE-PHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHOSPHOENOLPYRUVATE-PHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

WATER + PHOSPHO-ENOL-PYRUVATE -> PYRUVATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + PHOSPHO-ENOL-PYRUVATE -> PYRUVATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), Phosphoenolpyruvate (molecule.C00074). Products: Pyruvate (molecule.C00022), phosphate (molecule.ecocyc.Pi).

## Annotation

WATER + PHOSPHO-ENOL-PYRUVATE -> PYRUVATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PHOSPHOENOLPYRUVATE-PHOSPHATASE-RXN`

## Notes

WATER + PHOSPHO-ENOL-PYRUVATE -> PYRUVATE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
