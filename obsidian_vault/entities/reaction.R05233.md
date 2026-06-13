---
entity_id: "reaction.R05233"
entity_type: "reaction"
name: "trans-3-chloro-2-propene-1-ol:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R05233"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05233"
---

# trans-3-chloro-2-propene-1-ol:NAD+ oxidoreductase

`reaction.R05233`

## Static

- Type: `reaction`
- Source: `KEGG:R05233`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

trans-3-Chloro-2-propene-1-ol + NAD+ trans-3-Chloroallyl aldehyde + NADH + H+

## Biological Role

Catalyzed by adhE (protein.P0A9Q7), frmA (protein.P25437), yiaY (protein.P37686), adhP (protein.P39451). Substrates: NAD+ (molecule.C00003), trans-3-Chloro-2-propene-1-ol (molecule.C06611). Products: NADH (molecule.C00004), H+ (molecule.C00080), trans-3-Chloroallyl aldehyde (molecule.C06613).

## Annotation

trans-3-Chloro-2-propene-1-ol + NAD+ <=> trans-3-Chloroallyl aldehyde + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0A9Q7|protein.P0A9Q7]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` <-- [[protein.P25437|protein.P25437]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` <-- [[protein.P37686|protein.P37686]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` <-- [[protein.P39451|protein.P39451]] `KEGG` `database` - via EC:1.1.1.1
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C06611 + C00003 <=> C06613 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C06611 + C00003 <=> C06613 + C00004 + C00080
- `is_product_of` <-- [[molecule.C06613|molecule.C06613]] `KEGG` `database` - C06611 + C00003 <=> C06613 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C06611 + C00003 <=> C06613 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C06611|molecule.C06611]] `KEGG` `database` - C06611 + C00003 <=> C06613 + C00004 + C00080

## External IDs

- `KEGG:R05233`

## Notes

EQUATION: C06611 + C00003 <=> C06613 + C00004 + C00080
