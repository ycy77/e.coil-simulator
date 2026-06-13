---
entity_id: "reaction.ecocyc.RXN-25371"
entity_type: "reaction"
name: "RXN-25371"
source_database: "EcoCyc"
source_id: "RXN-25371"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25371

`reaction.ecocyc.RXN-25371`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25371`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + CPD-13043 + PROTON -> PPI + CPD-27984; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CPD-13043 + PROTON -> PPI + CPD-27984; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), 7-Carboxy-7-carbaguanine (molecule.C20248). Products: Diphosphate (molecule.C00013), 7-carboxyadenylyl-7-carbaguanine (molecule.ecocyc.CPD-27984).

## Annotation

ATP + CPD-13043 + PROTON -> PPI + CPD-27984; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-27984|molecule.ecocyc.CPD-27984]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C20248|molecule.C20248]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25371`

## Notes

ATP + CPD-13043 + PROTON -> PPI + CPD-27984; direction=PHYSIOL-LEFT-TO-RIGHT
