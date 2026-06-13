---
entity_id: "reaction.ecocyc.6PGLUCONOLACT-RXN"
entity_type: "reaction"
name: "6PGLUCONOLACT-RXN"
source_database: "EcoCyc"
source_id: "6PGLUCONOLACT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 6PGLUCONOLACT-RXN

`reaction.ecocyc.6PGLUCONOLACT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:6PGLUCONOLACT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second step in the pentose phosphate pathway. EcoCyc reaction equation: D-6-P-GLUCONO-DELTA-LACTONE + WATER -> PROTON + CPD-2961; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second step in the pentose phosphate pathway.

## Biological Role

Catalyzed by pgl (protein.P52697). Substrates: H2O (molecule.C00001), D-Glucono-1,5-lactone 6-phosphate (molecule.C01236). Products: H+ (molecule.C00080), 6-Phospho-D-gluconate (molecule.C00345).

## Enriched Pathways

- `ecocyc.GLYCOLYSIS-E-D` superpathway of glycolysis and the Entner-Doudoroff pathway (EcoCyc)
- `ecocyc.OXIDATIVEPENT-PWY` pentose phosphate pathway (oxidative branch) I (EcoCyc)

## Annotation

This is the second step in the pentose phosphate pathway.

## Pathways

- `ecocyc.GLYCOLYSIS-E-D` superpathway of glycolysis and the Entner-Doudoroff pathway (EcoCyc)
- `ecocyc.OXIDATIVEPENT-PWY` pentose phosphate pathway (oxidative branch) I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P52697|protein.P52697]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00345|molecule.C00345]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01236|molecule.C01236]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:6PGLUCONOLACT-RXN`

## Notes

D-6-P-GLUCONO-DELTA-LACTONE + WATER -> PROTON + CPD-2961; direction=PHYSIOL-LEFT-TO-RIGHT
