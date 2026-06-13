---
entity_id: "reaction.ecocyc.TRANS-RXN-188"
entity_type: "reaction"
name: "sodium:potassium symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-188"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# sodium:potassium symport

`reaction.ecocyc.TRANS-RXN-188`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-188`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

K+ + NA+ -> K+ + NA+; direction=LEFT-TO-RIGHT EcoCyc reaction equation: K+ + NA+ -> K+ + NA+; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by trkG (protein.P23849). Substrates: Potassium cation (molecule.C00238), Sodium cation (molecule.C01330). Products: Potassium cation (molecule.C00238), Sodium cation (molecule.C01330).

## Annotation

K+ + NA+ -> K+ + NA+; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P23849|protein.P23849]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-188`

## Notes

K+ + NA+ -> K+ + NA+; direction=LEFT-TO-RIGHT
