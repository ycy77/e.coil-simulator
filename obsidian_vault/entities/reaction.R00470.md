---
entity_id: "reaction.R00470"
entity_type: "reaction"
name: "4-hydroxy-2-oxoglutarate glyoxylate-lyase (pyruvate-forming)"
source_database: "KEGG"
source_id: "R00470"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00470"
---

# 4-hydroxy-2-oxoglutarate glyoxylate-lyase (pyruvate-forming)

`reaction.R00470`

## Static

- Type: `reaction`
- Source: `KEGG:R00470`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

4-Hydroxy-2-oxoglutarate Pyruvate + Glyoxylate

## Biological Role

Catalyzed by eda (protein.P0A955). Substrates: 4-Hydroxy-2-oxoglutarate (molecule.C01127). Products: Pyruvate (molecule.C00022), Glyoxylate (molecule.C00048).

## Annotation

4-Hydroxy-2-oxoglutarate <=> Pyruvate + Glyoxylate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A955|protein.P0A955]] `KEGG` `database` - via EC:4.1.3.42
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C01127 <=> C00022 + C00048
- `is_product_of` <-- [[molecule.C00048|molecule.C00048]] `KEGG` `database` - C01127 <=> C00022 + C00048
- `is_substrate_of` <-- [[molecule.C01127|molecule.C01127]] `KEGG` `database` - C01127 <=> C00022 + C00048

## External IDs

- `KEGG:R00470`

## Notes

EQUATION: C01127 <=> C00022 + C00048
