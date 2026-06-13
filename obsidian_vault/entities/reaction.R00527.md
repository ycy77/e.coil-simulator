---
entity_id: "reaction.R00527"
entity_type: "reaction"
name: "S-formylglutathione hydrolase"
source_database: "KEGG"
source_id: "R00527"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00527"
---

# S-formylglutathione hydrolase

`reaction.R00527`

## Static

- Type: `reaction`
- Source: `KEGG:R00527`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-Formylglutathione + H2O Formate + Glutathione

## Biological Role

Catalyzed by yeiG (protein.P33018), frmB (protein.P51025). Substrates: H2O (molecule.C00001), S-Formylglutathione (molecule.C01031). Products: Glutathione (molecule.C00051), Formate (molecule.C00058).

## Annotation

S-Formylglutathione + H2O <=> Formate + Glutathione

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P33018|protein.P33018]] `KEGG` `database` - via EC:3.1.2.12
- `catalyzes` <-- [[protein.P51025|protein.P51025]] `KEGG` `database` - via EC:3.1.2.12
- `is_product_of` <-- [[molecule.C00051|molecule.C00051]] `KEGG` `database` - C01031 + C00001 <=> C00058 + C00051
- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `KEGG` `database` - C01031 + C00001 <=> C00058 + C00051
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01031 + C00001 <=> C00058 + C00051
- `is_substrate_of` <-- [[molecule.C01031|molecule.C01031]] `KEGG` `database` - C01031 + C00001 <=> C00058 + C00051

## External IDs

- `KEGG:R00527`

## Notes

EQUATION: C01031 + C00001 <=> C00058 + C00051
