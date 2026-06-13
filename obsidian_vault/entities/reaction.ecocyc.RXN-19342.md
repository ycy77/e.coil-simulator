---
entity_id: "reaction.ecocyc.RXN-19342"
entity_type: "reaction"
name: "RXN-19342"
source_database: "EcoCyc"
source_id: "RXN-19342"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19342

`reaction.ecocyc.RXN-19342`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19342`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-20903 + Corrinoid-Adenosyltransferases -> CPD-20906; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-20903 + Corrinoid-Adenosyltransferases -> CPD-20906; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: cob(II)inamide (molecule.ecocyc.CPD-20903). Products: [corrinoid adenosyltranferase]-cob(II)inamide (molecule.ecocyc.CPD-20906).

## Enriched Pathways

- `ecocyc.PWY-7971` adenosylcobinamide-GDP salvage from cobinamide I (EcoCyc)

## Annotation

CPD-20903 + Corrinoid-Adenosyltransferases -> CPD-20906; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7971` adenosylcobinamide-GDP salvage from cobinamide I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.CPD-20906|molecule.ecocyc.CPD-20906]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20903|molecule.ecocyc.CPD-20903]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19342`

## Notes

CPD-20903 + Corrinoid-Adenosyltransferases -> CPD-20906; direction=PHYSIOL-LEFT-TO-RIGHT
