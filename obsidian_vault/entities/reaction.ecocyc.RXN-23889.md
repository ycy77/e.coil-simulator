---
entity_id: "reaction.ecocyc.RXN-23889"
entity_type: "reaction"
name: "RXN-23889"
source_database: "EcoCyc"
source_id: "RXN-23889"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23889

`reaction.ecocyc.RXN-23889`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23889`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ILE + ATP + PROTON -> CPD-26473 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ILE + ATP + PROTON -> CPD-26473 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), L-Isoleucine (molecule.C00407). Products: Diphosphate (molecule.C00013), (L-isoleucyl)adenylate (molecule.ecocyc.CPD-26473).

## Annotation

ILE + ATP + PROTON -> CPD-26473 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26473|molecule.ecocyc.CPD-26473]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00407|molecule.C00407]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23889`

## Notes

ILE + ATP + PROTON -> CPD-26473 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
