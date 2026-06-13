---
entity_id: "reaction.ecocyc.RXN0-1922"
entity_type: "reaction"
name: "RXN0-1922"
source_database: "EcoCyc"
source_id: "RXN0-1922"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1922

`reaction.ecocyc.RXN0-1922`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1922`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-8521 + WATER -> DNA-containing-abasic-Sites + Modified-Bases; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-8521 + WATER -> DNA-containing-abasic-Sites + Modified-Bases; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mug (protein.P0A9H1). Substrates: H2O (molecule.C00001). Products: a modified nucleobase (molecule.ecocyc.Modified-Bases).

## Annotation

CPD-8521 + WATER -> DNA-containing-abasic-Sites + Modified-Bases; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A9H1|protein.P0A9H1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Modified-Bases|molecule.ecocyc.Modified-Bases]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1922`

## Notes

CPD-8521 + WATER -> DNA-containing-abasic-Sites + Modified-Bases; direction=PHYSIOL-LEFT-TO-RIGHT
