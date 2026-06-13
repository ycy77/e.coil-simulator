---
entity_id: "reaction.ecocyc.GLY3KIN-RXN"
entity_type: "reaction"
name: "GLY3KIN-RXN"
source_database: "EcoCyc"
source_id: "GLY3KIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLY3KIN-RXN

`reaction.ecocyc.GLY3KIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLY3KIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a reaction in glycolate metabolism. EcoCyc reaction equation: GLYCERATE + ATP -> PROTON + G3P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This is a reaction in glycolate metabolism.

## Biological Role

Substrates: ATP (molecule.C00002), D-Glycerate (molecule.C00258). Products: ADP (molecule.C00008), H+ (molecule.C00080), 3-Phospho-D-glycerate (molecule.C00197).

## Annotation

This is a reaction in glycolate metabolism.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00197|molecule.C00197]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00258|molecule.C00258]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLY3KIN-RXN`

## Notes

GLYCERATE + ATP -> PROTON + G3P + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
