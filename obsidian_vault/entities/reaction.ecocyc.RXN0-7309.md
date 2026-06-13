---
entity_id: "reaction.ecocyc.RXN0-7309"
entity_type: "reaction"
name: "RXN0-7309"
source_database: "EcoCyc"
source_id: "RXN0-7309"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7309

`reaction.ecocyc.RXN0-7309`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7309`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-4211 + WATER -> CPD-14332 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-4211 + WATER -> CPD-14332 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ADP-sugar pyrophosphatase (complex.ecocyc.CPLX0-3721), nudJ (protein.P0AEI6). Substrates: H2O (molecule.C00001), Dimethylallyl diphosphate (molecule.C00235). Products: H+ (molecule.C00080), Dimethylallyl phosphate (molecule.C21214), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY0-1597` prenylated FMNH2 biosynthesis (EcoCyc)

## Annotation

CPD-4211 + WATER -> CPD-14332 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1597` prenylated FMNH2 biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3721|complex.ecocyc.CPLX0-3721]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AEI6|protein.P0AEI6]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C21214|molecule.C21214]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00235|molecule.C00235]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7309`

## Notes

CPD-4211 + WATER -> CPD-14332 + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
