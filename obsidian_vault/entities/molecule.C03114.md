---
entity_id: "molecule.C03114"
entity_type: "small_molecule"
name: "Dimethylbenzimidazole"
source_database: "KEGG"
source_id: "C03114"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Dimethylbenzimidazole"
  - "5,6-Dimethylbenzimidazole"
---

# Dimethylbenzimidazole

`molecule.C03114`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03114`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Dimethylbenzimidazole; 5,6-Dimethylbenzimidazole EcoCyc common name: 5,6-dimethylbenzimidazole.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: Dimethylbenzimidazole; 5,6-Dimethylbenzimidazole

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-463|reaction.ecocyc.TRANS-RXN0-463]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R04148|reaction.R04148]] `KEGG` `database` - C01185 + C03114 <=> C00253 + C04778 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.DMBPPRIBOSYLTRANS-RXN|reaction.ecocyc.DMBPPRIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-463|reaction.ecocyc.TRANS-RXN0-463]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03114`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
