---
entity_id: "reaction.ecocyc.RXN-23894"
entity_type: "reaction"
name: "RXN-23894"
source_database: "EcoCyc"
source_id: "RXN-23894"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23894

`reaction.ecocyc.RXN-23894`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23894`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GLN + ATP + PROTON -> CPD-26474 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: GLN + ATP + PROTON -> CPD-26474 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), L-Glutamine (molecule.C00064), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013), (L-glutaminyl)adenylate (molecule.ecocyc.CPD-26474).

## Annotation

GLN + ATP + PROTON -> CPD-26474 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26474|molecule.ecocyc.CPD-26474]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23894`

## Notes

GLN + ATP + PROTON -> CPD-26474 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
