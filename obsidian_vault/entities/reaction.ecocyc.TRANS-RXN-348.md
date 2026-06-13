---
entity_id: "reaction.ecocyc.TRANS-RXN-348"
entity_type: "reaction"
name: "tetraphenylphosphonium:Na+ antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-348"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# tetraphenylphosphonium:Na+ antiport

`reaction.ecocyc.TRANS-RXN-348`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-348`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CPD-20890 + NA+ -> CPD-20890 + NA+; direction=REVERSIBLE EcoCyc reaction equation: CPD-20890 + NA+ -> CPD-20890 + NA+; direction=REVERSIBLE.

## Biological Role

Catalyzed by mdtK (protein.P37340). Substrates: Sodium cation (molecule.C01330), tetraphenylphosphonium (molecule.ecocyc.CPD-20890). Products: Sodium cation (molecule.C01330), tetraphenylphosphonium (molecule.ecocyc.CPD-20890).

## Annotation

CPD-20890 + NA+ -> CPD-20890 + NA+; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37340|protein.P37340]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-20890|molecule.ecocyc.CPD-20890]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-20890|molecule.ecocyc.CPD-20890]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-348`

## Notes

CPD-20890 + NA+ -> CPD-20890 + NA+; direction=REVERSIBLE
