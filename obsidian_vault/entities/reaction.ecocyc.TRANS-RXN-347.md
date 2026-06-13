---
entity_id: "reaction.ecocyc.TRANS-RXN-347"
entity_type: "reaction"
name: "norfloxacin:Na+ antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-347"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# norfloxacin:Na+ antiport

`reaction.ecocyc.TRANS-RXN-347`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-347`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-21015 + NA+ -> CPD-21015 + NA+; direction=REVERSIBLE EcoCyc reaction equation: CPD-21015 + NA+ -> CPD-21015 + NA+; direction=REVERSIBLE.

## Biological Role

Catalyzed by mdtK (protein.P37340). Substrates: Sodium cation (molecule.C01330), Norfloxacin (molecule.C06687). Products: Sodium cation (molecule.C01330), Norfloxacin (molecule.C06687).

## Annotation

CPD-21015 + NA+ -> CPD-21015 + NA+; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P37340|protein.P37340]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06687|molecule.C06687]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06687|molecule.C06687]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-347`

## Notes

CPD-21015 + NA+ -> CPD-21015 + NA+; direction=REVERSIBLE
