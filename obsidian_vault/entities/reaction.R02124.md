---
entity_id: "reaction.R02124"
entity_type: "reaction"
name: "retinol:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R02124"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02124"
---

# retinol:NAD+ oxidoreductase

`reaction.R02124`

## Static

- Type: `reaction`
- Source: `KEGG:R02124`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Retinol + NAD+ Retinal + NADH + H+

## Biological Role

Catalyzed by adhE (protein.P0A9Q7), frmA (protein.P25437), yiaY (protein.P37686), adhP (protein.P39451). Substrates: NAD+ (molecule.C00003). Products: NADH (molecule.C00004), H+ (molecule.C00080).

## Annotation

Retinol + NAD+ <=> Retinal + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A9Q7|protein.P0A9Q7]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` <-- [[protein.P25437|protein.P25437]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` <-- [[protein.P37686|protein.P37686]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` <-- [[protein.P39451|protein.P39451]] `KEGG` `database` - via EC:1.1.1.1
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00473 + C00003 <=> C00376 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00473 + C00003 <=> C00376 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00473 + C00003 <=> C00376 + C00004 + C00080

## External IDs

- `KEGG:R02124`

## Notes

EQUATION: C00473 + C00003 <=> C00376 + C00004 + C00080
