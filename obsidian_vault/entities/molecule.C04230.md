---
entity_id: "molecule.C04230"
entity_type: "small_molecule"
name: "1-Acyl-sn-glycero-3-phosphocholine"
source_database: "KEGG"
source_id: "C04230"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "1-Acyl-sn-glycero-3-phosphocholine"
  - "1-Acyl-sn-glycerol-3-phosphocholine"
  - "alpha-Acylglycerophosphocholine"
  - "2-Lysolecithin"
  - "2-Lysophosphatidylcholine"
  - "1-Acylglycerophosphocholine"
---

# 1-Acyl-sn-glycero-3-phosphocholine

`molecule.C04230`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04230`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 1-Acyl-sn-glycero-3-phosphocholine; 1-Acyl-sn-glycerol-3-phosphocholine; alpha-Acylglycerophosphocholine; 2-Lysolecithin; 2-Lysophosphatidylcholine; 1-Acylglycerophosphocholine EcoCyc common name: a 2-lysophosphatidylcholine. Lysolecithins, or acyl-sn-glycero-3-phosphocholines, are derivatives of phosphatidylcholine, resulting from hydrolytic removal of one of the two acyl groups. The instances of this class include different variations based on the specific acyl group which has been removed. The structure below is an example of such an instance.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

KEGG compound: 1-Acyl-sn-glycero-3-phosphocholine; 1-Acyl-sn-glycerol-3-phosphocholine; alpha-Acylglycerophosphocholine; 2-Lysolecithin; 2-Lysophosphatidylcholine; 1-Acylglycerophosphocholine

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R01313|reaction.R01313]] `KEGG` `database` - C00157 + C00001 <=> C04230 + C00060
- `is_product_of` --> [[reaction.R01315|reaction.R01315]] `KEGG` `database` - C00157 + C00001 <=> C04230 + C00162
- `is_product_of` --> [[reaction.R01317|reaction.R01317]] `KEGG` `database` - C00157 + C00001 <=> C04230 + C00219
- `is_substrate_of` --> [[reaction.R07291|reaction.R07291]] `KEGG` `database` - C04230 + C00001 <=> C00670 + C00060
- `is_substrate_of` --> [[reaction.ecocyc.LYSOPHOSPHOLIPASE-RXN|reaction.ecocyc.LYSOPHOSPHOLIPASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04230`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
