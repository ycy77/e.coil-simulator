---
entity_id: "reaction.ecocyc.RXN-23892"
entity_type: "reaction"
name: "RXN-23892"
source_database: "EcoCyc"
source_id: "RXN-23892"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23892

`reaction.ecocyc.RXN-23892`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23892`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PHE + ATP + PROTON -> CPD-26471 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PHE + ATP + PROTON -> CPD-26471 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), L-Phenylalanine (molecule.C00079), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013), (L-phenylalanyl)adenylate (molecule.ecocyc.CPD-26471).

## Annotation

PHE + ATP + PROTON -> CPD-26471 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26471|molecule.ecocyc.CPD-26471]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00079|molecule.C00079]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23892`

## Notes

PHE + ATP + PROTON -> CPD-26471 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
