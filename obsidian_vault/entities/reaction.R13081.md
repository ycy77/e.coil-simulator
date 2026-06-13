---
entity_id: "reaction.R13081"
entity_type: "reaction"
name: "naringenin 7-O-beta-D-glucoside glucohydrolase"
source_database: "KEGG"
source_id: "R13081"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R13081"
---

# naringenin 7-O-beta-D-glucoside glucohydrolase

`reaction.R13081`

## Static

- Type: `reaction`
- Source: `KEGG:R13081`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Naringenin 7-O-beta-D-glucoside + H2O Naringenin + beta-D-Glucose

## Biological Role

Catalyzed by bglX (protein.P33363). Substrates: H2O (molecule.C00001), Naringenin 7-O-beta-D-glucoside (molecule.C09099). Products: beta-D-Glucose (molecule.C00221), Naringenin (molecule.C00509).

## Annotation

Naringenin 7-O-beta-D-glucoside + H2O <=> Naringenin + beta-D-Glucose

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P33363|protein.P33363]] `KEGG` `database` - via EC:3.2.1.21
- `is_product_of` <-- [[molecule.C00221|molecule.C00221]] `KEGG` `database` - C09099 + C00001 <=> C00509 + C00221
- `is_product_of` <-- [[molecule.C00509|molecule.C00509]] `KEGG` `database` - C09099 + C00001 <=> C00509 + C00221
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C09099 + C00001 <=> C00509 + C00221
- `is_substrate_of` <-- [[molecule.C09099|molecule.C09099]] `KEGG` `database` - C09099 + C00001 <=> C00509 + C00221

## External IDs

- `KEGG:R13081`

## Notes

EQUATION: C09099 + C00001 <=> C00509 + C00221
