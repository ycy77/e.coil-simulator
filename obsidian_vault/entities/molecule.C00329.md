---
entity_id: "molecule.C00329"
entity_type: "small_molecule"
name: "D-Glucosamine"
source_database: "KEGG"
source_id: "C00329"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "D-Glucosamine"
  - "Chitosamine"
  - "2-Amino-2-deoxy-D-glucose"
---

# D-Glucosamine

`molecule.C00329`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00329`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: D-Glucosamine; Chitosamine; 2-Amino-2-deoxy-D-glucose

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: D-Glucosamine; Chitosamine; 2-Amino-2-deoxy-D-glucose

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.RXN-17745|reaction.ecocyc.RXN-17745]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GLUCOSAMINE-KINASE-RXN|reaction.ecocyc.GLUCOSAMINE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-167A|reaction.ecocyc.TRANS-RXN-167A]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLUCOKIN-RXN|reaction.ecocyc.GLUCOKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00329`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
