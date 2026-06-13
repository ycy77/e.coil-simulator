---
entity_id: "reaction.R00278"
entity_type: "reaction"
name: "pyridoxine 5'-phosphate:oxygen oxidoreductase"
source_database: "KEGG"
source_id: "R00278"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00278"
---

# pyridoxine 5'-phosphate:oxygen oxidoreductase

`reaction.R00278`

## Static

- Type: `reaction`
- Source: `KEGG:R00278`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Pyridoxine phosphate + Oxygen Hydrogen peroxide + Pyridoxal phosphate

## Biological Role

Catalyzed by pdxH (protein.P0AFI7). Substrates: Oxygen (molecule.C00007), Pyridoxine phosphate (molecule.C00627). Products: Pyridoxal phosphate (molecule.C00018), Hydrogen peroxide (molecule.C00027).

## Annotation

Pyridoxine phosphate + Oxygen <=> Hydrogen peroxide + Pyridoxal phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AFI7|protein.P0AFI7]] `KEGG` `database` - via EC:1.4.3.5
- `is_product_of` <-- [[molecule.C00018|molecule.C00018]] `KEGG` `database` - C00627 + C00007 <=> C00027 + C00018
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `KEGG` `database` - C00627 + C00007 <=> C00027 + C00018
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - C00627 + C00007 <=> C00027 + C00018
- `is_substrate_of` <-- [[molecule.C00627|molecule.C00627]] `KEGG` `database` - C00627 + C00007 <=> C00027 + C00018

## External IDs

- `KEGG:R00278`

## Notes

EQUATION: C00627 + C00007 <=> C00027 + C00018
