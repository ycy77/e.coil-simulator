---
entity_id: "reaction.ecocyc.RXN0-5074"
entity_type: "reaction"
name: "RXN0-5074"
source_database: "EcoCyc"
source_id: "RXN0-5074"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5074

`reaction.ecocyc.RXN0-5074`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5074`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

XTP + WATER -> PROTON + XDP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: XTP + WATER -> PROTON + XDP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by inosine/xanthosine triphosphatase (complex.ecocyc.CPLX0-3948). Substrates: H2O (molecule.C00001), XTP (molecule.C00700). Products: H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi), XDP (molecule.ecocyc.XDP).

## Annotation

XTP + WATER -> PROTON + XDP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3948|complex.ecocyc.CPLX0-3948]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.XDP|molecule.ecocyc.XDP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00700|molecule.C00700]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5074`

## Notes

XTP + WATER -> PROTON + XDP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
