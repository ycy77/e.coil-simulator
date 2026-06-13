---
entity_id: "reaction.ecocyc.RXN0-6511"
entity_type: "reaction"
name: "RXN0-6511"
source_database: "EcoCyc"
source_id: "RXN0-6511"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6511

`reaction.ecocyc.RXN0-6511`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6511`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2363 + NADP + WATER -> CPD0-2364 + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2363 + NADP + WATER -> CPD0-2364 + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006), 2-Oxepin-2(3H)-ylideneacetyl-CoA (molecule.C19975). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 3-Oxo-5,6-dehydrosuberyl-CoA (molecule.C19945).

## Annotation

CPD0-2363 + NADP + WATER -> CPD0-2364 + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C19945|molecule.C19945]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C19975|molecule.C19975]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6511`

## Notes

CPD0-2363 + NADP + WATER -> CPD0-2364 + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
