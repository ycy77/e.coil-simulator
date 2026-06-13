---
entity_id: "reaction.ecocyc.RXN-5647"
entity_type: "reaction"
name: "RXN-5647"
source_database: "EcoCyc"
source_id: "RXN-5647"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-5647

`reaction.ecocyc.RXN-5647`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-5647`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

PHOSPHORYL-CHOLINE + WATER -> CHOLINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PHOSPHORYL-CHOLINE + WATER -> CHOLINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX). Substrates: H2O (molecule.C00001), Choline phosphate (molecule.C00588). Products: Choline (molecule.C00114), phosphate (molecule.ecocyc.Pi).

## Annotation

PHOSPHORYL-CHOLINE + WATER -> CHOLINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00114|molecule.C00114]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00588|molecule.C00588]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-5647`

## Notes

PHOSPHORYL-CHOLINE + WATER -> CHOLINE + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
