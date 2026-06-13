---
entity_id: "reaction.ecocyc.RXN0-6973"
entity_type: "reaction"
name: "RXN0-6973"
source_database: "EcoCyc"
source_id: "RXN0-6973"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6973

`reaction.ecocyc.RXN0-6973`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6973`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is needed because automated instantiation fails for the generic version RXN0-280. EcoCyc reaction equation: CPD-3744 + OXYGEN-MOLECULE + FMNH2 -> BUTANAL + SO3 + WATER + FMN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is needed because automated instantiation fails for the generic version RXN0-280.

## Biological Role

Substrates: Oxygen (molecule.C00007), Reduced FMN (molecule.C01847), 1-butanesulfonate (molecule.ecocyc.CPD-3744). Products: H2O (molecule.C00001), FMN (molecule.C00061), H+ (molecule.C00080), Sulfite (molecule.C00094), Butanal (molecule.C01412).

## Annotation

This reaction is needed because automated instantiation fails for the generic version RXN0-280.

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01412|molecule.C01412]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01847|molecule.C01847]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3744|molecule.ecocyc.CPD-3744]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6973`

## Notes

CPD-3744 + OXYGEN-MOLECULE + FMNH2 -> BUTANAL + SO3 + WATER + FMN + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
