---
entity_id: "reaction.ecocyc.D--TARTRATE-DEHYDRATASE-RXN"
entity_type: "reaction"
name: "D--TARTRATE-DEHYDRATASE-RXN"
source_database: "EcoCyc"
source_id: "D--TARTRATE-DEHYDRATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D--TARTRATE-DEHYDRATASE-RXN

`reaction.ecocyc.D--TARTRATE-DEHYDRATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:D--TARTRATE-DEHYDRATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-TARTRATE -> WATER + OXALACETIC_ACID; direction=REVERSIBLE EcoCyc reaction equation: D-TARTRATE -> WATER + OXALACETIC_ACID; direction=REVERSIBLE.

## Biological Role

Catalyzed by fumarase B (complex.ecocyc.FUMARASE-B). Substrates: D-tartrate (molecule.ecocyc.D-TARTRATE). Products: H2O (molecule.C00001), Oxaloacetate (molecule.C00036).

## Annotation

D-TARTRATE -> WATER + OXALACETIC_ACID; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.FUMARASE-B|complex.ecocyc.FUMARASE-B]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.D-TARTRATE|molecule.ecocyc.D-TARTRATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:D--TARTRATE-DEHYDRATASE-RXN`

## Notes

D-TARTRATE -> WATER + OXALACETIC_ACID; direction=REVERSIBLE
