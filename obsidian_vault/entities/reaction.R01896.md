---
entity_id: "reaction.R01896"
entity_type: "reaction"
name: "xylitol:NAD+ 2-oxidoreductase (D-xylulose-forming)"
source_database: "KEGG"
source_id: "R01896"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01896"
---

# xylitol:NAD+ 2-oxidoreductase (D-xylulose-forming)

`reaction.R01896`

## Static

- Type: `reaction`
- Source: `KEGG:R01896`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Xylitol + NAD+ D-Xylulose + NADH + H+

## Biological Role

Catalyzed by ydjJ (protein.P77280). Substrates: NAD+ (molecule.C00003), Xylitol (molecule.C00379). Products: NADH (molecule.C00004), H+ (molecule.C00080), D-Xylulose (molecule.C00310).

## Annotation

Xylitol + NAD+ <=> D-Xylulose + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P77280|protein.P77280]] `KEGG` `database` - via EC:1.1.1.14
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00379 + C00003 <=> C00310 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00379 + C00003 <=> C00310 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00310|molecule.C00310]] `KEGG` `database` - C00379 + C00003 <=> C00310 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00379 + C00003 <=> C00310 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00379|molecule.C00379]] `KEGG` `database` - C00379 + C00003 <=> C00310 + C00004 + C00080

## External IDs

- `KEGG:R01896`

## Notes

EQUATION: C00379 + C00003 <=> C00310 + C00004 + C00080
