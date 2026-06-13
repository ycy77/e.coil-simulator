---
entity_id: "reaction.ecocyc.RXN0-382"
entity_type: "reaction"
name: "RXN0-382"
source_database: "EcoCyc"
source_id: "RXN0-382"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-382

`reaction.ecocyc.RXN0-382`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-382`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + CPD-1093 -> PROTON + DEOXYXYLULOSE-5P + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ATP + CPD-1093 -> PROTON + DEOXYXYLULOSE-5P + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by xylulokinase (complex.ecocyc.CPLX0-7466). Substrates: ATP (molecule.C00002), 1-deoxy-D-xylulose (molecule.ecocyc.CPD-1093). Products: ADP (molecule.C00008), H+ (molecule.C00080), 1-Deoxy-D-xylulose 5-phosphate (molecule.C11437).

## Annotation

ATP + CPD-1093 -> PROTON + DEOXYXYLULOSE-5P + ADP; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7466|complex.ecocyc.CPLX0-7466]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C11437|molecule.C11437]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-1093|molecule.ecocyc.CPD-1093]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-382`

## Notes

ATP + CPD-1093 -> PROTON + DEOXYXYLULOSE-5P + ADP; direction=LEFT-TO-RIGHT
