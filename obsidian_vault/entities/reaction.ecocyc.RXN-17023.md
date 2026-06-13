---
entity_id: "reaction.ecocyc.RXN-17023"
entity_type: "reaction"
name: "RXN-17023"
source_database: "EcoCyc"
source_id: "RXN-17023"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17023

`reaction.ecocyc.RXN-17023`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17023`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

1-PALMITOYLGLYCEROL-3-PHOSPHATE + TETRADECANOYL-COA -> CPD-18390 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 1-PALMITOYLGLYCEROL-3-PHOSPHATE + TETRADECANOYL-COA -> CPD-18390 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Tetradecanoyl-CoA (molecule.C02593), 1-palmitoyl-sn-glycerol 3-phosphate (molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE). Products: CoA (molecule.C00010), 1-palmitoyl-2-myristoyl phosphatidate (molecule.ecocyc.CPD-18390).

## Annotation

1-PALMITOYLGLYCEROL-3-PHOSPHATE + TETRADECANOYL-COA -> CPD-18390 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-18390|molecule.ecocyc.CPD-18390]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C02593|molecule.C02593]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE|molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17023`

## Notes

1-PALMITOYLGLYCEROL-3-PHOSPHATE + TETRADECANOYL-COA -> CPD-18390 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
