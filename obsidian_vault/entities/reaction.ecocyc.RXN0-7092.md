---
entity_id: "reaction.ecocyc.RXN0-7092"
entity_type: "reaction"
name: "RXN0-7092"
source_database: "EcoCyc"
source_id: "RXN0-7092"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7092

`reaction.ecocyc.RXN0-7092`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7092`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NIACINAMIDE + RIBOSE-1P + PROTON -> NICOTINAMIDE_RIBOSE + Pi; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: NIACINAMIDE + RIBOSE-1P + PROTON -> NICOTINAMIDE_RIBOSE + Pi; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by xanthosine phosphorylase (complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX). Substrates: H+ (molecule.C00080), Nicotinamide (molecule.C00153), alpha-D-Ribose 1-phosphate (molecule.C00620). Products: Nicotinamide-beta-riboside (molecule.C03150), phosphate (molecule.ecocyc.Pi).

## Annotation

NIACINAMIDE + RIBOSE-1P + PROTON -> NICOTINAMIDE_RIBOSE + Pi; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX|complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C03150|molecule.C03150]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00153|molecule.C00153]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00620|molecule.C00620]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7092`

## Notes

NIACINAMIDE + RIBOSE-1P + PROTON -> NICOTINAMIDE_RIBOSE + Pi; direction=PHYSIOL-RIGHT-TO-LEFT
