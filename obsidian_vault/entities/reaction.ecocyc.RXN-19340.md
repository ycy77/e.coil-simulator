---
entity_id: "reaction.ecocyc.RXN-19340"
entity_type: "reaction"
name: "RXN-19340"
source_database: "EcoCyc"
source_id: "RXN-19340"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19340

`reaction.ecocyc.RXN-19340`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19340`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-1829 + Corrinoid-Adenosyltransferases -> CPD-20904; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-1829 + Corrinoid-Adenosyltransferases -> CPD-20904; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Cob(II)alamin (molecule.C00541). Products: cob(II)alamin-[corrinoid adenosyltranferase] (molecule.ecocyc.CPD-20904).

## Enriched Pathways

- `ecocyc.PWY-6268` adenosylcobalamin salvage from cobalamin (EcoCyc)

## Annotation

CPD-1829 + Corrinoid-Adenosyltransferases -> CPD-20904; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6268` adenosylcobalamin salvage from cobalamin (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.CPD-20904|molecule.ecocyc.CPD-20904]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00541|molecule.C00541]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19340`

## Notes

CPD-1829 + Corrinoid-Adenosyltransferases -> CPD-20904; direction=PHYSIOL-LEFT-TO-RIGHT
