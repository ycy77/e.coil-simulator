---
entity_id: "reaction.R06927"
entity_type: "reaction"
name: "(2-naphthyl)methanol:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R06927"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R06927"
---

# (2-naphthyl)methanol:NAD+ oxidoreductase

`reaction.R06927`

## Static

- Type: `reaction`
- Source: `KEGG:R06927`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(2-Naphthyl)methanol + NAD+ 2-Naphthaldehyde + NADH + H+

## Biological Role

Catalyzed by adhE (protein.P0A9Q7), frmA (protein.P25437), yiaY (protein.P37686), adhP (protein.P39451). Substrates: NAD+ (molecule.C00003), (2-Naphthyl)methanol (molecule.C02909). Products: NADH (molecule.C00004), H+ (molecule.C00080), 2-Naphthaldehyde (molecule.C14099).

## Annotation

(2-Naphthyl)methanol + NAD+ <=> 2-Naphthaldehyde + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0A9Q7|protein.P0A9Q7]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` <-- [[protein.P25437|protein.P25437]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` <-- [[protein.P37686|protein.P37686]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` <-- [[protein.P39451|protein.P39451]] `KEGG` `database` - via EC:1.1.1.1
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C02909 + C00003 <=> C14099 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C02909 + C00003 <=> C14099 + C00004 + C00080
- `is_product_of` <-- [[molecule.C14099|molecule.C14099]] `KEGG` `database` - C02909 + C00003 <=> C14099 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C02909 + C00003 <=> C14099 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C02909|molecule.C02909]] `KEGG` `database` - C02909 + C00003 <=> C14099 + C00004 + C00080

## External IDs

- `KEGG:R06927`

## Notes

EQUATION: C02909 + C00003 <=> C14099 + C00004 + C00080
