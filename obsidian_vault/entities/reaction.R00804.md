---
entity_id: "reaction.R00804"
entity_type: "reaction"
name: "sugar-phosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R00804"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00804"
---

# sugar-phosphate phosphohydrolase

`reaction.R00804`

## Static

- Type: `reaction`
- Source: `KEGG:R00804`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Sugar phosphate + H2O Sugar + Orthophosphate

## Biological Role

Catalyzed by yigL (protein.P27848), ybiV (protein.P75792), hxpB (protein.P77247), hxpA (protein.P77625). Substrates: H2O (molecule.C00001). Products: Orthophosphate (molecule.C00009).

## Annotation

Sugar phosphate + H2O <=> Sugar + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P27848|protein.P27848]] `KEGG` `database` - via EC:3.1.3.23
- `catalyzes` <-- [[protein.P75792|protein.P75792]] `KEGG` `database` - via EC:3.1.3.23
- `catalyzes` <-- [[protein.P77247|protein.P77247]] `KEGG` `database` - via EC:3.1.3.23
- `catalyzes` <-- [[protein.P77625|protein.P77625]] `KEGG` `database` - via EC:3.1.3.23
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00934 + C00001 <=> C11477 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00934 + C00001 <=> C11477 + C00009

## External IDs

- `KEGG:R00804`

## Notes

EQUATION: C00934 + C00001 <=> C11477 + C00009
