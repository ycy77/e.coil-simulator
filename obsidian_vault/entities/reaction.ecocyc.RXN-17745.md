---
entity_id: "reaction.ecocyc.RXN-17745"
entity_type: "reaction"
name: "RXN-17745"
source_database: "EcoCyc"
source_id: "RXN-17745"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17745

`reaction.ecocyc.RXN-17745`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17745`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

D-GLUCOSAMINE-6-P + WATER -> GLUCOSAMINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-GLUCOSAMINE-6-P + WATER -> GLUCOSAMINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), D-Glucosamine 6-phosphate (molecule.C00352). Products: D-Glucosamine (molecule.C00329), phosphate (molecule.ecocyc.Pi).

## Annotation

D-GLUCOSAMINE-6-P + WATER -> GLUCOSAMINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00329|molecule.C00329]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00352|molecule.C00352]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17745`

## Notes

D-GLUCOSAMINE-6-P + WATER -> GLUCOSAMINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
