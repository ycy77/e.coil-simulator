---
entity_id: "molecule.C05973"
entity_type: "small_molecule"
name: "2-Acyl-sn-glycero-3-phosphoethanolamine"
source_database: "KEGG"
source_id: "C05973"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Acyl-sn-glycero-3-phosphoethanolamine"
  - "L-1-Lysophosphatidylethanolamine"
  - "O-(2-Acyl-sn-glycero-3-phospho)-ethanolamine"
---

# 2-Acyl-sn-glycero-3-phosphoethanolamine

`molecule.C05973`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05973`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Acyl-sn-glycero-3-phosphoethanolamine; L-1-Lysophosphatidylethanolamine; O-(2-Acyl-sn-glycero-3-phospho)-ethanolamine EcoCyc common name: a 1-lysophosphatidylethanolamine.

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

KEGG compound: 2-Acyl-sn-glycero-3-phosphoethanolamine; L-1-Lysophosphatidylethanolamine; O-(2-Acyl-sn-glycero-3-phospho)-ethanolamine

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (9)

- `is_product_of` --> [[reaction.ecocyc.RXN-19774|reaction.ecocyc.RXN-19774]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-20914|reaction.ecocyc.RXN-20914]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6952|reaction.ecocyc.RXN0-6952]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-294|reaction.ecocyc.TRANS-RXN-294]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R03417|reaction.R03417]] `KEGG` `database` - C05973 + C00001 <=> C00162 + C01233
- `is_substrate_of` --> [[reaction.ecocyc.ACYLGPEACYLTRANS-RXN|reaction.ecocyc.ACYLGPEACYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19311|reaction.ecocyc.RXN-19311]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7122|reaction.ecocyc.RXN0-7122]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-294|reaction.ecocyc.TRANS-RXN-294]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05973`
- `EcoCyc:2-Acyl-glycero-3-phosphoethanolamine`
- `canonicalized_from:molecule.ecocyc.2-Acyl-glycero-3-phosphoethanolamine`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.2-Acyl-glycero-3-phosphoethanolamine: EcoCyc:2-Acyl-glycero-3-phosphoethanolamine
