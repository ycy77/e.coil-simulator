---
entity_id: "reaction.R00409"
entity_type: "reaction"
name: "(2S,3R)-3-hydroxybutane-1,2,3-tricarboxylate pyruvate-lyase (succinate-forming)"
source_database: "KEGG"
source_id: "R00409"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00409"
---

# (2S,3R)-3-hydroxybutane-1,2,3-tricarboxylate pyruvate-lyase (succinate-forming)

`reaction.R00409`

## Static

- Type: `reaction`
- Source: `KEGG:R00409`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(2S,3R)-3-Hydroxybutane-1,2,3-tricarboxylate Pyruvate + Succinate

## Biological Role

Catalyzed by aceA (protein.P0A9G6), prpB (protein.P77541). Substrates: (2S,3R)-3-Hydroxybutane-1,2,3-tricarboxylate (molecule.C04593). Products: Pyruvate (molecule.C00022), Succinate (molecule.C00042).

## Annotation

(2S,3R)-3-Hydroxybutane-1,2,3-tricarboxylate <=> Pyruvate + Succinate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A9G6|protein.P0A9G6]] `KEGG` `database` - via EC:4.1.3.30
- `catalyzes` <-- [[protein.P77541|protein.P77541]] `KEGG` `database` - via EC:4.1.3.30
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C04593 <=> C00022 + C00042
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `KEGG` `database` - C04593 <=> C00022 + C00042
- `is_substrate_of` <-- [[molecule.C04593|molecule.C04593]] `KEGG` `database` - C04593 <=> C00022 + C00042

## External IDs

- `KEGG:R00409`

## Notes

EQUATION: C04593 <=> C00022 + C00042
