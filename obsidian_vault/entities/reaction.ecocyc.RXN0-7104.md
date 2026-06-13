---
entity_id: "reaction.ecocyc.RXN0-7104"
entity_type: "reaction"
name: "RXN0-7104"
source_database: "EcoCyc"
source_id: "RXN0-7104"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7104

`reaction.ecocyc.RXN0-7104`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7104`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-207 + WATER -> PHENYLACETATE + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-207 + WATER -> PHENYLACETATE + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phenylacetyl-CoA thioesterase (complex.ecocyc.CPLX0-3941). Substrates: H2O (molecule.C00001), Phenylacetyl-CoA (molecule.C00582). Products: CoA (molecule.C00010), H+ (molecule.C00080), Phenylacetic acid (molecule.C07086).

## Annotation

CPD-207 + WATER -> PHENYLACETATE + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3941|complex.ecocyc.CPLX0-3941]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C07086|molecule.C07086]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00582|molecule.C00582]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7104`

## Notes

CPD-207 + WATER -> PHENYLACETATE + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
