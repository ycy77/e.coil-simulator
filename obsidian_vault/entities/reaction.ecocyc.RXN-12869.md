---
entity_id: "reaction.ecocyc.RXN-12869"
entity_type: "reaction"
name: "RXN-12869"
source_database: "EcoCyc"
source_id: "RXN-12869"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12869

`reaction.ecocyc.RXN-12869`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12869`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-DEHYDRO-ASCORBATE + OXYGEN-MOLECULE -> CPD-13914; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-DEHYDRO-ASCORBATE + OXYGEN-MOLECULE -> CPD-13914; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Oxygen (molecule.C00007), Dehydroascorbate (molecule.C05422). Products: cyclic-2,3-O-oxalyl-L-threonate (molecule.ecocyc.CPD-13914).

## Annotation

L-DEHYDRO-ASCORBATE + OXYGEN-MOLECULE -> CPD-13914; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.CPD-13914|molecule.ecocyc.CPD-13914]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05422|molecule.C05422]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12869`

## Notes

L-DEHYDRO-ASCORBATE + OXYGEN-MOLECULE -> CPD-13914; direction=PHYSIOL-LEFT-TO-RIGHT
