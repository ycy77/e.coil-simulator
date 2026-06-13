---
entity_id: "reaction.ecocyc.LCYSDESULF-RXN"
entity_type: "reaction"
name: "LCYSDESULF-RXN"
source_database: "EcoCyc"
source_id: "LCYSDESULF-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# LCYSDESULF-RXN

`reaction.ecocyc.LCYSDESULF-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LCYSDESULF-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of L-cysteine catabolism. EcoCyc reaction equation: CYS + WATER -> PYRUVATE + AMMONIUM + HS; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of L-cysteine catabolism.

## Biological Role

Catalyzed by cysteine synthase A (complex.ecocyc.ACSERLYA-CPLX), cysteine synthase B (complex.ecocyc.ACSERLYB-CPLX), negative regulator of MalT activity/cystathionine β-lyase (complex.ecocyc.CPLX0-8092), cystathionine β-lyase / L-cysteine desulfhydrase / alanine racemase (complex.ecocyc.CYSTATHIONINE-BETA-LYASE-CPLX), tryptophanase / L-cysteine desulfhydrase (complex.ecocyc.TRYPTOPHAN-CPLX), yhaM (protein.P42626). Substrates: H2O (molecule.C00001), L-Cysteine (molecule.C00097). Products: Pyruvate (molecule.C00022), Hydrogen sulfide (molecule.C00283), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

This reaction is part of L-cysteine catabolism.

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

- `catalyzes` <-- [[complex.ecocyc.ACSERLYA-CPLX|complex.ecocyc.ACSERLYA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.ACSERLYB-CPLX|complex.ecocyc.ACSERLYB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8092|complex.ecocyc.CPLX0-8092]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CYSTATHIONINE-BETA-LYASE-CPLX|complex.ecocyc.CYSTATHIONINE-BETA-LYASE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.TRYPTOPHAN-CPLX|complex.ecocyc.TRYPTOPHAN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P42626|protein.P42626]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00155|molecule.C00155]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00793|molecule.C00793]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01678|molecule.C01678]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9175|molecule.ecocyc.CPD-9175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:LCYSDESULF-RXN`

## Notes

CYS + WATER -> PYRUVATE + AMMONIUM + HS; direction=PHYSIOL-LEFT-TO-RIGHT
