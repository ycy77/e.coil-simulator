---
entity_id: "reaction.R02619"
entity_type: "reaction"
name: "3-sulfino-L-alanine:2-oxoglutarate aminotransferase"
source_database: "KEGG"
source_id: "R02619"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02619"
---

# 3-sulfino-L-alanine:2-oxoglutarate aminotransferase

`reaction.R02619`

## Static

- Type: `reaction`
- Source: `KEGG:R02619`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-Sulfino-L-alanine + 2-Oxoglutarate 3-Sulfinylpyruvate + L-Glutamate

## Biological Role

Catalyzed by aspC (protein.P00509). Substrates: 2-Oxoglutarate (molecule.C00026), 3-Sulfino-L-alanine (molecule.C00606). Products: L-Glutamate (molecule.C00025), 3-Sulfinylpyruvate (molecule.C05527).

## Annotation

3-Sulfino-L-alanine + 2-Oxoglutarate <=> 3-Sulfinylpyruvate + L-Glutamate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P00509|protein.P00509]] `KEGG` `database` - via EC:2.6.1.1
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00606 + C00026 <=> C05527 + C00025
- `is_product_of` <-- [[molecule.C05527|molecule.C05527]] `KEGG` `database` - C00606 + C00026 <=> C05527 + C00025
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `KEGG` `database` - C00606 + C00026 <=> C05527 + C00025
- `is_substrate_of` <-- [[molecule.C00606|molecule.C00606]] `KEGG` `database` - C00606 + C00026 <=> C05527 + C00025

## External IDs

- `KEGG:R02619`

## Notes

EQUATION: C00606 + C00026 <=> C05527 + C00025
