---
entity_id: "reaction.R01737"
entity_type: "reaction"
name: "ATP:D-gluconate 6-phosphotransferase"
source_database: "KEGG"
source_id: "R01737"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01737"
---

# ATP:D-gluconate 6-phosphotransferase

`reaction.R01737`

## Static

- Type: `reaction`
- Source: `KEGG:R01737`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + D-Gluconic acid ADP + 6-Phospho-D-gluconate

## Biological Role

Catalyzed by idnK (protein.P39208), gntK (protein.P46859). Substrates: ATP (molecule.C00002), D-Gluconic acid (molecule.C00257). Products: ADP (molecule.C00008), 6-Phospho-D-gluconate (molecule.C00345).

## Annotation

ATP + D-Gluconic acid <=> ADP + 6-Phospho-D-gluconate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P39208|protein.P39208]] `KEGG` `database` - via EC:2.7.1.12
- `catalyzes` <-- [[protein.P46859|protein.P46859]] `KEGG` `database` - via EC:2.7.1.12
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00257 <=> C00008 + C00345
- `is_product_of` <-- [[molecule.C00345|molecule.C00345]] `KEGG` `database` - C00002 + C00257 <=> C00008 + C00345
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00257 <=> C00008 + C00345
- `is_substrate_of` <-- [[molecule.C00257|molecule.C00257]] `KEGG` `database` - C00002 + C00257 <=> C00008 + C00345

## External IDs

- `KEGG:R01737`

## Notes

EQUATION: C00002 + C00257 <=> C00008 + C00345
