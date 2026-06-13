---
entity_id: "molecule.C02191"
entity_type: "small_molecule"
name: "Protoporphyrin"
source_database: "KEGG"
source_id: "C02191"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Protoporphyrin"
  - "Protoporphyrin IX"
  - "Porphyrinogen IX"
---

# Protoporphyrin

`molecule.C02191`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02191`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Protoporphyrin; Protoporphyrin IX; Porphyrinogen IX EcoCyc common name: protoporphyrin IX.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: Protoporphyrin; Protoporphyrin IX; Porphyrinogen IX

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.ecocyc.PROTOHEMEFERROCHELAT-RXN|reaction.ecocyc.PROTOHEMEFERROCHELAT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PROTOPORGENOXI-RXN|reaction.ecocyc.PROTOPORGENOXI-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21483|reaction.ecocyc.RXN-21483]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00310|reaction.R00310]] `KEGG` `database` - C02191 + C14818 <=> C00032 + 2 C00080
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16330|reaction.ecocyc.RXN-16330]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6259|reaction.ecocyc.RXN0-6259]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN0-1461|reaction.ecocyc.RXN0-1461]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02191`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
