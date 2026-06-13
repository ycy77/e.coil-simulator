---
entity_id: "reaction.ecocyc.GLUTAMIN-RXN"
entity_type: "reaction"
name: "GLUTAMIN-RXN"
source_database: "EcoCyc"
source_id: "GLUTAMIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUTAMIN-RXN

`reaction.ecocyc.GLUTAMIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUTAMIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the hydrolytic deamidation of L-glutamine. EcoCyc reaction equation: GLN + WATER -> GLT + AMMONIA + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the hydrolytic deamidation of L-glutamine.

## Biological Role

Catalyzed by asparagine synthetase B (complex.ecocyc.ASNSYNB-CPLX), glutaminase 1 (complex.ecocyc.CPLX0-7694), glutaminase 2 (complex.ecocyc.CPLX0-7695). Substrates: H2O (molecule.C00001), L-Glutamine (molecule.C00064). Products: Ammonia (molecule.C00014), L-Glutamate (molecule.C00025), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.AMMASSIM-PWY` ammonia assimilation cycle III (EcoCyc)
- `ecocyc.GLUTAMINDEG-PWY` L-glutamine degradation I (EcoCyc)
- `ecocyc.GLUTSYN-PWY` L-glutamate biosynthesis I (EcoCyc)

## Annotation

This reaction is the hydrolytic deamidation of L-glutamine.

## Pathways

- `ecocyc.AMMASSIM-PWY` ammonia assimilation cycle III (EcoCyc)
- `ecocyc.GLUTAMINDEG-PWY` L-glutamine degradation I (EcoCyc)
- `ecocyc.GLUTSYN-PWY` L-glutamate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.ASNSYNB-CPLX|complex.ecocyc.ASNSYNB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7694|complex.ecocyc.CPLX0-7694]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7695|complex.ecocyc.CPLX0-7695]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9195|molecule.ecocyc.CPD-9195]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUTAMIN-RXN`

## Notes

GLN + WATER -> GLT + AMMONIA + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
