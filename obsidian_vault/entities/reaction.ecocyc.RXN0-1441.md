---
entity_id: "reaction.ecocyc.RXN0-1441"
entity_type: "reaction"
name: "RXN0-1441"
source_database: "EcoCyc"
source_id: "RXN0-1441"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1441

`reaction.ecocyc.RXN0-1441`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1441`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ADENOSINE_DIPHOSPHATE_RIBOSE + WATER -> AMP + CPD-15317 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ADENOSINE_DIPHOSPHATE_RIBOSE + WATER -> AMP + CPD-15317 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), ADP-ribose (molecule.C00301). Products: AMP (molecule.C00020), H+ (molecule.C00080), D-ribofuranose 5-phosphate (molecule.ecocyc.CPD-15317).

## Annotation

ADENOSINE_DIPHOSPHATE_RIBOSE + WATER -> AMP + CPD-15317 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15317|molecule.ecocyc.CPD-15317]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00301|molecule.C00301]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1441`

## Notes

ADENOSINE_DIPHOSPHATE_RIBOSE + WATER -> AMP + CPD-15317 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
