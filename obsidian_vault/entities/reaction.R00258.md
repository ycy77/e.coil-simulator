---
entity_id: "reaction.R00258"
entity_type: "reaction"
name: "L-alanine:2-oxoglutarate aminotransferase"
source_database: "KEGG"
source_id: "R00258"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00258"
---

# L-alanine:2-oxoglutarate aminotransferase

`reaction.R00258`

## Static

- Type: `reaction`
- Source: `KEGG:R00258`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Alanine + 2-Oxoglutarate Pyruvate + L-Glutamate

## Biological Role

Catalyzed by alaA (protein.P0A959). Substrates: 2-Oxoglutarate (molecule.C00026), L-Alanine (molecule.C00041). Products: Pyruvate (molecule.C00022), L-Glutamate (molecule.C00025).

## Annotation

L-Alanine + 2-Oxoglutarate <=> Pyruvate + L-Glutamate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A959|protein.P0A959]] `KEGG` `database` - via EC:2.6.1.2
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00041 + C00026 <=> C00022 + C00025
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00041 + C00026 <=> C00022 + C00025
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `KEGG` `database` - C00041 + C00026 <=> C00022 + C00025
- `is_substrate_of` <-- [[molecule.C00041|molecule.C00041]] `KEGG` `database` - C00041 + C00026 <=> C00022 + C00025

## External IDs

- `KEGG:R00258`

## Notes

EQUATION: C00041 + C00026 <=> C00022 + C00025
