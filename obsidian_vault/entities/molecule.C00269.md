---
entity_id: "molecule.C00269"
entity_type: "small_molecule"
name: "CDP-diacylglycerol"
source_database: "KEGG"
source_id: "C00269"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "CDP-diacylglycerol"
  - "CDP-1,2-diacylglycerol"
  - "1,2-Diacyl-sn-glycero-3-cytidine-5'-diphosphate"
---

# CDP-diacylglycerol

`molecule.C00269`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00269`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: CDP-diacylglycerol; CDP-1,2-diacylglycerol; 1,2-Diacyl-sn-glycero-3-cytidine-5'-diphosphate EcoCyc common name: a CDP-diacylglycerol.

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

KEGG compound: CDP-diacylglycerol; CDP-1,2-diacylglycerol; 1,2-Diacyl-sn-glycero-3-cytidine-5'-diphosphate

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.CDPDIGLYSYN-RXN|reaction.ecocyc.CDPDIGLYSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.CDPDIGLYPYPHOSPHA-RXN|reaction.ecocyc.CDPDIGLYPYPHOSPHA-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PHOSPHAGLYPSYN-RXN|reaction.ecocyc.PHOSPHAGLYPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PHOSPHASERSYN-RXN|reaction.ecocyc.PHOSPHASERSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7499|reaction.ecocyc.RXN0-7499]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.PHOSPHAGLYPSYN-RXN|reaction.ecocyc.PHOSPHAGLYPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00269`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
