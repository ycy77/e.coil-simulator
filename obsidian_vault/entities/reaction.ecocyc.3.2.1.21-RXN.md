---
entity_id: "reaction.ecocyc.3.2.1.21-RXN"
entity_type: "reaction"
name: "3.2.1.21-RXN"
source_database: "EcoCyc"
source_id: "3.2.1.21-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Gentobiase"
  - "Cellobiase"
  - "Amygdalase"
  - "&beta"
  - "-D-glucosidase"
---

# 3.2.1.21-RXN

`reaction.ecocyc.3.2.1.21-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.2.1.21-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

Beta-D-glucosides + WATER -> Non-Glucosylated-Glucose-Acceptors + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Beta-D-glucosides + WATER -> Non-Glucosylated-Glucose-Acceptors + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), beta-D-Glucoside (molecule.C00963). Products: D-Glucose (molecule.C00031).

## Annotation

Beta-D-glucosides + WATER -> Non-Glucosylated-Glucose-Acceptors + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00963|molecule.C00963]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.2.1.21-RXN`

## Notes

Beta-D-glucosides + WATER -> Non-Glucosylated-Glucose-Acceptors + Glucopyranose; direction=PHYSIOL-LEFT-TO-RIGHT
