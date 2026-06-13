---
entity_id: "reaction.ecocyc.RXN-17008"
entity_type: "reaction"
name: "RXN-17008"
source_database: "EcoCyc"
source_id: "RXN-17008"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17008

`reaction.ecocyc.RXN-17008`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17008`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-10269 + 1-PALMITOYLGLYCEROL-3-PHOSPHATE -> CPD-18350 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-10269 + 1-PALMITOYLGLYCEROL-3-PHOSPHATE -> CPD-18350 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Palmitoleoyl-CoA (molecule.C21072), 1-palmitoyl-sn-glycerol 3-phosphate (molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE). Products: CoA (molecule.C00010), 1-palmitoyl-2-palmitoleoyl-sn-glycerol 3-phosphate (molecule.ecocyc.CPD-18350).

## Annotation

CPD-10269 + 1-PALMITOYLGLYCEROL-3-PHOSPHATE -> CPD-18350 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-18350|molecule.ecocyc.CPD-18350]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C21072|molecule.C21072]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE|molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17008`

## Notes

CPD-10269 + 1-PALMITOYLGLYCEROL-3-PHOSPHATE -> CPD-18350 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
