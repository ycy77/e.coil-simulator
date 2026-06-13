---
entity_id: "reaction.R04429"
entity_type: "reaction"
name: "butyryl-[acp]:NAD+ trans-2-oxidoreductase"
source_database: "KEGG"
source_id: "R04429"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04429"
---

# butyryl-[acp]:NAD+ trans-2-oxidoreductase

`reaction.R04429`

## Static

- Type: `reaction`
- Source: `KEGG:R04429`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Butyryl-[acp] + NAD+ But-2-enoyl-[acyl-carrier protein] + NADH + H+

## Biological Role

Catalyzed by fabI (protein.P0AEK4). Substrates: NAD+ (molecule.C00003), Butyryl-[acp] (molecule.C05745). Products: NADH (molecule.C00004), H+ (molecule.C00080), But-2-enoyl-[acyl-carrier protein] (molecule.C04246).

## Annotation

Butyryl-[acp] + NAD+ <=> But-2-enoyl-[acyl-carrier protein] + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEK4|protein.P0AEK4]] `KEGG` `database` - via EC:1.3.1.9
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C05745 + C00003 <=> C04246 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C05745 + C00003 <=> C04246 + C00004 + C00080
- `is_product_of` <-- [[molecule.C04246|molecule.C04246]] `KEGG` `database` - C05745 + C00003 <=> C04246 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C05745 + C00003 <=> C04246 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C05745|molecule.C05745]] `KEGG` `database` - C05745 + C00003 <=> C04246 + C00004 + C00080

## External IDs

- `KEGG:R04429`

## Notes

EQUATION: C05745 + C00003 <=> C04246 + C00004 + C00080
