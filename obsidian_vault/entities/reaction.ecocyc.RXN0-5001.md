---
entity_id: "reaction.ecocyc.RXN0-5001"
entity_type: "reaction"
name: "RXN0-5001"
source_database: "EcoCyc"
source_id: "RXN0-5001"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5001

`reaction.ecocyc.RXN0-5001`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5001`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

1-4-beta-Xylan + WATER -> CPD-25028; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 1-4-beta-Xylan + WATER -> CPD-25028; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by α-D-xyloside xylohydrolase (complex.ecocyc.CPLX0-3901). Substrates: H2O (molecule.C00001), 1,4-beta-D-Xylan (molecule.C02352). Products: α-D-xylopyranose (molecule.ecocyc.CPD-25028).

## Annotation

1-4-beta-Xylan + WATER -> CPD-25028; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3901|complex.ecocyc.CPLX0-3901]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-25028|molecule.ecocyc.CPD-25028]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02352|molecule.C02352]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.1-DEOXYXYLONOJIRIMYCIN|molecule.ecocyc.1-DEOXYXYLONOJIRIMYCIN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5001`

## Notes

1-4-beta-Xylan + WATER -> CPD-25028; direction=PHYSIOL-LEFT-TO-RIGHT
