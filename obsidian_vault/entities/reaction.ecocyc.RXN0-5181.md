---
entity_id: "reaction.ecocyc.RXN0-5181"
entity_type: "reaction"
name: "RXN0-5181"
source_database: "EcoCyc"
source_id: "RXN0-5181"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5181

`reaction.ecocyc.RXN0-5181`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5181`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

1-4-alpha-D-Glucan + WATER -> 1-4-alpha-D-Glucan + MALTOHEXAOSE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 1-4-alpha-D-Glucan + WATER -> 1-4-alpha-D-Glucan + MALTOHEXAOSE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by malS (protein.P25718). Substrates: H2O (molecule.C00001), Amylose (molecule.C00718). Products: Amylose (molecule.C00718), maltohexaose (molecule.ecocyc.MALTOHEXAOSE).

## Annotation

1-4-alpha-D-Glucan + WATER -> 1-4-alpha-D-Glucan + MALTOHEXAOSE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P25718|protein.P25718]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00718|molecule.C00718]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MALTOHEXAOSE|molecule.ecocyc.MALTOHEXAOSE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00718|molecule.C00718]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5181`

## Notes

1-4-alpha-D-Glucan + WATER -> 1-4-alpha-D-Glucan + MALTOHEXAOSE; direction=PHYSIOL-LEFT-TO-RIGHT
