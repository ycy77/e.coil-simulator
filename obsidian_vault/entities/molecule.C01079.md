---
entity_id: "molecule.C01079"
entity_type: "small_molecule"
name: "Protoporphyrinogen IX"
source_database: "KEGG"
source_id: "C01079"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Protoporphyrinogen IX"
---

# Protoporphyrinogen IX

`molecule.C01079`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01079`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Protoporphyrinogen IX

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: Protoporphyrinogen IX

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.R06895|reaction.R06895]] `KEGG` `database` - C03263 + 2 C00019 <=> C01079 + 2 C00011 + 2 C00073 + 2 C05198
- `is_product_of` --> [[reaction.ecocyc.HEMN-RXN|reaction.ecocyc.HEMN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16330|reaction.ecocyc.RXN-16330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1461|reaction.ecocyc.RXN0-1461]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6259|reaction.ecocyc.RXN0-6259]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.PROTOPORGENOXI-RXN|reaction.ecocyc.PROTOPORGENOXI-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21483|reaction.ecocyc.RXN-21483]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01079`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
