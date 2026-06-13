---
entity_id: "reaction.R01016"
entity_type: "reaction"
name: "glycerone-phosphate phosphate-lyase (methylglyoxal-forming)"
source_database: "KEGG"
source_id: "R01016"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01016"
---

# glycerone-phosphate phosphate-lyase (methylglyoxal-forming)

`reaction.R01016`

## Static

- Type: `reaction`
- Source: `KEGG:R01016`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Glycerone phosphate Methylglyoxal + Orthophosphate

## Biological Role

Catalyzed by mgsA (protein.P0A731). Substrates: Glycerone phosphate (molecule.C00111). Products: Orthophosphate (molecule.C00009), Methylglyoxal (molecule.C00546).

## Annotation

Glycerone phosphate <=> Methylglyoxal + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A731|protein.P0A731]] `KEGG` `database` - via EC:4.2.3.3
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00111 <=> C00546 + C00009
- `is_product_of` <-- [[molecule.C00546|molecule.C00546]] `KEGG` `database` - C00111 <=> C00546 + C00009
- `is_substrate_of` <-- [[molecule.C00111|molecule.C00111]] `KEGG` `database` - C00111 <=> C00546 + C00009

## External IDs

- `KEGG:R01016`

## Notes

EQUATION: C00111 <=> C00546 + C00009
