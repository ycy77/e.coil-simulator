---
entity_id: "reaction.ecocyc.RXN-21400"
entity_type: "reaction"
name: "RXN-21400"
source_database: "EcoCyc"
source_id: "RXN-21400"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21400

`reaction.ecocyc.RXN-21400`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21400`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-DEHYDRO-ASCORBATE + WATER -> CPD-334; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-DEHYDRO-ASCORBATE + WATER -> CPD-334; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), Dehydroascorbate (molecule.C05422). Products: 2,3-didehydro-L-gulonate (molecule.ecocyc.CPD-334).

## Enriched Pathways

- `ecocyc.PWY-6961` L-ascorbate degradation II (bacterial, aerobic) (EcoCyc)

## Annotation

L-DEHYDRO-ASCORBATE + WATER -> CPD-334; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6961` L-ascorbate degradation II (bacterial, aerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.CPD-334|molecule.ecocyc.CPD-334]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05422|molecule.C05422]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21400`

## Notes

L-DEHYDRO-ASCORBATE + WATER -> CPD-334; direction=PHYSIOL-LEFT-TO-RIGHT
