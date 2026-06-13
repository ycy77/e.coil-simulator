---
entity_id: "reaction.ecocyc.RXN0-5121"
entity_type: "reaction"
name: "RXN0-5121"
source_database: "EcoCyc"
source_id: "RXN0-5121"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5121

`reaction.ecocyc.RXN0-5121`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5121`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-932 + ATP -> PROTON + CPD0-933 + ADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-932 + ATP -> PROTON + CPD0-933 + ADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaP (protein.P25741). Substrates: ATP (molecule.C00002), glucosyl-(heptosyl)2-Kdo2-lipid A (molecule.ecocyc.CPD0-932). Products: ADP (molecule.C00008), H+ (molecule.C00080), glucosyl-(heptosyl)2-Kdo2-lipid A-phosphate (molecule.ecocyc.CPD0-933).

## Annotation

CPD0-932 + ATP -> PROTON + CPD0-933 + ADP; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P25741|protein.P25741]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-933|molecule.ecocyc.CPD0-933]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-932|molecule.ecocyc.CPD0-932]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5121`

## Notes

CPD0-932 + ATP -> PROTON + CPD0-933 + ADP; direction=LEFT-TO-RIGHT
