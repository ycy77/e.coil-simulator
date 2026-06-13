---
entity_id: "reaction.ecocyc.TRYPTOPHAN-RXN"
entity_type: "reaction"
name: "TRYPTOPHAN-RXN"
source_database: "EcoCyc"
source_id: "TRYPTOPHAN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRYPTOPHAN-RXN

`reaction.ecocyc.TRYPTOPHAN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRYPTOPHAN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction takes part in the degradation of tryptophan. EcoCyc reaction equation: TRP + WATER -> AMMONIUM + INDOLE + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction takes part in the degradation of tryptophan.

## Biological Role

Catalyzed by tryptophanase / L-cysteine desulfhydrase (complex.ecocyc.TRYPTOPHAN-CPLX). Substrates: H2O (molecule.C00001), L-Tryptophan (molecule.C00078). Products: Pyruvate (molecule.C00022), Indole (molecule.C00463), ammonium (molecule.ecocyc.AMMONIUM).

## Annotation

This reaction takes part in the degradation of tryptophan.

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.TRYPTOPHAN-CPLX|complex.ecocyc.TRYPTOPHAN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00463|molecule.C00463]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00078|molecule.C00078]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRYPTOPHAN-RXN`

## Notes

TRP + WATER -> AMMONIUM + INDOLE + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT
