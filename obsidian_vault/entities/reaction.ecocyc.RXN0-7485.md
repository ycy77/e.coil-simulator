---
entity_id: "reaction.ecocyc.RXN0-7485"
entity_type: "reaction"
name: "RXN0-7485"
source_database: "EcoCyc"
source_id: "RXN0-7485"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7485

`reaction.ecocyc.RXN0-7485`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7485`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MESO-TARTRATE -> OXALACETIC_ACID + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: MESO-TARTRATE -> OXALACETIC_ACID + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by L(+)-tartrate dehydratase (complex.ecocyc.LTARTDEHYDRA-CPLX). Substrates: meso-Tartaric acid (molecule.C00552). Products: H2O (molecule.C00001), Oxaloacetate (molecule.C00036).

## Annotation

MESO-TARTRATE -> OXALACETIC_ACID + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.LTARTDEHYDRA-CPLX|complex.ecocyc.LTARTDEHYDRA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00552|molecule.C00552]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7485`

## Notes

MESO-TARTRATE -> OXALACETIC_ACID + WATER; direction=LEFT-TO-RIGHT
