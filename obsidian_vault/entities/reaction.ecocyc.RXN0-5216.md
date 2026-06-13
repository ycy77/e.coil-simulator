---
entity_id: "reaction.ecocyc.RXN0-5216"
entity_type: "reaction"
name: "RXN0-5216"
source_database: "EcoCyc"
source_id: "RXN0-5216"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5216

`reaction.ecocyc.RXN0-5216`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5216`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1063 + WATER -> CPD-15979 + GLYCERATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1063 + WATER -> CPD-15979 + GLYCERATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mngB (protein.P54746). Substrates: H2O (molecule.C00001), 2-O-(6-Phospho-alpha-mannosyl)-D-glycerate (molecule.C16699). Products: D-Glycerate (molecule.C00258), D-mannopyranose 6-phosphate (molecule.ecocyc.CPD-15979).

## Enriched Pathways

- `ecocyc.PWY0-1300` 2-O-α-mannosyl-D-glycerate degradation (EcoCyc)

## Annotation

CPD0-1063 + WATER -> CPD-15979 + GLYCERATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1300` 2-O-α-mannosyl-D-glycerate degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P54746|protein.P54746]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00258|molecule.C00258]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-15979|molecule.ecocyc.CPD-15979]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C16699|molecule.C16699]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5216`

## Notes

CPD0-1063 + WATER -> CPD-15979 + GLYCERATE; direction=PHYSIOL-LEFT-TO-RIGHT
