---
entity_id: "molecule.C00399"
entity_type: "small_molecule"
name: "Ubiquinone"
source_database: "KEGG"
source_id: "C00399"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Ubiquinone"
  - "Coenzyme Q"
  - "CoQ"
  - "Q"
---

# Ubiquinone

`molecule.C00399`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00399`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Ubiquinone; Coenzyme Q; CoQ; Q EcoCyc common name: ubiquinone-2.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: Ubiquinone; Coenzyme Q; CoQ; Q

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R11335|reaction.R11335]] `KEGG` `database` - 2 C00390 + C00007 + 8 C00080 <=> 2 C00399 + 2 C00001 + 8 C00080
- `is_substrate_of` --> [[reaction.R03145|reaction.R03145]] `KEGG` `database` - C00022 + C00399 + C00001 <=> C00033 + C00390 + C00011
- `is_substrate_of` --> [[reaction.R11945|reaction.R11945]] `KEGG` `database` - C00399 + C00004 + C00080 + 4 C00080 <=> C00390 + C00003 + 4 C00080

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00399`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
