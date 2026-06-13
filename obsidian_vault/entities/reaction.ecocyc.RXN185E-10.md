---
entity_id: "reaction.ecocyc.RXN185E-10"
entity_type: "reaction"
name: "RXN185E-10"
source_database: "EcoCyc"
source_id: "RXN185E-10"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN185E-10

`reaction.ecocyc.RXN185E-10`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN185E-10`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-Aggregates + ATP + WATER -> Unfolded-Proteins + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Protein-Aggregates + ATP + WATER -> Unfolded-Proteins + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by protein disaggregase (complex.ecocyc.CPLX0-8180). Substrates: H2O (molecule.C00001), ATP (molecule.C00002). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

Protein-Aggregates + ATP + WATER -> Unfolded-Proteins + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8180|complex.ecocyc.CPLX0-8180]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN185E-10`

## Notes

Protein-Aggregates + ATP + WATER -> Unfolded-Proteins + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
