---
entity_id: "reaction.ecocyc.RXN0-2561"
entity_type: "reaction"
name: "xenobiotic:Na+ antiport"
source_database: "EcoCyc"
source_id: "RXN0-2561"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# xenobiotic:Na+ antiport

`reaction.ecocyc.RXN0-2561`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2561`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Xenobiotic + NA+ -> Xenobiotic + NA+; direction=REVERSIBLE EcoCyc reaction equation: Xenobiotic + NA+ -> Xenobiotic + NA+; direction=REVERSIBLE.

## Biological Role

Catalyzed by mdtK (protein.P37340). Substrates: Sodium cation (molecule.C01330). Products: Sodium cation (molecule.C01330).

## Annotation

Xenobiotic + NA+ -> Xenobiotic + NA+; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P37340|protein.P37340]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2561`

## Notes

Xenobiotic + NA+ -> Xenobiotic + NA+; direction=REVERSIBLE
