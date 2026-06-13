---
entity_id: "molecule.C04778"
entity_type: "small_molecule"
name: "N1-(5-Phospho-alpha-D-ribosyl)-5,6-dimethylbenzimidazole"
source_database: "KEGG"
source_id: "C04778"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N1-(5-Phospho-alpha-D-ribosyl)-5,6-dimethylbenzimidazole"
  - "alpha-Ribazole 5'-phosphate"
---

# N1-(5-Phospho-alpha-D-ribosyl)-5,6-dimethylbenzimidazole

`molecule.C04778`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04778`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N1-(5-Phospho-alpha-D-ribosyl)-5,6-dimethylbenzimidazole; alpha-Ribazole 5'-phosphate EcoCyc common name: α-ribazole 5'-phosphate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: N1-(5-Phospho-alpha-D-ribosyl)-5,6-dimethylbenzimidazole; alpha-Ribazole 5'-phosphate

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R04148|reaction.R04148]] `KEGG` `database` - C01185 + C03114 <=> C00253 + C04778 + C00080
- `is_product_of` --> [[reaction.ecocyc.DMBPPRIBOSYLTRANS-RXN|reaction.ecocyc.DMBPPRIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.COBALAMIN5PSYN-RXN|reaction.ecocyc.COBALAMIN5PSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16788|reaction.ecocyc.RXN-16788]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04778`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
