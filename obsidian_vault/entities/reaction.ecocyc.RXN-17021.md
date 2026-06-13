---
entity_id: "reaction.ecocyc.RXN-17021"
entity_type: "reaction"
name: "RXN-17021"
source_database: "EcoCyc"
source_id: "RXN-17021"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17021

`reaction.ecocyc.RXN-17021`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17021`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TETRADECANOYL-COA + CPD-18379 -> CPD0-1425 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: TETRADECANOYL-COA + CPD-18379 -> CPD0-1425 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Tetradecanoyl-CoA (molecule.C02593), 1-myristoyl-sn-glycerol 3-phosphate (molecule.ecocyc.CPD-18379). Products: CoA (molecule.C00010), 1,2-dimyristoyl-sn-glycerol 3-phosphate (molecule.ecocyc.CPD0-1425).

## Annotation

TETRADECANOYL-COA + CPD-18379 -> CPD0-1425 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1425|molecule.ecocyc.CPD0-1425]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C02593|molecule.C02593]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-18379|molecule.ecocyc.CPD-18379]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17021`

## Notes

TETRADECANOYL-COA + CPD-18379 -> CPD0-1425 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
