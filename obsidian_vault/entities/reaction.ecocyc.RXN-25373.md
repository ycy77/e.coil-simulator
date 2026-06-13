---
entity_id: "reaction.ecocyc.RXN-25373"
entity_type: "reaction"
name: "RXN-25373"
source_database: "EcoCyc"
source_id: "RXN-25373"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25373

`reaction.ecocyc.RXN-25373`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25373`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + CPD-27985 -> PPI + CPD-27987; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CPD-27985 -> PPI + CPD-27987; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), 7-amido-7-carbaguanine (molecule.ecocyc.CPD-27985). Products: Diphosphate (molecule.C00013), 7-iminomethyladenylyl-7-carbaguanine (molecule.ecocyc.CPD-27987).

## Annotation

ATP + CPD-27985 -> PPI + CPD-27987; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-27987|molecule.ecocyc.CPD-27987]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-27985|molecule.ecocyc.CPD-27985]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25373`

## Notes

ATP + CPD-27985 -> PPI + CPD-27987; direction=PHYSIOL-LEFT-TO-RIGHT
