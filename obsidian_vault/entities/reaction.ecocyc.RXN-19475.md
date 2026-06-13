---
entity_id: "reaction.ecocyc.RXN-19475"
entity_type: "reaction"
name: "RXN-19475"
source_database: "EcoCyc"
source_id: "RXN-19475"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19475

`reaction.ecocyc.RXN-19475`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19475`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TRP + ATP + PROTON -> CPD-21003 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: TRP + ATP + PROTON -> CPD-21003 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), L-Tryptophan (molecule.C00078), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013), (L-tryptophanyl)adenylate (molecule.ecocyc.CPD-21003).

## Annotation

TRP + ATP + PROTON -> CPD-21003 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21003|molecule.ecocyc.CPD-21003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00078|molecule.C00078]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19475`

## Notes

TRP + ATP + PROTON -> CPD-21003 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
