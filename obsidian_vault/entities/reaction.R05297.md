---
entity_id: "reaction.R05297"
entity_type: "reaction"
name: "R05297"
source_database: "KEGG"
source_id: "R05297"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05297"
---

# R05297

`reaction.R05297`

## Static

- Type: `reaction`
- Source: `KEGG:R05297`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(4E)-2-Oxohexenoic acid + H2O 4-Hydroxy-2-oxohexanoic acid

## Biological Role

Catalyzed by mhpD (protein.P77608). Substrates: H2O (molecule.C00001). Products: 4-Hydroxy-2-oxohexanoic acid (molecule.C06762).

## Annotation

(4E)-2-Oxohexenoic acid + H2O <=> 4-Hydroxy-2-oxohexanoic acid

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P77608|protein.P77608]] `KEGG` `database` - via EC:4.2.1.80
- `is_product_of` <-- [[molecule.C06762|molecule.C06762]] `KEGG` `database` - C06761 + C00001 <=> C06762
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C06761 + C00001 <=> C06762

## External IDs

- `KEGG:R05297`

## Notes

EQUATION: C06761 + C00001 <=> C06762
