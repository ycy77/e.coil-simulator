---
entity_id: "molecule.C00345"
entity_type: "small_molecule"
name: "6-Phospho-D-gluconate"
source_database: "KEGG"
source_id: "C00345"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "6-Phospho-D-gluconate"
---

# 6-Phospho-D-gluconate

`molecule.C00345`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00345`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 6-Phospho-D-gluconate EcoCyc common name: D-gluconate 6-phosphate.

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)

## Annotation

KEGG compound: 6-Phospho-D-gluconate

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)

## Outgoing Edges (10)

- `is_product_of` --> [[reaction.R01737|reaction.R01737]] `KEGG` `database` - C00002 + C00257 <=> C00008 + C00345
- `is_product_of` --> [[reaction.ecocyc.6PGLUCONOLACT-RXN|reaction.ecocyc.6PGLUCONOLACT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLUCONOKIN-RXN|reaction.ecocyc.GLUCONOKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01528|reaction.R01528]] `KEGG` `database` - C00345 + C00006 <=> C00199 + C00011 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R10221|reaction.R10221]] `KEGG` `database` - C00345 + C00003 <=> C00199 + C00011 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.PGLUCONDEHYDRAT-RXN|reaction.ecocyc.PGLUCONDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9952|reaction.ecocyc.RXN-9952]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5185|reaction.ecocyc.RXN0-5185]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.KDPGALDOL-RXN|reaction.ecocyc.KDPGALDOL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PGLUCISOM-RXN|reaction.ecocyc.PGLUCISOM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00345`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
