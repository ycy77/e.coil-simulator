---
entity_id: "reaction.R00335"
entity_type: "reaction"
name: "GTP phosphohydrolase"
source_database: "KEGG"
source_id: "R00335"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00335"
---

# GTP phosphohydrolase

`reaction.R00335`

## Static

- Type: `reaction`
- Source: `KEGG:R00335`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GTP + H2O GDP + Orthophosphate

## Biological Role

Catalyzed by ffh (protein.P0AGD7). Substrates: H2O (molecule.C00001), GTP (molecule.C00044). Products: Orthophosphate (molecule.C00009), GDP (molecule.C00035).

## Annotation

GTP + H2O <=> GDP + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AGD7|protein.P0AGD7]] `KEGG` `database` - via EC:3.6.5.4
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00044 + C00001 <=> C00035 + C00009
- `is_product_of` <-- [[molecule.C00035|molecule.C00035]] `KEGG` `database` - C00044 + C00001 <=> C00035 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00044 + C00001 <=> C00035 + C00009
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `KEGG` `database` - C00044 + C00001 <=> C00035 + C00009

## External IDs

- `KEGG:R00335`

## Notes

EQUATION: C00044 + C00001 <=> C00035 + C00009
