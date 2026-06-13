---
entity_id: "reaction.ecocyc.RXN-12070"
entity_type: "reaction"
name: "RXN-12070"
source_database: "EcoCyc"
source_id: "RXN-12070"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "2-hydroxy-6-oxonona-2,4-dienedioate hydrolase"
---

# RXN-12070

`reaction.ecocyc.RXN-12070`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12070`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2184 + WATER -> CPD-14447 + FUM + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2184 + WATER -> CPD-14447 + FUM + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 2-hydroxy-6-oxononatrienedioate hydrolase (complex.ecocyc.CPLX0-7950). Substrates: H2O (molecule.C00001), 2-Hydroxy-6-ketononatrienedioate (molecule.C12624). Products: H+ (molecule.C00080), Fumarate (molecule.C00122), (2Z)-2-hydroxypenta-2,4-dienoate (molecule.ecocyc.CPD-14447).

## Enriched Pathways

- `ecocyc.PWY-6690` cinnamate and 3-hydroxycinnamate degradation to 2-hydroxypentadienoate (EcoCyc)

## Annotation

CPD0-2184 + WATER -> CPD-14447 + FUM + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6690` cinnamate and 3-hydroxycinnamate degradation to 2-hydroxypentadienoate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7950|complex.ecocyc.CPLX0-7950]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-14447|molecule.ecocyc.CPD-14447]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C12624|molecule.C12624]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12070`

## Notes

CPD0-2184 + WATER -> CPD-14447 + FUM + PROTON; direction=LEFT-TO-RIGHT
