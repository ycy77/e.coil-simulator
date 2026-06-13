---
entity_id: "reaction.ecocyc.RXN-19366"
entity_type: "reaction"
name: "RXN-19366"
source_database: "EcoCyc"
source_id: "RXN-19366"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19366

`reaction.ecocyc.RXN-19366`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19366`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

B12-Corrinoid-Adenosyltranferase -> ADENOSYLCOBALAMIN + Corrinoid-Adenosyltransferases; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: B12-Corrinoid-Adenosyltranferase -> ADENOSYLCOBALAMIN + Corrinoid-Adenosyltransferases; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: adenosylcob(III)alamin-[corrinoid adenosyltranferase] (molecule.ecocyc.B12-Corrinoid-Adenosyltranferase). Products: Cobamide coenzyme (molecule.C00194).

## Enriched Pathways

- `ecocyc.PWY-6268` adenosylcobalamin salvage from cobalamin (EcoCyc)

## Annotation

B12-Corrinoid-Adenosyltranferase -> ADENOSYLCOBALAMIN + Corrinoid-Adenosyltransferases; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6268` adenosylcobalamin salvage from cobalamin (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00194|molecule.C00194]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.B12-Corrinoid-Adenosyltranferase|molecule.ecocyc.B12-Corrinoid-Adenosyltranferase]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19366`

## Notes

B12-Corrinoid-Adenosyltranferase -> ADENOSYLCOBALAMIN + Corrinoid-Adenosyltransferases; direction=PHYSIOL-LEFT-TO-RIGHT
