---
entity_id: "reaction.R00505"
entity_type: "reaction"
name: "UDP-alpha-D-galactopyranose furanomutase"
source_database: "KEGG"
source_id: "R00505"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00505"
---

# UDP-alpha-D-galactopyranose furanomutase

`reaction.R00505`

## Static

- Type: `reaction`
- Source: `KEGG:R00505`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-alpha-D-galactose UDP-alpha-D-galactofuranose

## Biological Role

Catalyzed by glf (protein.P37747). Substrates: UDP-alpha-D-galactose (molecule.C00052). Products: UDP-alpha-D-galactofuranose (molecule.C03733).

## Annotation

UDP-alpha-D-galactose <=> UDP-alpha-D-galactofuranose

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P37747|protein.P37747]] `KEGG` `database` - via EC:5.4.99.9
- `is_product_of` <-- [[molecule.C03733|molecule.C03733]] `KEGG` `database` - C00052 <=> C03733
- `is_substrate_of` <-- [[molecule.C00052|molecule.C00052]] `KEGG` `database` - C00052 <=> C03733

## External IDs

- `KEGG:R00505`

## Notes

EQUATION: C00052 <=> C03733
