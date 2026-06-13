---
entity_id: "reaction.ecocyc.PEPCARBOXYKIN-RXN"
entity_type: "reaction"
name: "PEPCARBOXYKIN-RXN"
source_database: "EcoCyc"
source_id: "PEPCARBOXYKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PEPCARBOXYKIN-RXN

`reaction.ecocyc.PEPCARBOXYKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PEPCARBOXYKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a reaction of gluconeogenesis. EcoCyc reaction equation: OXALACETIC_ACID + ATP -> CARBON-DIOXIDE + PHOSPHO-ENOL-PYRUVATE + ADP; direction=REVERSIBLE. This is a reaction of gluconeogenesis.

## Biological Role

Catalyzed by pckA (protein.P22259). Substrates: ATP (molecule.C00002), Oxaloacetate (molecule.C00036). Products: ADP (molecule.C00008), CO2 (molecule.C00011), Phosphoenolpyruvate (molecule.C00074).

## Enriched Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)

## Annotation

This is a reaction of gluconeogenesis.

## Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P22259|protein.P22259]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PEPCARBOXYKIN-RXN`

## Notes

OXALACETIC_ACID + ATP -> CARBON-DIOXIDE + PHOSPHO-ENOL-PYRUVATE + ADP; direction=REVERSIBLE
