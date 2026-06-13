---
entity_id: "reaction.ecocyc.RXN0-5073"
entity_type: "reaction"
name: "RXN0-5073"
source_database: "EcoCyc"
source_id: "RXN0-5073"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5073

`reaction.ecocyc.RXN0-5073`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5073`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ITP + WATER -> PROTON + IDP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ITP + WATER -> PROTON + IDP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by inosine/xanthosine triphosphatase (complex.ecocyc.CPLX0-3948). Substrates: H2O (molecule.C00001), ITP (molecule.C00081). Products: H+ (molecule.C00080), IDP (molecule.C00104), phosphate (molecule.ecocyc.Pi).

## Annotation

ITP + WATER -> PROTON + IDP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3948|complex.ecocyc.CPLX0-3948]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00104|molecule.C00104]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00081|molecule.C00081]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5073`

## Notes

ITP + WATER -> PROTON + IDP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
