---
entity_id: "reaction.ecocyc.TRANS-RXN0-235"
entity_type: "reaction"
name: "2,3-dioxo-L-gulonate:Na+ symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-235"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2,3-dioxo-L-gulonate:Na+ symport

`reaction.ecocyc.TRANS-RXN0-235`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-235`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NA+ + CPD-334 -> NA+ + CPD-334; direction=LEFT-TO-RIGHT EcoCyc reaction equation: NA+ + CPD-334 -> NA+ + CPD-334; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 2,3-diketo-L-gulonate:Na+ symporter (complex.ecocyc.TRANS-CPLX-203). Substrates: Sodium cation (molecule.C01330), 2,3-didehydro-L-gulonate (molecule.ecocyc.CPD-334). Products: Sodium cation (molecule.C01330), 2,3-didehydro-L-gulonate (molecule.ecocyc.CPD-334).

## Annotation

NA+ + CPD-334 -> NA+ + CPD-334; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.TRANS-CPLX-203|complex.ecocyc.TRANS-CPLX-203]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-334|molecule.ecocyc.CPD-334]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-334|molecule.ecocyc.CPD-334]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-235`

## Notes

NA+ + CPD-334 -> NA+ + CPD-334; direction=LEFT-TO-RIGHT
