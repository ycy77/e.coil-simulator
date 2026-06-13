---
entity_id: "molecule.C00229"
entity_type: "small_molecule"
name: "Acyl-carrier protein"
source_database: "KEGG"
source_id: "C00229"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Acyl-carrier protein"
  - "ACP"
  - "[Acyl-carrier protein]"
  - "Holo-[acyl-carrier protein]"
---

# Acyl-carrier protein

`molecule.C00229`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00229`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Acyl-carrier protein; ACP; [Acyl-carrier protein]; Holo-[acyl-carrier protein]

## Biological Role

Produced in 7 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Annotation

KEGG compound: Acyl-carrier protein; ACP; [Acyl-carrier protein]; Holo-[acyl-carrier protein]

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.R04726|reaction.R04726]] `KEGG` `database` - C05223 + C01209 <=> C05759 + C00011 + C00229
- `is_product_of` --> [[reaction.R04957|reaction.R04957]] `KEGG` `database` - C05749 + C01209 <=> C05750 + C00011 + C00229
- `is_product_of` --> [[reaction.R04960|reaction.R04960]] `KEGG` `database` - C05752 + C01209 <=> C05753 + C00011 + C00229
- `is_product_of` --> [[reaction.R04963|reaction.R04963]] `KEGG` `database` - C05755 + C01209 <=> C05756 + C00011 + C00229
- `is_product_of` --> [[reaction.R07766|reaction.R07766]] `KEGG` `database` - C05752 + C16240 <=> C16236 + C00229
- `is_product_of` --> [[reaction.R07769|reaction.R07769]] `KEGG` `database` - C16239 + C16240 <=> C16237 + C00229
- `is_product_of` --> [[reaction.R10906|reaction.R10906]] `KEGG` `database` - C16520 + C06025 <=> C20933 + C00229

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00229`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
