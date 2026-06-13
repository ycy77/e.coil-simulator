---
entity_id: "reaction.R02135"
entity_type: "reaction"
name: "thiamin monophosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R02135"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02135"
---

# thiamin monophosphate phosphohydrolase

`reaction.R02135`

## Static

- Type: `reaction`
- Source: `KEGG:R02135`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Thiamin monophosphate + H2O Thiamine + Orthophosphate

## Biological Role

Catalyzed by phoA (protein.P00634), appA (protein.P07102), aphA (protein.P0AE22), rsgA (protein.P39286). Substrates: H2O (molecule.C00001), Thiamin monophosphate (molecule.C01081). Products: Orthophosphate (molecule.C00009), Thiamine (molecule.C00378).

## Annotation

Thiamin monophosphate + H2O <=> Thiamine + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P00634|protein.P00634]] `KEGG` `database` - via EC:3.1.3.1
- `catalyzes` <-- [[protein.P07102|protein.P07102]] `KEGG` `database` - via EC:3.1.3.2
- `catalyzes` <-- [[protein.P0AE22|protein.P0AE22]] `KEGG` `database` - via EC:3.1.3.2
- `catalyzes` <-- [[protein.P39286|protein.P39286]] `KEGG` `database` - via EC:3.1.3.100
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C01081 + C00001 <=> C00378 + C00009
- `is_product_of` <-- [[molecule.C00378|molecule.C00378]] `KEGG` `database` - C01081 + C00001 <=> C00378 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01081 + C00001 <=> C00378 + C00009
- `is_substrate_of` <-- [[molecule.C01081|molecule.C01081]] `KEGG` `database` - C01081 + C00001 <=> C00378 + C00009

## External IDs

- `KEGG:R02135`

## Notes

EQUATION: C01081 + C00001 <=> C00378 + C00009
