---
entity_id: "reaction.ecocyc.RXN-17012"
entity_type: "reaction"
name: "RXN-17012"
source_database: "EcoCyc"
source_id: "RXN-17012"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17012

`reaction.ecocyc.RXN-17012`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17012`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Palmitoleoyl-ACPs + 1-PALMITOYLGLYCEROL-3-PHOSPHATE -> CPD-18350 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Palmitoleoyl-ACPs + 1-PALMITOYLGLYCEROL-3-PHOSPHATE -> CPD-18350 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by plsC (protein.P26647). Substrates: 1-palmitoyl-sn-glycerol 3-phosphate (molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE). Products: 1-palmitoyl-2-palmitoleoyl-sn-glycerol 3-phosphate (molecule.ecocyc.CPD-18350).

## Annotation

Palmitoleoyl-ACPs + 1-PALMITOYLGLYCEROL-3-PHOSPHATE -> CPD-18350 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P26647|protein.P26647]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-18350|molecule.ecocyc.CPD-18350]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE|molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17012`

## Notes

Palmitoleoyl-ACPs + 1-PALMITOYLGLYCEROL-3-PHOSPHATE -> CPD-18350 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT
