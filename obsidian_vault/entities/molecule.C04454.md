---
entity_id: "molecule.C04454"
entity_type: "small_molecule"
name: "5-Amino-6-(5'-phospho-D-ribitylamino)uracil"
source_database: "KEGG"
source_id: "C04454"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5-Amino-6-(5'-phospho-D-ribitylamino)uracil"
  - "5-Amino-2,6-dioxy-4-(5'-phospho-D-ribitylamino)pyrimidine"
  - "5-Amino-6-(5-phospho-D-ribitylamino)uracil"
---

# 5-Amino-6-(5'-phospho-D-ribitylamino)uracil

`molecule.C04454`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04454`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5-Amino-6-(5'-phospho-D-ribitylamino)uracil; 5-Amino-2,6-dioxy-4-(5'-phospho-D-ribitylamino)pyrimidine; 5-Amino-6-(5-phospho-D-ribitylamino)uracil EcoCyc common name: 5-amino-6-(5-phospho-D-ribitylamino)uracil.

## Biological Role

Consumed as substrate in 4 reaction(s).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Annotation

KEGG compound: 5-Amino-6-(5'-phospho-D-ribitylamino)uracil; 5-Amino-2,6-dioxy-4-(5'-phospho-D-ribitylamino)pyrimidine; 5-Amino-6-(5-phospho-D-ribitylamino)uracil

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Outgoing Edges (4)

- `is_substrate_of` --> [[reaction.R03458|reaction.R03458]] `KEGG` `database` - C04454 + C00006 <=> C01268 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R07280|reaction.R07280]] `KEGG` `database` - C04454 + C00001 <=> C04732 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.RIBOFLAVINSYNREDUC-RXN|reaction.ecocyc.RIBOFLAVINSYNREDUC-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RIBOPHOSPHAT-RXN|reaction.ecocyc.RIBOPHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04454`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
