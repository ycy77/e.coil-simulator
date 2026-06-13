---
entity_id: "reaction.ecocyc.RXN-14455"
entity_type: "reaction"
name: "RXN-14455"
source_database: "EcoCyc"
source_id: "RXN-14455"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14455

`reaction.ecocyc.RXN-14455`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14455`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CU+ + ATP + WATER -> CU+ + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CU+ + ATP + WATER -> CU+ + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by copA (protein.Q59385). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), Cu+ (molecule.ecocyc.CU_). Products: ADP (molecule.C00008), H+ (molecule.C00080), Cu+ (molecule.ecocyc.CU_), phosphate (molecule.ecocyc.Pi).

## Annotation

CU+ + ATP + WATER -> CU+ + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.Q59385|protein.Q59385]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CU|molecule.ecocyc.CU_]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CU|molecule.ecocyc.CU_]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14455`

## Notes

CU+ + ATP + WATER -> CU+ + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
