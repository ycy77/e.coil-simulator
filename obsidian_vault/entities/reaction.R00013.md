---
entity_id: "reaction.R00013"
entity_type: "reaction"
name: "glyoxylate carboxy-lyase (dimerizing; tartronate-semialdehyde-forming)"
source_database: "KEGG"
source_id: "R00013"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00013"
---

# glyoxylate carboxy-lyase (dimerizing; tartronate-semialdehyde-forming)

`reaction.R00013`

## Static

- Type: `reaction`
- Source: `KEGG:R00013`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2 Glyoxylate 2-Hydroxy-3-oxopropanoate + CO2

## Biological Role

Catalyzed by gcl (protein.P0AEP7). Substrates: Glyoxylate (molecule.C00048). Products: CO2 (molecule.C00011), 2-Hydroxy-3-oxopropanoate (molecule.C01146).

## Annotation

2 Glyoxylate <=> 2-Hydroxy-3-oxopropanoate + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0AEP7|protein.P0AEP7]] `KEGG` `database` - via EC:4.1.1.47
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - 2 C00048 <=> C01146 + C00011
- `is_product_of` <-- [[molecule.C01146|molecule.C01146]] `KEGG` `database` - 2 C00048 <=> C01146 + C00011
- `is_substrate_of` <-- [[molecule.C00048|molecule.C00048]] `KEGG` `database` - 2 C00048 <=> C01146 + C00011

## External IDs

- `KEGG:R00013`

## Notes

EQUATION: 2 C00048 <=> C01146 + C00011
