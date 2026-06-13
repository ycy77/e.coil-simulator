---
entity_id: "reaction.ecocyc.RXN0-1140"
entity_type: "reaction"
name: "RXN0-1140"
source_database: "EcoCyc"
source_id: "RXN0-1140"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1140

`reaction.ecocyc.RXN0-1140`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1140`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

LIPOIC-ACID + E2O-MONOMER + ATP -> SUCB-LIPOATE + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: LIPOIC-ACID + E2O-MONOMER + ATP -> SUCB-LIPOATE + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lplA (protein.P32099). Substrates: ATP (molecule.C00002), (R)-Lipoate (molecule.C16241). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Annotation

LIPOIC-ACID + E2O-MONOMER + ATP -> SUCB-LIPOATE + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P32099|protein.P32099]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C16241|molecule.C16241]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1140`

## Notes

LIPOIC-ACID + E2O-MONOMER + ATP -> SUCB-LIPOATE + AMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
