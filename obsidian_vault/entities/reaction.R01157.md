---
entity_id: "reaction.R01157"
entity_type: "reaction"
name: "agmatine amidinohydrolase"
source_database: "KEGG"
source_id: "R01157"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01157"
---

# agmatine amidinohydrolase

`reaction.R01157`

## Static

- Type: `reaction`
- Source: `KEGG:R01157`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Agmatine + H2O Putrescine + Urea

## Biological Role

Catalyzed by speB (protein.P60651). Substrates: H2O (molecule.C00001), Agmatine (molecule.C00179). Products: Urea (molecule.C00086), Putrescine (molecule.C00134).

## Annotation

Agmatine + H2O <=> Putrescine + Urea

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P60651|protein.P60651]] `KEGG` `database` - via EC:3.5.3.11
- `is_product_of` <-- [[molecule.C00086|molecule.C00086]] `KEGG` `database` - C00179 + C00001 <=> C00134 + C00086
- `is_product_of` <-- [[molecule.C00134|molecule.C00134]] `KEGG` `database` - C00179 + C00001 <=> C00134 + C00086
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00179 + C00001 <=> C00134 + C00086
- `is_substrate_of` <-- [[molecule.C00179|molecule.C00179]] `KEGG` `database` - C00179 + C00001 <=> C00134 + C00086

## External IDs

- `KEGG:R01157`

## Notes

EQUATION: C00179 + C00001 <=> C00134 + C00086
