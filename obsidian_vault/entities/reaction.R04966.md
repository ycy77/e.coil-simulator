---
entity_id: "reaction.R04966"
entity_type: "reaction"
name: "tetradecanoyl-[acp]:NAD+ trans-2-oxidoreductase"
source_database: "KEGG"
source_id: "R04966"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04966"
---

# tetradecanoyl-[acp]:NAD+ trans-2-oxidoreductase

`reaction.R04966`

## Static

- Type: `reaction`
- Source: `KEGG:R04966`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Tetradecanoyl-[acp] + NAD+ trans-Tetradec-2-enoyl-[acp] + NADH + H+

## Biological Role

Catalyzed by fabI (protein.P0AEK4). Substrates: NAD+ (molecule.C00003), Tetradecanoyl-[acp] (molecule.C05761). Products: NADH (molecule.C00004), H+ (molecule.C00080), trans-Tetradec-2-enoyl-[acp] (molecule.C05760).

## Annotation

Tetradecanoyl-[acp] + NAD+ <=> trans-Tetradec-2-enoyl-[acp] + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEK4|protein.P0AEK4]] `KEGG` `database` - via EC:1.3.1.9
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C05761 + C00003 <=> C05760 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C05761 + C00003 <=> C05760 + C00004 + C00080
- `is_product_of` <-- [[molecule.C05760|molecule.C05760]] `KEGG` `database` - C05761 + C00003 <=> C05760 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C05761 + C00003 <=> C05760 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C05761|molecule.C05761]] `KEGG` `database` - C05761 + C00003 <=> C05760 + C00004 + C00080

## External IDs

- `KEGG:R04966`

## Notes

EQUATION: C05761 + C00003 <=> C05760 + C00004 + C00080
