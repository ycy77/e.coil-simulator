---
entity_id: "reaction.ecocyc.1.1.1.83-RXN"
entity_type: "reaction"
name: "1.1.1.83-RXN"
source_database: "EcoCyc"
source_id: "1.1.1.83-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.1.1.83-RXN

`reaction.ecocyc.1.1.1.83-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.1.1.83-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD + CPD-660 -> NADH + CARBON-DIOXIDE + PYRUVATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: NAD + CPD-660 -> NADH + CARBON-DIOXIDE + PYRUVATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dmlA (protein.P76251). Substrates: NAD+ (molecule.C00003), (R)-Malate (molecule.C00497). Products: NADH (molecule.C00004), CO2 (molecule.C00011), Pyruvate (molecule.C00022).

## Enriched Pathways

- `ecocyc.PWY0-1465` D-malate degradation (EcoCyc)

## Annotation

NAD + CPD-660 -> NADH + CARBON-DIOXIDE + PYRUVATE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1465` D-malate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P76251|protein.P76251]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00497|molecule.C00497]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:1.1.1.83-RXN`

## Notes

NAD + CPD-660 -> NADH + CARBON-DIOXIDE + PYRUVATE; direction=LEFT-TO-RIGHT
