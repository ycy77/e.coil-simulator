---
entity_id: "reaction.ecocyc.RXN-17190"
entity_type: "reaction"
name: "RXN-17190"
source_database: "EcoCyc"
source_id: "RXN-17190"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17190

`reaction.ecocyc.RXN-17190`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17190`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-ALPHA-ALANINE + ATP + PROTON -> CPD-18588 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-ALPHA-ALANINE + ATP + PROTON -> CPD-18588 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), L-Alanine (molecule.C00041), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013), (L-alanyl)adenylate (molecule.ecocyc.CPD-18588).

## Annotation

L-ALPHA-ALANINE + ATP + PROTON -> CPD-18588 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-18588|molecule.ecocyc.CPD-18588]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17190`

## Notes

L-ALPHA-ALANINE + ATP + PROTON -> CPD-18588 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
