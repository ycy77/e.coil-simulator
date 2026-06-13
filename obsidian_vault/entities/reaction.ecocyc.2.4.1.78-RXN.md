---
entity_id: "reaction.ecocyc.2.4.1.78-RXN"
entity_type: "reaction"
name: "2.4.1.78-RXN"
source_database: "EcoCyc"
source_id: "2.4.1.78-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2.4.1.78-RXN

`reaction.ecocyc.2.4.1.78-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.4.1.78-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-12575 + CPD-9646 -> CPD-20966 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-12575 + CPD-9646 -> CPD-20966 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yfdH (protein.P77293). Substrates: UDP-glucose (molecule.C00029), di-trans,poly-cis-Undecaprenyl phosphate (molecule.C17556). Products: UDP (molecule.C00015), β-D-Glc-PP-Und (molecule.ecocyc.CPD-20966).

## Annotation

CPD-12575 + CPD-9646 -> CPD-20966 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P77293|protein.P77293]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20966|molecule.ecocyc.CPD-20966]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00029|molecule.C00029]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C17556|molecule.C17556]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.4.1.78-RXN`

## Notes

CPD-12575 + CPD-9646 -> CPD-20966 + UDP; direction=PHYSIOL-LEFT-TO-RIGHT
