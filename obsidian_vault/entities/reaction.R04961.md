---
entity_id: "reaction.R04961"
entity_type: "reaction"
name: "decanoyl-[acp]:NAD+ trans-2-oxidoreductase"
source_database: "KEGG"
source_id: "R04961"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04961"
---

# decanoyl-[acp]:NAD+ trans-2-oxidoreductase

`reaction.R04961`

## Static

- Type: `reaction`
- Source: `KEGG:R04961`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Decanoyl-[acp] + NAD+ trans-Dec-2-enoyl-[acp] + NADH + H+

## Biological Role

Catalyzed by fabI (protein.P0AEK4). Substrates: NAD+ (molecule.C00003), Decanoyl-[acp] (molecule.C05755). Products: NADH (molecule.C00004), H+ (molecule.C00080), trans-Dec-2-enoyl-[acp] (molecule.C05754).

## Annotation

Decanoyl-[acp] + NAD+ <=> trans-Dec-2-enoyl-[acp] + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEK4|protein.P0AEK4]] `KEGG` `database` - via EC:1.3.1.9
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C05755 + C00003 <=> C05754 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C05755 + C00003 <=> C05754 + C00004 + C00080
- `is_product_of` <-- [[molecule.C05754|molecule.C05754]] `KEGG` `database` - C05755 + C00003 <=> C05754 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C05755 + C00003 <=> C05754 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C05755|molecule.C05755]] `KEGG` `database` - C05755 + C00003 <=> C05754 + C00004 + C00080

## External IDs

- `KEGG:R04961`

## Notes

EQUATION: C05755 + C00003 <=> C05754 + C00004 + C00080
