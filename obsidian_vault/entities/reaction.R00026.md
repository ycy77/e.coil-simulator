---
entity_id: "reaction.R00026"
entity_type: "reaction"
name: "cellobiose glucohydrolase"
source_database: "KEGG"
source_id: "R00026"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00026"
---

# cellobiose glucohydrolase

`reaction.R00026`

## Static

- Type: `reaction`
- Source: `KEGG:R00026`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Cellobiose + H2O 2 beta-D-Glucose

## Biological Role

Catalyzed by bglX (protein.P33363). Substrates: H2O (molecule.C00001), Cellobiose (molecule.C00185). Products: beta-D-Glucose (molecule.C00221).

## Annotation

Cellobiose + H2O <=> 2 beta-D-Glucose

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P33363|protein.P33363]] `KEGG` `database` - via EC:3.2.1.21
- `is_product_of` <-- [[molecule.C00221|molecule.C00221]] `KEGG` `database` - C00185 + C00001 <=> 2 C00221
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00185 + C00001 <=> 2 C00221
- `is_substrate_of` <-- [[molecule.C00185|molecule.C00185]] `KEGG` `database` - C00185 + C00001 <=> 2 C00221

## External IDs

- `KEGG:R00026`

## Notes

EQUATION: C00185 + C00001 <=> 2 C00221
