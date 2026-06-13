---
entity_id: "reaction.ecocyc.RXN0-6562"
entity_type: "reaction"
name: "RXN0-6562"
source_database: "EcoCyc"
source_id: "RXN0-6562"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6562

`reaction.ecocyc.RXN0-6562`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6562`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-P-HYDROXYPYRUVATE + WATER -> OH-PYR + Pi; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 3-P-HYDROXYPYRUVATE + WATER -> OH-PYR + Pi; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by nudL (protein.P43337). Substrates: H2O (molecule.C00001), 3-Phosphonooxypyruvate (molecule.C03232). Products: Hydroxypyruvate (molecule.C00168), phosphate (molecule.ecocyc.Pi).

## Annotation

3-P-HYDROXYPYRUVATE + WATER -> OH-PYR + Pi; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P43337|protein.P43337]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00168|molecule.C00168]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03232|molecule.C03232]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6562`

## Notes

3-P-HYDROXYPYRUVATE + WATER -> OH-PYR + Pi; direction=LEFT-TO-RIGHT
