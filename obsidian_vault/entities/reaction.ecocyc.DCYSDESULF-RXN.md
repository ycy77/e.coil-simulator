---
entity_id: "reaction.ecocyc.DCYSDESULF-RXN"
entity_type: "reaction"
name: "DCYSDESULF-RXN"
source_database: "EcoCyc"
source_id: "DCYSDESULF-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DCYSDESULF-RXN

`reaction.ecocyc.DCYSDESULF-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DCYSDESULF-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the α,β-elimination of D-cysteine, removing both sulfur and the amino group. EcoCyc reaction equation: D-CYSTEINE + WATER -> AMMONIUM + PYRUVATE + HS; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the α,β-elimination of D-cysteine, removing both sulfur and the amino group.

## Biological Role

Catalyzed by D-cysteine desulfhydrase, PLP-dependent / 3-chloro-D-alanine dehydrochlorinase (complex.ecocyc.DCYSDESULF-CPLX). Substrates: H2O (molecule.C00001), D-Cysteine (molecule.C00793). Products: Pyruvate (molecule.C00022), Hydrogen sulfide (molecule.C00283), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

This reaction is the α,β-elimination of D-cysteine, removing both sulfur and the amino group.

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.DCYSDESULF-CPLX|complex.ecocyc.DCYSDESULF-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00793|molecule.C00793]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00793|molecule.C00793]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DCYSDESULF-RXN`

## Notes

D-CYSTEINE + WATER -> AMMONIUM + PYRUVATE + HS; direction=PHYSIOL-LEFT-TO-RIGHT
