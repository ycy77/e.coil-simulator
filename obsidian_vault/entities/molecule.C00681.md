---
entity_id: "molecule.C00681"
entity_type: "small_molecule"
name: "1-Acyl-sn-glycerol 3-phosphate"
source_database: "KEGG"
source_id: "C00681"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "1-Acyl-sn-glycerol 3-phosphate"
  - "2-Lysophosphatidate"
  - "Lysophosphatidate"
  - "Lysophosphatidic acid"
---

# 1-Acyl-sn-glycerol 3-phosphate

`molecule.C00681`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00681`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 1-Acyl-sn-glycerol 3-phosphate; 2-Lysophosphatidate; Lysophosphatidate; Lysophosphatidic acid EcoCyc common name: a 2-lysophosphatidate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

KEGG compound: 1-Acyl-sn-glycerol 3-phosphate; 2-Lysophosphatidate; Lysophosphatidate; Lysophosphatidic acid

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.R02617|reaction.R02617]] `KEGG` `database` - C00605 + C00093 <=> C00010 + C00681
- `is_product_of` --> [[reaction.ecocyc.RXN-10462|reaction.ecocyc.RXN-10462]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-1381|reaction.ecocyc.RXN-1381]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R11527|reaction.R11527]] `KEGG` `database` - C00681 + C00001 <=> C01885 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN|reaction.ecocyc.1-ACYLGLYCEROL-3-P-ACYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-1623|reaction.ecocyc.RXN-1623]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00681`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
