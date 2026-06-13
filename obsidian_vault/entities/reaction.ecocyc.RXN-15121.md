---
entity_id: "reaction.ecocyc.RXN-15121"
entity_type: "reaction"
name: "RXN-15121"
source_database: "EcoCyc"
source_id: "RXN-15121"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15121

`reaction.ecocyc.RXN-15121`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15121`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15056 -> CPD-16013; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-15056 -> CPD-16013; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: (Z)-2-aminobutenoate (molecule.ecocyc.CPD-15056). Products: 2-iminobutanoate (molecule.ecocyc.CPD-16013).

## Enriched Pathways

- `ecocyc.ILEUSYN-PWY` L-isoleucine biosynthesis I (from threonine) (EcoCyc)
- `ecocyc.PWY-5437` L-threonine degradation I (EcoCyc)

## Annotation

CPD-15056 -> CPD-16013; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.ILEUSYN-PWY` L-isoleucine biosynthesis I (from threonine) (EcoCyc)
- `ecocyc.PWY-5437` L-threonine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.CPD-16013|molecule.ecocyc.CPD-16013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15056|molecule.ecocyc.CPD-15056]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15121`

## Notes

CPD-15056 -> CPD-16013; direction=LEFT-TO-RIGHT
