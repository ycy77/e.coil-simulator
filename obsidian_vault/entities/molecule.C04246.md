---
entity_id: "molecule.C04246"
entity_type: "small_molecule"
name: "But-2-enoyl-[acyl-carrier protein]"
source_database: "KEGG"
source_id: "C04246"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "But-2-enoyl-[acyl-carrier protein]"
  - "(2E)-But-2-enoyl-[acp]"
  - "(2E)-Butenoyl-[acp]"
---

# But-2-enoyl-[acyl-carrier protein]

`molecule.C04246`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04246`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: But-2-enoyl-[acyl-carrier protein]; (2E)-But-2-enoyl-[acp]; (2E)-Butenoyl-[acp]

## Biological Role

Produced in 3 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)

## Annotation

KEGG compound: But-2-enoyl-[acyl-carrier protein]; (2E)-But-2-enoyl-[acp]; (2E)-Butenoyl-[acp]

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R04428|reaction.R04428]] `KEGG` `database` - C04618 <=> C04246 + C00001
- `is_product_of` --> [[reaction.R04429|reaction.R04429]] `KEGG` `database` - C05745 + C00003 <=> C04246 + C00004 + C00080
- `is_product_of` --> [[reaction.R04430|reaction.R04430]] `KEGG` `database` - C05745 + C00006 <=> C04246 + C00005 + C00080

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04246`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
