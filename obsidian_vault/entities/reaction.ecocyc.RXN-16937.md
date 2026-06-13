---
entity_id: "reaction.ecocyc.RXN-16937"
entity_type: "reaction"
name: "RXN-16937"
source_database: "EcoCyc"
source_id: "RXN-16937"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16937

`reaction.ecocyc.RXN-16937`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16937`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FMNH2 + CPD-14332 -> CPD-18260 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FMNH2 + CPD-14332 -> CPD-18260 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ubiX (protein.P0AG03). Substrates: Reduced FMN (molecule.C01847), Dimethylallyl phosphate (molecule.C21214). Products: Prenylated FMNH2 (molecule.C21215), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY0-1597` prenylated FMNH2 biosynthesis (EcoCyc)

## Annotation

FMNH2 + CPD-14332 -> CPD-18260 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1597` prenylated FMNH2 biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AG03|protein.P0AG03]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C21215|molecule.C21215]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01847|molecule.C01847]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C21214|molecule.C21214]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-16937`

## Notes

FMNH2 + CPD-14332 -> CPD-18260 + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
