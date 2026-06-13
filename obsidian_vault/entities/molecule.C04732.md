---
entity_id: "molecule.C04732"
entity_type: "small_molecule"
name: "5-Amino-6-(1-D-ribitylamino)uracil"
source_database: "KEGG"
source_id: "C04732"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5-Amino-6-(1-D-ribitylamino)uracil"
  - "5-Amino-6-(D-ribitylamino)uracil"
  - "6-(1-D-Ribitylamino)-5-amino-2,4-dihydroxypyrimidine"
  - "6-(1-D-Ribitylamino)-5-aminouracil"
  - "4-(1-D-Ribitylamino)-5-amino-2,6-dihydroxypyrimidine"
---

# 5-Amino-6-(1-D-ribitylamino)uracil

`molecule.C04732`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04732`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5-Amino-6-(1-D-ribitylamino)uracil; 5-Amino-6-(D-ribitylamino)uracil; 6-(1-D-Ribitylamino)-5-amino-2,4-dihydroxypyrimidine; 6-(1-D-Ribitylamino)-5-aminouracil; 4-(1-D-Ribitylamino)-5-amino-2,6-dihydroxypyrimidine EcoCyc common name: 5-amino-6-(D-ribitylamino)uracil.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)

## Annotation

KEGG compound: 5-Amino-6-(1-D-ribitylamino)uracil; 5-Amino-6-(D-ribitylamino)uracil; 6-(1-D-Ribitylamino)-5-amino-2,4-dihydroxypyrimidine; 6-(1-D-Ribitylamino)-5-aminouracil; 4-(1-D-Ribitylamino)-5-amino-2,6-dihydroxypyrimidine

## Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R00066|reaction.R00066]] `KEGG` `database` - 2 C04332 <=> C00255 + C04732
- `is_product_of` --> [[reaction.R07280|reaction.R07280]] `KEGG` `database` - C04454 + C00001 <=> C04732 + C00009
- `is_product_of` --> [[reaction.ecocyc.RIBOFLAVIN-SYN-RXN|reaction.ecocyc.RIBOFLAVIN-SYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RIBOPHOSPHAT-RXN|reaction.ecocyc.RIBOPHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.LUMAZINESYN-RXN|reaction.ecocyc.LUMAZINESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04732`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
