---
entity_id: "reaction.ecocyc.2.4.1.230-RXN"
entity_type: "reaction"
name: "2.4.1.230-RXN"
source_database: "EcoCyc"
source_id: "2.4.1.230-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2.4.1.230-RXN

`reaction.ecocyc.2.4.1.230-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.4.1.230-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-16569 + Pi -> Glucopyranose + CPD-448; direction=REVERSIBLE EcoCyc reaction equation: CPD-16569 + Pi -> Glucopyranose + CPD-448; direction=REVERSIBLE.

## Biological Role

Catalyzed by ycjT (protein.P77154). Substrates: kojibiose (molecule.ecocyc.CPD-16569), phosphate (molecule.ecocyc.Pi). Products: D-Glucose (molecule.C00031), beta-D-Glucose 1-phosphate (molecule.C00663).

## Annotation

CPD-16569 + Pi -> Glucopyranose + CPD-448; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P77154|protein.P77154]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00663|molecule.C00663]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-16569|molecule.ecocyc.CPD-16569]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.4.1.230-RXN`

## Notes

CPD-16569 + Pi -> Glucopyranose + CPD-448; direction=REVERSIBLE
