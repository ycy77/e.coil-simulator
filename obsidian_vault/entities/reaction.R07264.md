---
entity_id: "reaction.R07264"
entity_type: "reaction"
name: "2-alpha-D-glucosyl-D-glucose:phosphate beta-D-glucosyltransferase"
source_database: "KEGG"
source_id: "R07264"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07264"
---

# 2-alpha-D-glucosyl-D-glucose:phosphate beta-D-glucosyltransferase

`reaction.R07264`

## Static

- Type: `reaction`
- Source: `KEGG:R07264`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-alpha-D-Glucosyl-D-glucose + Orthophosphate D-Glucose + beta-D-Glucose 1-phosphate

## Biological Role

Catalyzed by ycjT (protein.P77154). Substrates: Orthophosphate (molecule.C00009). Products: D-Glucose (molecule.C00031), beta-D-Glucose 1-phosphate (molecule.C00663).

## Annotation

2-alpha-D-Glucosyl-D-glucose + Orthophosphate <=> D-Glucose + beta-D-Glucose 1-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P77154|protein.P77154]] `KEGG` `database` - via EC:2.4.1.230
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `KEGG` `database` - C15548 + C00009 <=> C00031 + C00663
- `is_product_of` <-- [[molecule.C00663|molecule.C00663]] `KEGG` `database` - C15548 + C00009 <=> C00031 + C00663
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C15548 + C00009 <=> C00031 + C00663

## External IDs

- `KEGG:R07264`

## Notes

EQUATION: C15548 + C00009 <=> C00031 + C00663
