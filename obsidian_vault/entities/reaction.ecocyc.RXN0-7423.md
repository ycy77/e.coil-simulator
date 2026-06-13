---
entity_id: "reaction.ecocyc.RXN0-7423"
entity_type: "reaction"
name: "RXN0-7423"
source_database: "EcoCyc"
source_id: "RXN0-7423"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7423

`reaction.ecocyc.RXN0-7423`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7423`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-195 + ATP + PROTON -> CPD-26594 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-195 + ATP + PROTON -> CPD-26594 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), Octanoic acid (molecule.C06423). Products: Diphosphate (molecule.C00013), (octanoyl)adenylate (molecule.ecocyc.CPD-26594).

## Enriched Pathways

- `ecocyc.PWY0-1275` lipoate biosynthesis and incorporation II (EcoCyc)

## Annotation

CPD-195 + ATP + PROTON -> CPD-26594 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1275` lipoate biosynthesis and incorporation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26594|molecule.ecocyc.CPD-26594]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06423|molecule.C06423]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7423`

## Notes

CPD-195 + ATP + PROTON -> CPD-26594 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
