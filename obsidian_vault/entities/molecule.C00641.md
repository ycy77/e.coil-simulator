---
entity_id: "molecule.C00641"
entity_type: "small_molecule"
name: "1,2-Diacyl-sn-glycerol"
source_database: "KEGG"
source_id: "C00641"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "1,2-Diacyl-sn-glycerol"
  - "1,2-Diacylglycerol"
  - "L-1,2-Diacylglycerol"
---

# 1,2-Diacyl-sn-glycerol

`molecule.C00641`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00641`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 1,2-Diacyl-sn-glycerol; 1,2-Diacylglycerol; L-1,2-Diacylglycerol EcoCyc common name: a 1,2-diacyl-sn-glycerol.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 8 reaction(s).

## Enriched Pathways

- `eco00552` Teichoic acid biosynthesis (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

KEGG compound: 1,2-Diacyl-sn-glycerol; 1,2-Diacylglycerol; L-1,2-Diacylglycerol

## Pathways

- `eco00552` Teichoic acid biosynthesis (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (11)

- `is_product_of` --> [[reaction.ecocyc.PGLYCEROLTRANSI-RXN|reaction.ecocyc.PGLYCEROLTRANSI-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14363|reaction.ecocyc.RXN-14363]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14379|reaction.ecocyc.RXN-14379]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15210|reaction.ecocyc.RXN-15210]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16286|reaction.ecocyc.RXN-16286]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19630|reaction.ecocyc.RXN-19630]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22561|reaction.ecocyc.RXN-22561]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-4581|reaction.ecocyc.RXN0-4581]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DIACYLGLYKIN-RXN|reaction.ecocyc.DIACYLGLYKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DIACYLGLYKIN-RXN|reaction.ecocyc.DIACYLGLYKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-14379|reaction.ecocyc.RXN-14379]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00641`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
