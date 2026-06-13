---
entity_id: "molecule.C04233"
entity_type: "small_molecule"
name: "2-Acyl-sn-glycero-3-phosphocholine"
source_database: "KEGG"
source_id: "C04233"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Acyl-sn-glycero-3-phosphocholine"
  - "2-Acylglycero-3-phosphocholine"
  - "1-Lysophosphatidylcholine"
  - "1-Lysolecithin"
  - "3-Lysolecithin"
---

# 2-Acyl-sn-glycero-3-phosphocholine

`molecule.C04233`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04233`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Acyl-sn-glycero-3-phosphocholine; 2-Acylglycero-3-phosphocholine; 1-Lysophosphatidylcholine; 1-Lysolecithin; 3-Lysolecithin EcoCyc common name: a 1-lysophosphatidylcholine.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

KEGG compound: 2-Acyl-sn-glycero-3-phosphocholine; 2-Acylglycero-3-phosphocholine; 1-Lysophosphatidylcholine; 1-Lysolecithin; 3-Lysolecithin

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R01314|reaction.R01314]] `KEGG` `database` - C00157 + C00001 <=> C04233 + C00060
- `is_product_of` --> [[reaction.R01316|reaction.R01316]] `KEGG` `database` - C00157 + C00001 <=> C04233 + C00162
- `is_product_of` --> [[reaction.ecocyc.RXN-20918|reaction.ecocyc.RXN-20918]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-1842|reaction.ecocyc.RXN0-1842]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16225|reaction.ecocyc.RXN-16225]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04233`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
