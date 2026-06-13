---
entity_id: "reaction.ecocyc.5-OXOPROLINASE-ATP-HYDROLYSING-RXN"
entity_type: "reaction"
name: "5-OXOPROLINASE-ATP-HYDROLYSING-RXN"
source_database: "EcoCyc"
source_id: "5-OXOPROLINASE-ATP-HYDROLYSING-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 5-OXOPROLINASE-ATP-HYDROLYSING-RXN

`reaction.ecocyc.5-OXOPROLINASE-ATP-HYDROLYSING-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:5-OXOPROLINASE-ATP-HYDROLYSING-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-OXOPROLINE + WATER + ATP -> PROTON + GLT + Pi + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 5-OXOPROLINE + WATER + ATP -> PROTON + GLT + Pi + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 5-oxoprolinase (complex.ecocyc.CPLX0-8249). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), 5-Oxoproline (molecule.C01879). Products: ADP (molecule.C00008), L-Glutamate (molecule.C00025), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

5-OXOPROLINE + WATER + ATP -> PROTON + GLT + Pi + ADP; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8249|complex.ecocyc.CPLX0-8249]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01879|molecule.C01879]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:5-OXOPROLINASE-ATP-HYDROLYSING-RXN`

## Notes

5-OXOPROLINE + WATER + ATP -> PROTON + GLT + Pi + ADP; direction=LEFT-TO-RIGHT
