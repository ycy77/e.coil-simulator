---
entity_id: "reaction.ecocyc.RXN-23888"
entity_type: "reaction"
name: "RXN-23888"
source_database: "EcoCyc"
source_id: "RXN-23888"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23888

`reaction.ecocyc.RXN-23888`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23888`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HIS + ATP + PROTON -> CPD-26469 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: HIS + ATP + PROTON -> CPD-26469 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), L-Histidine (molecule.C00135). Products: Diphosphate (molecule.C00013), (L-histidyl)adenylate (molecule.ecocyc.CPD-26469).

## Annotation

HIS + ATP + PROTON -> CPD-26469 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26469|molecule.ecocyc.CPD-26469]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00135|molecule.C00135]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23888`

## Notes

HIS + ATP + PROTON -> CPD-26469 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
