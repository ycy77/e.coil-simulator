---
entity_id: "reaction.ecocyc.RXN0-5223"
entity_type: "reaction"
name: "RXN0-5223"
source_database: "EcoCyc"
source_id: "RXN0-5223"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5223

`reaction.ecocyc.RXN0-5223`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5223`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-1-PHOSPHATIDYL-GLYCEROL + ATP -> L-1-PHOSPHATIDYL-GLYCEROL-P + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: L-1-PHOSPHATIDYL-GLYCEROL + ATP -> L-1-PHOSPHATIDYL-GLYCEROL-P + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yegS (protein.P76407). Substrates: ATP (molecule.C00002), Phosphatidylglycerol (molecule.C00344). Products: ADP (molecule.C00008), H+ (molecule.C00080), Phosphatidylglycerophosphate (molecule.C03892).

## Annotation

L-1-PHOSPHATIDYL-GLYCEROL + ATP -> L-1-PHOSPHATIDYL-GLYCEROL-P + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P76407|protein.P76407]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03892|molecule.C03892]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00344|molecule.C00344]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5223`

## Notes

L-1-PHOSPHATIDYL-GLYCEROL + ATP -> L-1-PHOSPHATIDYL-GLYCEROL-P + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
