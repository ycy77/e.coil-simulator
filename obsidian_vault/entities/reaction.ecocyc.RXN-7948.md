---
entity_id: "reaction.ecocyc.RXN-7948"
entity_type: "reaction"
name: "RXN-7948"
source_database: "EcoCyc"
source_id: "RXN-7948"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-7948

`reaction.ecocyc.RXN-7948`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-7948`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

PHOSPHORYL-ETHANOLAMINE + WATER -> ETHANOL-AMINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PHOSPHORYL-ETHANOLAMINE + WATER -> ETHANOL-AMINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), Ethanolamine phosphate (molecule.C00346). Products: Ethanolamine (molecule.C00189), phosphate (molecule.ecocyc.Pi).

## Annotation

PHOSPHORYL-ETHANOLAMINE + WATER -> ETHANOL-AMINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00189|molecule.C00189]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00346|molecule.C00346]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-7948`

## Notes

PHOSPHORYL-ETHANOLAMINE + WATER -> ETHANOL-AMINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
