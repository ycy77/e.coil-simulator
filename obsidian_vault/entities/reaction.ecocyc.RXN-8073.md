---
entity_id: "reaction.ecocyc.RXN-8073"
entity_type: "reaction"
name: "heme d biosynthesis"
source_database: "EcoCyc"
source_id: "RXN-8073"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# heme d biosynthesis

`reaction.ecocyc.RXN-8073`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-8073`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Heme-b + HYDROGEN-PEROXIDE -> HEME_D; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Heme-b + HYDROGEN-PEROXIDE -> HEME_D; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by catalase HPII (complex.ecocyc.HYDROPEROXIDII-CPLX). Substrates: Hydrogen peroxide (molecule.C00027), Heme (molecule.C00032). Products: heme d (molecule.ecocyc.HEME_D).

## Annotation

Heme-b + HYDROGEN-PEROXIDE -> HEME_D; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.HYDROPEROXIDII-CPLX|complex.ecocyc.HYDROPEROXIDII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.HEME_D|molecule.ecocyc.HEME_D]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00032|molecule.C00032]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-8073`

## Notes

Heme-b + HYDROGEN-PEROXIDE -> HEME_D; direction=PHYSIOL-LEFT-TO-RIGHT
