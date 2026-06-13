---
entity_id: "reaction.R00268"
entity_type: "reaction"
name: "oxalosuccinate carboxy-lyase (2-oxoglutarate-forming)"
source_database: "KEGG"
source_id: "R00268"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00268"
---

# oxalosuccinate carboxy-lyase (2-oxoglutarate-forming)

`reaction.R00268`

## Static

- Type: `reaction`
- Source: `KEGG:R00268`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Oxalosuccinate 2-Oxoglutarate + CO2

## Biological Role

Catalyzed by icd (protein.P08200). Substrates: Oxalosuccinate (molecule.C05379). Products: CO2 (molecule.C00011), 2-Oxoglutarate (molecule.C00026).

## Annotation

Oxalosuccinate <=> 2-Oxoglutarate + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P08200|protein.P08200]] `KEGG` `database` - via EC:1.1.1.42
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C05379 <=> C00026 + C00011
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `KEGG` `database` - C05379 <=> C00026 + C00011
- `is_substrate_of` <-- [[molecule.C05379|molecule.C05379]] `KEGG` `database` - C05379 <=> C00026 + C00011

## External IDs

- `KEGG:R00268`

## Notes

EQUATION: C05379 <=> C00026 + C00011
