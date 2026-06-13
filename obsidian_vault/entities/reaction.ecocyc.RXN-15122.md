---
entity_id: "reaction.ecocyc.RXN-15122"
entity_type: "reaction"
name: "RXN-15122"
source_database: "EcoCyc"
source_id: "RXN-15122"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15122

`reaction.ecocyc.RXN-15122`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15122`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

THR -> CPD-15056 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: THR -> CPD-15056 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: L-Threonine (molecule.C00188). Products: H2O (molecule.C00001), (Z)-2-aminobutenoate (molecule.ecocyc.CPD-15056).

## Enriched Pathways

- `ecocyc.ILEUSYN-PWY` L-isoleucine biosynthesis I (from threonine) (EcoCyc)
- `ecocyc.PWY-5437` L-threonine degradation I (EcoCyc)

## Annotation

THR -> CPD-15056 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.ILEUSYN-PWY` L-isoleucine biosynthesis I (from threonine) (EcoCyc)
- `ecocyc.PWY-5437` L-threonine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15056|molecule.ecocyc.CPD-15056]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15122`

## Notes

THR -> CPD-15056 + WATER; direction=PHYSIOL-LEFT-TO-RIGHT
