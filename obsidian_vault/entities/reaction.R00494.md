---
entity_id: "reaction.R00494"
entity_type: "reaction"
name: "glutathione gamma-glutamylaminopeptidase"
source_database: "KEGG"
source_id: "R00494"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00494"
---

# glutathione gamma-glutamylaminopeptidase

`reaction.R00494`

## Static

- Type: `reaction`
- Source: `KEGG:R00494`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Glutathione + H2O Cys-Gly + L-Glutamate

## Biological Role

Catalyzed by ggt (protein.P18956). Substrates: H2O (molecule.C00001), Glutathione (molecule.C00051). Products: L-Glutamate (molecule.C00025), Cys-Gly (molecule.C01419).

## Annotation

Glutathione + H2O <=> Cys-Gly + L-Glutamate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P18956|protein.P18956]] `KEGG` `database` - via EC:3.4.19.13
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00051 + C00001 <=> C01419 + C00025
- `is_product_of` <-- [[molecule.C01419|molecule.C01419]] `KEGG` `database` - C00051 + C00001 <=> C01419 + C00025
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00051 + C00001 <=> C01419 + C00025
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `KEGG` `database` - C00051 + C00001 <=> C01419 + C00025

## External IDs

- `KEGG:R00494`

## Notes

EQUATION: C00051 + C00001 <=> C01419 + C00025
