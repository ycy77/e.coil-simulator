---
entity_id: "reaction.R01155"
entity_type: "reaction"
name: "putrescine:2-oxoglutarate aminotransferase"
source_database: "KEGG"
source_id: "R01155"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01155"
---

# putrescine:2-oxoglutarate aminotransferase

`reaction.R01155`

## Static

- Type: `reaction`
- Source: `KEGG:R01155`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Putrescine + 2-Oxoglutarate 4-Aminobutyraldehyde + L-Glutamate

## Biological Role

Catalyzed by patA (protein.P42588). Substrates: 2-Oxoglutarate (molecule.C00026), Putrescine (molecule.C00134). Products: L-Glutamate (molecule.C00025), 4-Aminobutyraldehyde (molecule.C00555).

## Annotation

Putrescine + 2-Oxoglutarate <=> 4-Aminobutyraldehyde + L-Glutamate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P42588|protein.P42588]] `KEGG` `database` - via EC:2.6.1.82
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00134 + C00026 <=> C00555 + C00025
- `is_product_of` <-- [[molecule.C00555|molecule.C00555]] `KEGG` `database` - C00134 + C00026 <=> C00555 + C00025
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `KEGG` `database` - C00134 + C00026 <=> C00555 + C00025
- `is_substrate_of` <-- [[molecule.C00134|molecule.C00134]] `KEGG` `database` - C00134 + C00026 <=> C00555 + C00025

## External IDs

- `KEGG:R01155`

## Notes

EQUATION: C00134 + C00026 <=> C00555 + C00025
