---
entity_id: "reaction.R00549"
entity_type: "reaction"
name: "ATP:riboflavin 5'-phosphotransferase"
source_database: "KEGG"
source_id: "R00549"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00549"
---

# ATP:riboflavin 5'-phosphotransferase

`reaction.R00549`

## Static

- Type: `reaction`
- Source: `KEGG:R00549`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Riboflavin ADP + FMN

## Biological Role

Catalyzed by ribF (protein.P0AG40). Substrates: ATP (molecule.C00002), Riboflavin (molecule.C00255). Products: ADP (molecule.C00008), FMN (molecule.C00061).

## Annotation

ATP + Riboflavin <=> ADP + FMN

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AG40|protein.P0AG40]] `KEGG` `database` - via EC:2.7.1.26
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00255 <=> C00008 + C00061
- `is_product_of` <-- [[molecule.C00061|molecule.C00061]] `KEGG` `database` - C00002 + C00255 <=> C00008 + C00061
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00255 <=> C00008 + C00061
- `is_substrate_of` <-- [[molecule.C00255|molecule.C00255]] `KEGG` `database` - C00002 + C00255 <=> C00008 + C00061

## External IDs

- `KEGG:R00549`

## Notes

EQUATION: C00002 + C00255 <=> C00008 + C00061
