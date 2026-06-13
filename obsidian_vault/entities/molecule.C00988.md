---
entity_id: "molecule.C00988"
entity_type: "small_molecule"
name: "2-Phosphoglycolate"
source_database: "KEGG"
source_id: "C00988"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Phosphoglycolate"
  - "Phosphoglycolic acid"
---

# 2-Phosphoglycolate

`molecule.C00988`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00988`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Phosphoglycolate; Phosphoglycolic acid

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Annotation

KEGG compound: 2-Phosphoglycolate; Phosphoglycolic acid

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.RXN-20429|reaction.ecocyc.RXN-20429]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GPH-RXN|reaction.ecocyc.GPH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.METHGLYSYN-RXN|reaction.ecocyc.METHGLYSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5260|reaction.ecocyc.RXN0-5260]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRIOSEPISOMERIZATION-RXN|reaction.ecocyc.TRIOSEPISOMERIZATION-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00988`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
