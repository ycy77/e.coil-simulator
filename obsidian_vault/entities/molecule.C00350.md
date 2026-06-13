---
entity_id: "molecule.C00350"
entity_type: "small_molecule"
name: "Phosphatidylethanolamine"
source_database: "KEGG"
source_id: "C00350"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Phosphatidylethanolamine"
  - "(3-Phosphatidyl)ethanolamine"
  - "(3-Phosphatidyl)-ethanolamine"
  - "Cephalin"
  - "O-(1-beta-Acyl-2-acyl-sn-glycero-3-phospho)ethanolamine"
  - "1-Acyl-2-acyl-sn-glycero-3-phosphoethanolamine"
  - "L-1-Phosphatidylethanolamine"
---

# Phosphatidylethanolamine

`molecule.C00350`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00350`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Phosphatidylethanolamine; (3-Phosphatidyl)ethanolamine; (3-Phosphatidyl)-ethanolamine; Cephalin; O-(1-beta-Acyl-2-acyl-sn-glycero-3-phospho)ethanolamine; 1-Acyl-2-acyl-sn-glycero-3-phosphoethanolamine; L-1-Phosphatidylethanolamine EcoCyc common name: a phosphatidylethanolamine. Phosphatidylethanolamines are a class of Phosphoglycerides phosphoglycerolipids" found in biological membranes. They are synthesized by the addition of an ethanolamine group from CDP-ethanolamine to Diacylglycerides diglycerides. Phosphatidylethanolamines are found in all living cells, composing 25% of all phospholipids.

## Biological Role

Consumed as substrate in 12 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

KEGG compound: Phosphatidylethanolamine; (3-Phosphatidyl)ethanolamine; (3-Phosphatidyl)-ethanolamine; Cephalin; O-(1-beta-Acyl-2-acyl-sn-glycero-3-phospho)ethanolamine; 1-Acyl-2-acyl-sn-glycero-3-phosphoethanolamine; L-1-Phosphatidylethanolamine

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (15)

- `activates` --> [[reaction.ecocyc.CARDIOLIPSYN-RXN|reaction.ecocyc.CARDIOLIPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.ACYLGPEACYLTRANS-RXN|reaction.ecocyc.ACYLGPEACYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PHOSPHASERDECARB-RXN|reaction.ecocyc.PHOSPHASERDECARB-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14363|reaction.ecocyc.RXN-14363]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14379|reaction.ecocyc.RXN-14379]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15210|reaction.ecocyc.RXN-15210]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16286|reaction.ecocyc.RXN-16286]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19630|reaction.ecocyc.RXN-19630]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19774|reaction.ecocyc.RXN-19774]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22561|reaction.ecocyc.RXN-22561]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4581|reaction.ecocyc.RXN0-4581]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6725|reaction.ecocyc.RXN0-6725]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6952|reaction.ecocyc.RXN0-6952]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7012|reaction.ecocyc.RXN0-7012]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7272|reaction.ecocyc.RXN0-7272]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00350`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
