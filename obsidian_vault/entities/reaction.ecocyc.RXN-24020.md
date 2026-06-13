---
entity_id: "reaction.ecocyc.RXN-24020"
entity_type: "reaction"
name: "RXN-24020"
source_database: "EcoCyc"
source_id: "RXN-24020"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-24020

`reaction.ecocyc.RXN-24020`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-24020`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SPERMIDINE + CPD-26564 + ATP -> CPD-26565 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: SPERMIDINE + CPD-26564 + ATP -> CPD-26565 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ygiC (protein.P0ADT5), yjfC (protein.P33222). Substrates: ATP (molecule.C00002), Spermidine (molecule.C00315), triglycine (molecule.ecocyc.CPD-26564). Products: ADP (molecule.C00008), H+ (molecule.C00080), triglycylspermidine (molecule.ecocyc.CPD-26565), phosphate (molecule.ecocyc.Pi).

## Annotation

SPERMIDINE + CPD-26564 + ATP -> CPD-26565 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0ADT5|protein.P0ADT5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P33222|protein.P33222]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-26565|molecule.ecocyc.CPD-26565]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-26564|molecule.ecocyc.CPD-26564]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-24020`

## Notes

SPERMIDINE + CPD-26564 + ATP -> CPD-26565 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
