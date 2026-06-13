---
entity_id: "reaction.R04430"
entity_type: "reaction"
name: "butyryl-[acp]:NADP+ trans-2-oxidoreductase"
source_database: "KEGG"
source_id: "R04430"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04430"
---

# butyryl-[acp]:NADP+ trans-2-oxidoreductase

`reaction.R04430`

## Static

- Type: `reaction`
- Source: `KEGG:R04430`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Butyryl-[acp] + NADP+ But-2-enoyl-[acyl-carrier protein] + NADPH + H+

## Biological Role

Catalyzed by fabI (protein.P0AEK4). Substrates: NADP+ (molecule.C00006), Butyryl-[acp] (molecule.C05745). Products: NADPH (molecule.C00005), H+ (molecule.C00080), But-2-enoyl-[acyl-carrier protein] (molecule.C04246).

## Annotation

Butyryl-[acp] + NADP+ <=> But-2-enoyl-[acyl-carrier protein] + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEK4|protein.P0AEK4]] `KEGG` `database` - via EC:1.3.1.10
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C05745 + C00006 <=> C04246 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C05745 + C00006 <=> C04246 + C00005 + C00080
- `is_product_of` <-- [[molecule.C04246|molecule.C04246]] `KEGG` `database` - C05745 + C00006 <=> C04246 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C05745 + C00006 <=> C04246 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C05745|molecule.C05745]] `KEGG` `database` - C05745 + C00006 <=> C04246 + C00005 + C00080

## External IDs

- `KEGG:R04430`

## Notes

EQUATION: C05745 + C00006 <=> C04246 + C00005 + C00080
