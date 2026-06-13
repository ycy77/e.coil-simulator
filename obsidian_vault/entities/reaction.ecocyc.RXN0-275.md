---
entity_id: "reaction.ecocyc.RXN0-275"
entity_type: "reaction"
name: "RXN0-275"
source_database: "EcoCyc"
source_id: "RXN0-275"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-275

`reaction.ecocyc.RXN0-275`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-275`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PHENYLHYDANTOIN + WATER -> CPD-8524 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PHENYLHYDANTOIN + WATER -> CPD-8524 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phenylhydantoinase (complex.ecocyc.CPLX0-255). Substrates: H2O (molecule.C00001), D-phenylhydantoin (molecule.ecocyc.PHENYLHYDANTOIN). Products: H+ (molecule.C00080), N-carbamoyl-D-phenylglycine (molecule.ecocyc.CPD-8524).

## Annotation

PHENYLHYDANTOIN + WATER -> CPD-8524 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-255|complex.ecocyc.CPLX0-255]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-8524|molecule.ecocyc.CPD-8524]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PHENYLHYDANTOIN|molecule.ecocyc.PHENYLHYDANTOIN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-275`

## Notes

PHENYLHYDANTOIN + WATER -> CPD-8524 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
