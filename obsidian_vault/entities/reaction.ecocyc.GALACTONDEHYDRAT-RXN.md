---
entity_id: "reaction.ecocyc.GALACTONDEHYDRAT-RXN"
entity_type: "reaction"
name: "GALACTONDEHYDRAT-RXN"
source_database: "EcoCyc"
source_id: "GALACTONDEHYDRAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GALACTONDEHYDRAT-RXN

`reaction.ecocyc.GALACTONDEHYDRAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GALACTONDEHYDRAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The first step of galactonate catabolism. EcoCyc reaction equation: D-GALACTONATE -> WATER + 2-DEHYDRO-3-DEOXY-D-GALACTONATE; direction=LEFT-TO-RIGHT. The first step of galactonate catabolism.

## Biological Role

Catalyzed by dgoD (protein.Q6BF17). Substrates: D-Galactonate (molecule.C00880). Products: H2O (molecule.C00001), 2-Dehydro-3-deoxy-D-galactonate (molecule.C01216).

## Enriched Pathways

- `ecocyc.GALACTCAT-PWY` D-galactonate degradation (EcoCyc)

## Annotation

The first step of galactonate catabolism.

## Pathways

- `ecocyc.GALACTCAT-PWY` D-galactonate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.Q6BF17|protein.Q6BF17]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01216|molecule.C01216]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00880|molecule.C00880]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GALACTONDEHYDRAT-RXN`

## Notes

D-GALACTONATE -> WATER + 2-DEHYDRO-3-DEOXY-D-GALACTONATE; direction=LEFT-TO-RIGHT
