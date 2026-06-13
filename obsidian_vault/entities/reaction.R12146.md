---
entity_id: "reaction.R12146"
entity_type: "reaction"
name: "L-galactonate:NAD+ 5-oxidoreductase"
source_database: "KEGG"
source_id: "R12146"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12146"
---

# L-galactonate:NAD+ 5-oxidoreductase

`reaction.R12146`

## Static

- Type: `reaction`
- Source: `KEGG:R12146`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Galactonate + NAD+ D-Tagaturonate + NADH + H+

## Biological Role

Catalyzed by lgoD (protein.P39400). Substrates: NAD+ (molecule.C00003), L-Galactonate (molecule.C15930). Products: NADH (molecule.C00004), H+ (molecule.C00080), D-Tagaturonate (molecule.C00558).

## Annotation

L-Galactonate + NAD+ <=> D-Tagaturonate + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P39400|protein.P39400]] `KEGG` `database` - via EC:1.1.1.414
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C15930 + C00003 <=> C00558 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C15930 + C00003 <=> C00558 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00558|molecule.C00558]] `KEGG` `database` - C15930 + C00003 <=> C00558 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C15930 + C00003 <=> C00558 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C15930|molecule.C15930]] `KEGG` `database` - C15930 + C00003 <=> C00558 + C00004 + C00080

## External IDs

- `KEGG:R12146`

## Notes

EQUATION: C15930 + C00003 <=> C00558 + C00004 + C00080
