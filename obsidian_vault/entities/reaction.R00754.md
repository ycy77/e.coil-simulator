---
entity_id: "reaction.R00754"
entity_type: "reaction"
name: "ethanol:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R00754"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00754"
---

# ethanol:NAD+ oxidoreductase

`reaction.R00754`

## Static

- Type: `reaction`
- Source: `KEGG:R00754`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Ethanol + NAD+ Acetaldehyde + NADH + H+

## Biological Role

Catalyzed by adhE (protein.P0A9Q7), frmA (protein.P25437), yiaY (protein.P37686), adhP (protein.P39451). Substrates: NAD+ (molecule.C00003), Ethanol (molecule.C00469). Products: NADH (molecule.C00004), H+ (molecule.C00080), Acetaldehyde (molecule.C00084).

## Annotation

Ethanol + NAD+ <=> Acetaldehyde + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0A9Q7|protein.P0A9Q7]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` <-- [[protein.P25437|protein.P25437]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` <-- [[protein.P37686|protein.P37686]] `KEGG` `database` - via EC:1.1.1.1
- `catalyzes` <-- [[protein.P39451|protein.P39451]] `KEGG` `database` - via EC:1.1.1.1
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00469 + C00003 <=> C00084 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00469 + C00003 <=> C00084 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00084|molecule.C00084]] `KEGG` `database` - C00469 + C00003 <=> C00084 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00469 + C00003 <=> C00084 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00469|molecule.C00469]] `KEGG` `database` - C00469 + C00003 <=> C00084 + C00004 + C00080

## External IDs

- `KEGG:R00754`

## Notes

EQUATION: C00469 + C00003 <=> C00084 + C00004 + C00080
