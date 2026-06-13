---
entity_id: "reaction.ecocyc.TRANS-RXN-24"
entity_type: "reaction"
name: "lactose:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-24"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# lactose:proton symport

`reaction.ecocyc.TRANS-RXN-24`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-24`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + CPD-15972 -> PROTON + CPD-15972; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + CPD-15972 -> PROTON + CPD-15972; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by lacY (protein.P02920). Substrates: H+ (molecule.C00080), Lactose (molecule.C00243). Products: H+ (molecule.C00080), Lactose (molecule.C00243).

## Annotation

PROTON + CPD-15972 -> PROTON + CPD-15972; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P02920|protein.P02920]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00243|molecule.C00243]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00243|molecule.C00243]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-24`

## Notes

PROTON + CPD-15972 -> PROTON + CPD-15972; direction=LEFT-TO-RIGHT
