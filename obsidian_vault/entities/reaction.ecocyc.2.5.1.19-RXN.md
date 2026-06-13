---
entity_id: "reaction.ecocyc.2.5.1.19-RXN"
entity_type: "reaction"
name: "2.5.1.19-RXN"
source_database: "EcoCyc"
source_id: "2.5.1.19-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "3-enol-pyruvoylshikimate-5-phosphate synthase"
---

# 2.5.1.19-RXN

`reaction.ecocyc.2.5.1.19-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.5.1.19-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the sixth step in the shikimate pathway EcoCyc reaction equation: SHIKIMATE-5P + PHOSPHO-ENOL-PYRUVATE -> 3-ENOLPYRUVYL-SHIKIMATE-5P + Pi; direction=REVERSIBLE. This is the sixth step in the shikimate pathway

## Biological Role

Catalyzed by aroA (protein.P0A6D3). Substrates: Phosphoenolpyruvate (molecule.C00074), Shikimate 3-phosphate (molecule.C03175). Products: 5-O-(1-Carboxyvinyl)-3-phosphoshikimate (molecule.C01269), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6163` chorismate biosynthesis from 3-dehydroquinate (EcoCyc)

## Annotation

This is the sixth step in the shikimate pathway

## Pathways

- `ecocyc.PWY-6163` chorismate biosynthesis from 3-dehydroquinate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `activates` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P0A6D3|protein.P0A6D3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01269|molecule.C01269]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03175|molecule.C03175]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01269|molecule.C01269]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.3-BROMOPYRUVATE|molecule.ecocyc.3-BROMOPYRUVATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1308|molecule.ecocyc.CPD0-1308]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:2.5.1.19-RXN`

## Notes

SHIKIMATE-5P + PHOSPHO-ENOL-PYRUVATE -> 3-ENOLPYRUVYL-SHIKIMATE-5P + Pi; direction=REVERSIBLE
