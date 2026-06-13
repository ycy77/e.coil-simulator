---
entity_id: "reaction.ecocyc.RXN-11496"
entity_type: "reaction"
name: "RXN-11496"
source_database: "EcoCyc"
source_id: "RXN-11496"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "pyruvic (cytochrome b1) dehydrogenase"
---

# RXN-11496

`reaction.ecocyc.RXN-11496`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11496`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PYRUVATE + WATER + Ubiquinones -> CARBON-DIOXIDE + Ubiquinols + ACET; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PYRUVATE + WATER + Ubiquinones -> CARBON-DIOXIDE + Ubiquinols + ACET; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by pyruvate oxidase (complex.ecocyc.PYRUVOXID-CPLX). Substrates: H2O (molecule.C00001), Pyruvate (molecule.C00022), a ubiquinone (molecule.ecocyc.Ubiquinones). Products: CO2 (molecule.C00011), Acetate (molecule.C00033), Ubiquinol (molecule.C00390).

## Enriched Pathways

- `ecocyc.PWY-7544` pyruvate to cytochrome bo oxidase electron transfer (EcoCyc)
- `ecocyc.PWY-7545` pyruvate to cytochrome bd oxidase electron transfer (EcoCyc)

## Annotation

PYRUVATE + WATER + Ubiquinones -> CARBON-DIOXIDE + Ubiquinols + ACET; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7544` pyruvate to cytochrome bo oxidase electron transfer (EcoCyc)
- `ecocyc.PWY-7545` pyruvate to cytochrome bd oxidase electron transfer (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (17)

- `activates` <-- [[molecule.C00249|molecule.C00249]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00638|molecule.C00638]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00741|molecule.C00741]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00865|molecule.C00865]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.PYRUVOXID-CPLX|complex.ecocyc.PYRUVOXID-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C03167|molecule.C03167]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.METHYL-ACETYLPHOSPHONATE|molecule.ecocyc.METHYL-ACETYLPHOSPHONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.METHYLMETHANETHIOSULFONATE|molecule.ecocyc.METHYLMETHANETHIOSULFONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHENYLGLYOXAL|molecule.ecocyc.PHENYLGLYOXAL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-11496`

## Notes

PYRUVATE + WATER + Ubiquinones -> CARBON-DIOXIDE + Ubiquinols + ACET; direction=LEFT-TO-RIGHT
