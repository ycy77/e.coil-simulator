---
entity_id: "molecule.C00416"
entity_type: "small_molecule"
name: "Phosphatidate"
source_database: "KEGG"
source_id: "C00416"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phosphatidate"
  - "Phosphatidic acid"
  - "1,2-Diacyl-sn-glycerol 3-phosphate"
  - "3-sn-Phosphatidate"
---

# Phosphatidate

`molecule.C00416`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00416`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phosphatidate; Phosphatidic acid; 1,2-Diacyl-sn-glycerol 3-phosphate; 3-sn-Phosphatidate EcoCyc common name: a phosphatidate. L-PHOSPHATIDATE "1,2-Diacyl-sn-glycerol-3-phosphate", often referred to as phosphatidate, is a class of compounds consisting of a GLYCEROL backbone, a (usually) saturated fatty acid bonded to carbon 1, a (usually) unsaturated fatty acid bonded to carbon 2, and a phosphate group esterified to carbon 3.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

KEGG compound: Phosphatidate; Phosphatidic acid; 1,2-Diacyl-sn-glycerol 3-phosphate; 3-sn-Phosphatidate

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.ecocyc.1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN|reaction.ecocyc.1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.CDPDIGLYPYPHOSPHA-RXN|reaction.ecocyc.CDPDIGLYPYPHOSPHA-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DIACYLGLYKIN-RXN|reaction.ecocyc.DIACYLGLYKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-11277|reaction.ecocyc.RXN-11277]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-1623|reaction.ecocyc.RXN-1623]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.CDPDIGLYSYN-RXN|reaction.ecocyc.CDPDIGLYSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.CARDIOLIPSYN-RXN|reaction.ecocyc.CARDIOLIPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00416`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
