---
entity_id: "reaction.R00623"
entity_type: "reaction"
name: "primary_alcohol:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R00623"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00623"
---

# primary_alcohol:NAD+ oxidoreductase

`reaction.R00623`

## Static

- Type: `reaction`
- Source: `KEGG:R00623`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Primary alcohol + NAD+ Aldehyde + NADH + H+

## Biological Role

Catalyzed by adhE (protein.P0A9Q7), frmA (protein.P25437), yiaY (protein.P37686), adhP (protein.P39451). Substrates: NAD+ (molecule.C00003), Primary alcohol (molecule.C00226). Products: NADH (molecule.C00004), Aldehyde (molecule.C00071), H+ (molecule.C00080).

## Annotation

Primary alcohol + NAD+ <=> Aldehyde + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0A9Q7|protein.P0A9Q7]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` <-- [[protein.P25437|protein.P25437]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` <-- [[protein.P37686|protein.P37686]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` <-- [[protein.P39451|protein.P39451]] `KEGG` `database` - via EC:1.1.1.1
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00226 + C00003 <=> C00071 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00071|molecule.C00071]] `KEGG` `database` - C00226 + C00003 <=> C00071 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00226 + C00003 <=> C00071 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00226 + C00003 <=> C00071 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00226|molecule.C00226]] `KEGG` `database` - C00226 + C00003 <=> C00071 + C00004 + C00080

## External IDs

- `KEGG:R00623`

## Notes

EQUATION: C00226 + C00003 <=> C00071 + C00004 + C00080
