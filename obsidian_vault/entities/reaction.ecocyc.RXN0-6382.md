---
entity_id: "reaction.ecocyc.RXN0-6382"
entity_type: "reaction"
name: "RXN0-6382"
source_database: "EcoCyc"
source_id: "RXN0-6382"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6382

`reaction.ecocyc.RXN0-6382`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6382`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ITP + WATER -> PROTON + IMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ITP + WATER -> PROTON + IMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dITP/XTP pyrophosphatase (complex.ecocyc.CPLX0-7826). Substrates: H2O (molecule.C00001), ITP (molecule.C00081). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), IMP (molecule.C00130).

## Annotation

ITP + WATER -> PROTON + IMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7826|complex.ecocyc.CPLX0-7826]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00130|molecule.C00130]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00081|molecule.C00081]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6382`

## Notes

ITP + WATER -> PROTON + IMP + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
