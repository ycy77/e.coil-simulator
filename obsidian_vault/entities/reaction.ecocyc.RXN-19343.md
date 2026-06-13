---
entity_id: "reaction.ecocyc.RXN-19343"
entity_type: "reaction"
name: "RXN-19343"
source_database: "EcoCyc"
source_id: "RXN-19343"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19343

`reaction.ecocyc.RXN-19343`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19343`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + CPD-20907 + PROTON -> ADENOSYLCOBINAMIDE + P3I + Corrinoid-Adenosyltransferases; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CPD-20907 + PROTON -> ADENOSYLCOBINAMIDE + P3I + Corrinoid-Adenosyltransferases; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), [corrinoid adenosyltranferase]-cob(I)inamide (molecule.ecocyc.CPD-20907). Products: Triphosphate (molecule.C00536), Adenosyl cobinamide (molecule.C06508).

## Enriched Pathways

- `ecocyc.PWY-7971` adenosylcobinamide-GDP salvage from cobinamide I (EcoCyc)

## Annotation

ATP + CPD-20907 + PROTON -> ADENOSYLCOBINAMIDE + P3I + Corrinoid-Adenosyltransferases; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7971` adenosylcobinamide-GDP salvage from cobinamide I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00536|molecule.C00536]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06508|molecule.C06508]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20907|molecule.ecocyc.CPD-20907]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19343`

## Notes

ATP + CPD-20907 + PROTON -> ADENOSYLCOBINAMIDE + P3I + Corrinoid-Adenosyltransferases; direction=PHYSIOL-LEFT-TO-RIGHT
