---
entity_id: "reaction.ecocyc.RXN-19780"
entity_type: "reaction"
name: "RXN-19780"
source_database: "EcoCyc"
source_id: "RXN-19780"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19780

`reaction.ecocyc.RXN-19780`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19780`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-21398 + WATER -> Protein-L-Aspartates + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-21398 + WATER -> Protein-L-Aspartates + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H2O (molecule.C00001), a [protein]-phospho-L-aspartate (molecule.ecocyc.CPD-21398). Products: H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi), a [protein]-L-aspartate (molecule.ecocyc.Protein-L-Aspartates).

## Annotation

CPD-21398 + WATER -> Protein-L-Aspartates + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-L-Aspartates|molecule.ecocyc.Protein-L-Aspartates]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21398|molecule.ecocyc.CPD-21398]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19780`

## Notes

CPD-21398 + WATER -> Protein-L-Aspartates + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
