---
entity_id: "molecule.C11437"
entity_type: "small_molecule"
name: "1-Deoxy-D-xylulose 5-phosphate"
source_database: "KEGG"
source_id: "C11437"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "1-Deoxy-D-xylulose 5-phosphate"
---

# 1-Deoxy-D-xylulose 5-phosphate

`molecule.C11437`

## Static

- Type: `small_molecule`
- Source: `KEGG:C11437`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 1-Deoxy-D-xylulose 5-phosphate

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)

## Annotation

KEGG compound: 1-Deoxy-D-xylulose 5-phosphate

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00730` Thiamine metabolism (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)

## Outgoing Edges (9)

- `is_product_of` --> [[reaction.ecocyc.DXPREDISOM-RXN|reaction.ecocyc.DXPREDISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DXS-RXN|reaction.ecocyc.DXS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-382|reaction.ecocyc.RXN0-382]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R05838|reaction.R05838]] `KEGG` `database` - C11638 + C11437 <=> C00627 + C00009 + 2 C00001
- `is_substrate_of` --> [[reaction.R10247|reaction.R10247]] `KEGG` `database` - C11437 + C15809 + C15814 <=> C20246 + C15810 + 2 C00001
- `is_substrate_of` --> [[reaction.ecocyc.PDXJ-RXN|reaction.ecocyc.PDXJ-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7141|reaction.ecocyc.RXN0-7141]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7196|reaction.ecocyc.RXN0-7196]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.THIAZOLSYN2-RXN|reaction.ecocyc.THIAZOLSYN2-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C11437`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
