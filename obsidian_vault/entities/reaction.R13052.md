---
entity_id: "reaction.R13052"
entity_type: "reaction"
name: "genistein 7-O-beta-D-glucoside glucohydrolase"
source_database: "KEGG"
source_id: "R13052"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R13052"
---

# genistein 7-O-beta-D-glucoside glucohydrolase

`reaction.R13052`

## Static

- Type: `reaction`
- Source: `KEGG:R13052`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Genistin + H2O Genistein + beta-D-Glucose

## Biological Role

Catalyzed by bglX (protein.P33363). Substrates: H2O (molecule.C00001), Genistin (molecule.C09126). Products: beta-D-Glucose (molecule.C00221), Genistein (molecule.C06563).

## Annotation

Genistin + H2O <=> Genistein + beta-D-Glucose

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P33363|protein.P33363]] `KEGG` `database` - via EC:3.2.1.21
- `is_product_of` <-- [[molecule.C00221|molecule.C00221]] `KEGG` `database` - C09126 + C00001 <=> C06563 + C00221
- `is_product_of` <-- [[molecule.C06563|molecule.C06563]] `KEGG` `database` - C09126 + C00001 <=> C06563 + C00221
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C09126 + C00001 <=> C06563 + C00221
- `is_substrate_of` <-- [[molecule.C09126|molecule.C09126]] `KEGG` `database` - C09126 + C00001 <=> C06563 + C00221

## External IDs

- `KEGG:R13052`

## Notes

EQUATION: C09126 + C00001 <=> C06563 + C00221
