---
entity_id: "reaction.ecocyc.RXN-23949"
entity_type: "reaction"
name: "RXN-23949"
source_database: "EcoCyc"
source_id: "RXN-23949"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-23949

`reaction.ecocyc.RXN-23949`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-23949`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-2-AMINOPENTANOIC-ACID + ATP + PROTON -> CPD-26483 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-2-AMINOPENTANOIC-ACID + ATP + PROTON -> CPD-26483 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), L-norvaline (molecule.ecocyc.L-2-AMINOPENTANOIC-ACID). Products: Diphosphate (molecule.C00013), (L-norvalyl)adenylate (molecule.ecocyc.CPD-26483).

## Annotation

L-2-AMINOPENTANOIC-ACID + ATP + PROTON -> CPD-26483 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26483|molecule.ecocyc.CPD-26483]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.L-2-AMINOPENTANOIC-ACID|molecule.ecocyc.L-2-AMINOPENTANOIC-ACID]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-23949`

## Notes

L-2-AMINOPENTANOIC-ACID + ATP + PROTON -> CPD-26483 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
