---
entity_id: "reaction.ecocyc.TRANS-RXN-349"
entity_type: "reaction"
name: "deoxycholate:Na+ antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-349"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# deoxycholate:Na+ antiport

`reaction.ecocyc.TRANS-RXN-349`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-349`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

DEOXYCHOLATE + NA+ -> DEOXYCHOLATE + NA+; direction=REVERSIBLE EcoCyc reaction equation: DEOXYCHOLATE + NA+ -> DEOXYCHOLATE + NA+; direction=REVERSIBLE.

## Biological Role

Catalyzed by mdtK (protein.P37340). Substrates: Sodium cation (molecule.C01330), Deoxycholic acid (molecule.C04483). Products: Sodium cation (molecule.C01330), Deoxycholic acid (molecule.C04483).

## Annotation

DEOXYCHOLATE + NA+ -> DEOXYCHOLATE + NA+; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37340|protein.P37340]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04483|molecule.C04483]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04483|molecule.C04483]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-349`

## Notes

DEOXYCHOLATE + NA+ -> DEOXYCHOLATE + NA+; direction=REVERSIBLE
