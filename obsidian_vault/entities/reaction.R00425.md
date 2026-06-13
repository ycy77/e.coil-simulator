---
entity_id: "reaction.R00425"
entity_type: "reaction"
name: "GTP 7,8-8,9-dihydrolase (diphosphate-forming)"
source_database: "KEGG"
source_id: "R00425"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00425"
---

# GTP 7,8-8,9-dihydrolase (diphosphate-forming)

`reaction.R00425`

## Static

- Type: `reaction`
- Source: `KEGG:R00425`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GTP + 4 H2O Formate + 2,5-Diamino-6-(5-phospho-D-ribosylamino)pyrimidin-4(3H)-one + 2 Orthophosphate

## Biological Role

Catalyzed by ribA (protein.P0A7I7). Substrates: H2O (molecule.C00001), GTP (molecule.C00044). Products: Orthophosphate (molecule.C00009), Formate (molecule.C00058), 2,5-Diamino-6-(5-phospho-D-ribosylamino)pyrimidin-4(3H)-one (molecule.C01304).

## Annotation

GTP + 4 H2O <=> Formate + 2,5-Diamino-6-(5-phospho-D-ribosylamino)pyrimidin-4(3H)-one + 2 Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A7I7|protein.P0A7I7]] `KEGG` `database` - via EC:3.5.4.25
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00044 + 4 C00001 <=> C00058 + C01304 + 2 C00009
- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `KEGG` `database` - C00044 + 4 C00001 <=> C00058 + C01304 + 2 C00009
- `is_product_of` <-- [[molecule.C01304|molecule.C01304]] `KEGG` `database` - C00044 + 4 C00001 <=> C00058 + C01304 + 2 C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00044 + 4 C00001 <=> C00058 + C01304 + 2 C00009
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `KEGG` `database` - C00044 + 4 C00001 <=> C00058 + C01304 + 2 C00009

## External IDs

- `KEGG:R00425`

## Notes

EQUATION: C00044 + 4 C00001 <=> C00058 + C01304 + 2 C00009
