---
entity_id: "reaction.R00519"
entity_type: "reaction"
name: "formate:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R00519"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00519"
---

# formate:NAD+ oxidoreductase

`reaction.R00519`

## Static

- Type: `reaction`
- Source: `KEGG:R00519`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Formate + NAD+ H+ + CO2 + NADH

## Biological Role

Catalyzed by fdoG (protein.P32176). Substrates: NAD+ (molecule.C00003), Formate (molecule.C00058). Products: NADH (molecule.C00004), CO2 (molecule.C00011), H+ (molecule.C00080).

## Annotation

Formate + NAD+ <=> H+ + CO2 + NADH

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P32176|protein.P32176]] `KEGG` `database` - via EC:1.17.1.9
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00058 + C00003 <=> C00080 + C00011 + C00004
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00058 + C00003 <=> C00080 + C00011 + C00004
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00058 + C00003 <=> C00080 + C00011 + C00004
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00058 + C00003 <=> C00080 + C00011 + C00004
- `is_substrate_of` <-- [[molecule.C00058|molecule.C00058]] `KEGG` `database` - C00058 + C00003 <=> C00080 + C00011 + C00004

## External IDs

- `KEGG:R00519`

## Notes

EQUATION: C00058 + C00003 <=> C00080 + C00011 + C00004
