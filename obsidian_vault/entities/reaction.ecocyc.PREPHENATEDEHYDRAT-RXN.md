---
entity_id: "reaction.ecocyc.PREPHENATEDEHYDRAT-RXN"
entity_type: "reaction"
name: "PREPHENATEDEHYDRAT-RXN"
source_database: "EcoCyc"
source_id: "PREPHENATEDEHYDRAT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PREPHENATEDEHYDRAT-RXN

`reaction.ecocyc.PREPHENATEDEHYDRAT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PREPHENATEDEHYDRAT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction after chorismate in the biosynthesis of phenylalanine. It differs from the corresponding step in the biosynthesis of tyrosine in that it is a dehydratase, not a dehydrogenase. EcoCyc reaction equation: PROTON + PREPHENATE -> PHENYL-PYRUVATE + WATER + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT. This is the second reaction after chorismate in the biosynthesis of phenylalanine. It differs from the corresponding step in the biosynthesis of tyrosine in that it is a dehydratase, not a dehydrogenase.

## Biological Role

Catalyzed by fused chorismate mutase/prephenate dehydratase (complex.ecocyc.CHORISMUTPREPHENDEHYDRAT-CPLX). Substrates: H+ (molecule.C00080), Prephenate (molecule.C00254). Products: H2O (molecule.C00001), CO2 (molecule.C00011), Phenylpyruvate (molecule.C00166).

## Enriched Pathways

- `ecocyc.PHESYN` L-phenylalanine biosynthesis I (EcoCyc)

## Annotation

This is the second reaction after chorismate in the biosynthesis of phenylalanine. It differs from the corresponding step in the biosynthesis of tyrosine in that it is a dehydratase, not a dehydrogenase.

## Pathways

- `ecocyc.PHESYN` L-phenylalanine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

- `catalyzes` <-- [[complex.ecocyc.CHORISMUTPREPHENDEHYDRAT-CPLX|complex.ecocyc.CHORISMUTPREPHENDEHYDRAT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00166|molecule.C00166]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00254|molecule.C00254]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00079|molecule.C00079]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00251|molecule.C00251]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00417|molecule.C00417]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C02341|molecule.C02341]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1524|molecule.ecocyc.CPD0-1524]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1525|molecule.ecocyc.CPD0-1525]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.TETRANITROMETHANE|molecule.ecocyc.TETRANITROMETHANE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PREPHENATEDEHYDRAT-RXN`

## Notes

PROTON + PREPHENATE -> PHENYL-PYRUVATE + WATER + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
