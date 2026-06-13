---
entity_id: "reaction.ecocyc.RXN-19793"
entity_type: "reaction"
name: "RXN-19793"
source_database: "EcoCyc"
source_id: "RXN-19793"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19793

`reaction.ecocyc.RXN-19793`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19793`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-21409 + WATER -> CPD-21407 + CPD-21406; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-21409 + WATER -> CPD-21407 + CPD-21406; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pgaB (protein.P75906). Substrates: H2O (molecule.C00001), a partially deacetylated poly-β-1,6-N-acetyl-D-glucosamine I (molecule.ecocyc.CPD-21409). Products: a partially deacetylated poly-β-1,6-N-acetyl-D-glucosamine (fragment 1) (molecule.ecocyc.CPD-21406), a partially deacetylated poly-β-1,6-N-acetyl-D-glucosamine (fragment 2) (molecule.ecocyc.CPD-21407).

## Annotation

CPD-21409 + WATER -> CPD-21407 + CPD-21406; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P75906|protein.P75906]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-21406|molecule.ecocyc.CPD-21406]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21407|molecule.ecocyc.CPD-21407]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21409|molecule.ecocyc.CPD-21409]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19793`

## Notes

CPD-21409 + WATER -> CPD-21407 + CPD-21406; direction=PHYSIOL-LEFT-TO-RIGHT
