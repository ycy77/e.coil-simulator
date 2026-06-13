---
entity_id: "reaction.ecocyc.RXN-17024"
entity_type: "reaction"
name: "RXN-17024"
source_database: "EcoCyc"
source_id: "RXN-17024"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17024

`reaction.ecocyc.RXN-17024`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17024`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

1-PALMITOYLGLYCEROL-3-PHOSPHATE + Myristoyl-ACPs -> CPD-18390 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 1-PALMITOYLGLYCEROL-3-PHOSPHATE + Myristoyl-ACPs -> CPD-18390 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by plsC (protein.P26647). Substrates: 1-palmitoyl-sn-glycerol 3-phosphate (molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE). Products: 1-palmitoyl-2-myristoyl phosphatidate (molecule.ecocyc.CPD-18390).

## Annotation

1-PALMITOYLGLYCEROL-3-PHOSPHATE + Myristoyl-ACPs -> CPD-18390 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P26647|protein.P26647]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-18390|molecule.ecocyc.CPD-18390]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE|molecule.ecocyc.1-PALMITOYLGLYCEROL-3-PHOSPHATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17024`

## Notes

1-PALMITOYLGLYCEROL-3-PHOSPHATE + Myristoyl-ACPs -> CPD-18390 + ACP; direction=PHYSIOL-LEFT-TO-RIGHT
