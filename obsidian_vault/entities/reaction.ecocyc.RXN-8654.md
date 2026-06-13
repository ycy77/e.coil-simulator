---
entity_id: "reaction.ecocyc.RXN-8654"
entity_type: "reaction"
name: "RXN-8654"
source_database: "EcoCyc"
source_id: "RXN-8654"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-8654

`reaction.ecocyc.RXN-8654`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8654`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + LIPOIC-ACID + ATP -> LIPOYL-AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + LIPOIC-ACID + ATP -> LIPOYL-AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: ATP (molecule.C00002), H+ (molecule.C00080), (R)-Lipoate (molecule.C16241). Products: Diphosphate (molecule.C00013), Lipoyl-AMP (molecule.C16238).

## Enriched Pathways

- `ecocyc.PWY0-522` lipoate salvage I (EcoCyc)

## Annotation

PROTON + LIPOIC-ACID + ATP -> LIPOYL-AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-522` lipoate salvage I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C16238|molecule.C16238]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C16241|molecule.C16241]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8654`

## Notes

PROTON + LIPOIC-ACID + ATP -> LIPOYL-AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
