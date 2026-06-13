---
entity_id: "reaction.ecocyc.RXN-17010"
entity_type: "reaction"
name: "RXN-17010"
source_database: "EcoCyc"
source_id: "RXN-17010"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17010

`reaction.ecocyc.RXN-17010`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17010`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-18346 + 1-PALMITOYLGLYCEROL-3-PHOSPHATE -> CPD-18352 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-18346 + 1-PALMITOYLGLYCEROL-3-PHOSPHATE -> CPD-18352 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: cis-Vaccenoyl-CoA (molecule.C21945), 1-palmitoyl-sn-glycerol 3-phosphate (molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE). Products: CoA (molecule.C00010), 1-palmitoyl-2-cis-vaccenoyl phosphatidate (molecule.ecocyc.CPD-18352).

## Annotation

CPD-18346 + 1-PALMITOYLGLYCEROL-3-PHOSPHATE -> CPD-18352 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-18352|molecule.ecocyc.CPD-18352]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C21945|molecule.C21945]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE|molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17010`

## Notes

CPD-18346 + 1-PALMITOYLGLYCEROL-3-PHOSPHATE -> CPD-18352 + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
