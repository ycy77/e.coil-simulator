---
entity_id: "reaction.R00274"
entity_type: "reaction"
name: "glutathione:hydrogen-peroxide oxidoreductase"
source_database: "KEGG"
source_id: "R00274"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00274"
---

# glutathione:hydrogen-peroxide oxidoreductase

`reaction.R00274`

## Static

- Type: `reaction`
- Source: `KEGG:R00274`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Hydrogen peroxide + 2 Glutathione Glutathione disulfide + 2 H2O

## Biological Role

Catalyzed by btuE (protein.P06610). Substrates: Hydrogen peroxide (molecule.C00027), Glutathione (molecule.C00051). Products: H2O (molecule.C00001), Glutathione disulfide (molecule.C00127).

## Annotation

Hydrogen peroxide + 2 Glutathione <=> Glutathione disulfide + 2 H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P06610|protein.P06610]] `KEGG` `database` - via EC:1.11.1.9
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00027 + 2 C00051 <=> C00127 + 2 C00001
- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `KEGG` `database` - C00027 + 2 C00051 <=> C00127 + 2 C00001
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `KEGG` `database` - C00027 + 2 C00051 <=> C00127 + 2 C00001
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `KEGG` `database` - C00027 + 2 C00051 <=> C00127 + 2 C00001

## External IDs

- `KEGG:R00274`

## Notes

EQUATION: C00027 + 2 C00051 <=> C00127 + 2 C00001
