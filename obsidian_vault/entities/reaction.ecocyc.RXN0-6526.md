---
entity_id: "reaction.ecocyc.RXN0-6526"
entity_type: "reaction"
name: "RXN0-6526"
source_database: "EcoCyc"
source_id: "RXN0-6526"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6526

`reaction.ecocyc.RXN0-6526`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6526`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

23S-rRNAs + WATER -> rRNA-fragments; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 23S-rRNAs + WATER -> rRNA-fragments; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rna (protein.P21338). Substrates: H2O (molecule.C00001).

## Annotation

23S-rRNAs + WATER -> rRNA-fragments; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P21338|protein.P21338]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6526`

## Notes

23S-rRNAs + WATER -> rRNA-fragments; direction=PHYSIOL-LEFT-TO-RIGHT
