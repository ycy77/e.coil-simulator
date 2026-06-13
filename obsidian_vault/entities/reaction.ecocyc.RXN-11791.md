---
entity_id: "reaction.ecocyc.RXN-11791"
entity_type: "reaction"
name: "RXN-11791"
source_database: "EcoCyc"
source_id: "RXN-11791"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11791

`reaction.ecocyc.RXN-11791`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11791`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-12575 + CPD-9646 -> UMP + CPD-12773; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-12575 + CPD-9646 -> UMP + CPD-12773; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by wcaJ (protein.P71241). Substrates: UDP-glucose (molecule.C00029), di-trans,poly-cis-Undecaprenyl phosphate (molecule.C17556). Products: UMP (molecule.C00105), α-D-Glc-PP-Und (molecule.ecocyc.CPD-12773).

## Enriched Pathways

- `ecocyc.PWY-8243` colanic acid (Escherichia coli K12) biosynthesis (EcoCyc)

## Annotation

CPD-12575 + CPD-9646 -> UMP + CPD-12773; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-8243` colanic acid (Escherichia coli K12) biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P71241|protein.P71241]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00105|molecule.C00105]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-12773|molecule.ecocyc.CPD-12773]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00029|molecule.C00029]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C17556|molecule.C17556]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11791`

## Notes

CPD-12575 + CPD-9646 -> UMP + CPD-12773; direction=PHYSIOL-LEFT-TO-RIGHT
