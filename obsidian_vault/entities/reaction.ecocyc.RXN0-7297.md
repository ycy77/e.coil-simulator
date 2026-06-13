---
entity_id: "reaction.ecocyc.RXN0-7297"
entity_type: "reaction"
name: "RXN0-7297"
source_database: "EcoCyc"
source_id: "RXN0-7297"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7297

`reaction.ecocyc.RXN0-7297`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7297`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PHOSPHO-NARL + WATER -> NARL-MONOMER + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PHOSPHO-NARL + WATER -> NARL-MONOMER + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by sensor histidine kinase NarX (complex.ecocyc.NARX-CPLX). Substrates: H2O (molecule.C00001). Products: H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

PHOSPHO-NARL + WATER -> NARL-MONOMER + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.NARX-CPLX|complex.ecocyc.NARX-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7297`

## Notes

PHOSPHO-NARL + WATER -> NARL-MONOMER + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
