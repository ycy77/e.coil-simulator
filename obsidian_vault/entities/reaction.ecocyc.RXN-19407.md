---
entity_id: "reaction.ecocyc.RXN-19407"
entity_type: "reaction"
name: "RXN-19407"
source_database: "EcoCyc"
source_id: "RXN-19407"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-19407

`reaction.ecocyc.RXN-19407`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-19407`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-602 + WATER -> CPD-20969 + CPD-15317; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-602 + WATER -> CPD-20969 + CPD-15317; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ybiA (protein.P30176). Substrates: H2O (molecule.C00001), 5-Amino-6-(5'-phosphoribosylamino)uracil (molecule.C01268). Products: D-ribofuranose 5-phosphate (molecule.ecocyc.CPD-15317), 5,6-diaminouracil (molecule.ecocyc.CPD-20969).

## Annotation

CPD-602 + WATER -> CPD-20969 + CPD-15317; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P30176|protein.P30176]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-15317|molecule.ecocyc.CPD-15317]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20969|molecule.ecocyc.CPD-20969]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01268|molecule.C01268]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-19407`

## Notes

CPD-602 + WATER -> CPD-20969 + CPD-15317; direction=PHYSIOL-LEFT-TO-RIGHT
