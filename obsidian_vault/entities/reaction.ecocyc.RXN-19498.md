---
entity_id: "reaction.ecocyc.RXN-19498"
entity_type: "reaction"
name: "RXN-19498"
source_database: "EcoCyc"
source_id: "RXN-19498"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19498

`reaction.ecocyc.RXN-19498`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19498`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ARG + ATP + PROTON -> CPD-21008 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ARG + ATP + PROTON -> CPD-21008 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), L-Arginine (molecule.C00062), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013), (L-arginyl)adenylate (molecule.ecocyc.CPD-21008).

## Annotation

ARG + ATP + PROTON -> CPD-21008 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21008|molecule.ecocyc.CPD-21008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00062|molecule.C00062]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19498`

## Notes

ARG + ATP + PROTON -> CPD-21008 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
