---
entity_id: "reaction.R00460"
entity_type: "reaction"
name: "lysine racemase"
source_database: "KEGG"
source_id: "R00460"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00460"
---

# lysine racemase

`reaction.R00460`

## Static

- Type: `reaction`
- Source: `KEGG:R00460`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Lysine D-Lysine

## Biological Role

Catalyzed by ygeA (protein.P03813). Substrates: L-Lysine (molecule.C00047). Products: D-Lysine (molecule.C00739).

## Annotation

L-Lysine <=> D-Lysine

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P03813|protein.P03813]] `KEGG` `database` - via EC:5.1.1.10
- `is_product_of` <-- [[molecule.C00739|molecule.C00739]] `KEGG` `database` - C00047 <=> C00739
- `is_substrate_of` <-- [[molecule.C00047|molecule.C00047]] `KEGG` `database` - C00047 <=> C00739

## External IDs

- `KEGG:R00460`

## Notes

EQUATION: C00047 <=> C00739
