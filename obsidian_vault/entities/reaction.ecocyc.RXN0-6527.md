---
entity_id: "reaction.ecocyc.RXN0-6527"
entity_type: "reaction"
name: "RXN0-6527"
source_database: "EcoCyc"
source_id: "RXN0-6527"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6527

`reaction.ecocyc.RXN0-6527`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6527`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

ssRNA-Holder + WATER -> rRNA-fragments; direction=LEFT-TO-RIGHT EcoCyc reaction equation: ssRNA-Holder + WATER -> rRNA-fragments; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rna (protein.P21338). Substrates: H2O (molecule.C00001), a single-stranded RNA (molecule.ecocyc.ssRNA-Holder).

## Annotation

ssRNA-Holder + WATER -> rRNA-fragments; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P21338|protein.P21338]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.ssRNA-Holder|molecule.ecocyc.ssRNA-Holder]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-6527`

## Notes

ssRNA-Holder + WATER -> rRNA-fragments; direction=LEFT-TO-RIGHT
