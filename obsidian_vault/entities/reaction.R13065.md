---
entity_id: "reaction.R13065"
entity_type: "reaction"
name: "quercetin 3-O-glucoside glucohydrolase"
source_database: "KEGG"
source_id: "R13065"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R13065"
---

# quercetin 3-O-glucoside glucohydrolase

`reaction.R13065`

## Static

- Type: `reaction`
- Source: `KEGG:R13065`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Isoquercitrin + H2O Quercetin + beta-D-Glucose

## Biological Role

Catalyzed by bglX (protein.P33363). Substrates: H2O (molecule.C00001), Isoquercitrin (molecule.C05623). Products: beta-D-Glucose (molecule.C00221), Quercetin (molecule.C00389).

## Annotation

Isoquercitrin + H2O <=> Quercetin + beta-D-Glucose

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P33363|protein.P33363]] `KEGG` `database` - via EC:3.2.1.21
- `is_product_of` <-- [[molecule.C00221|molecule.C00221]] `KEGG` `database` - C05623 + C00001 <=> C00389 + C00221
- `is_product_of` <-- [[molecule.C00389|molecule.C00389]] `KEGG` `database` - C05623 + C00001 <=> C00389 + C00221
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C05623 + C00001 <=> C00389 + C00221
- `is_substrate_of` <-- [[molecule.C05623|molecule.C05623]] `KEGG` `database` - C05623 + C00001 <=> C00389 + C00221

## External IDs

- `KEGG:R13065`

## Notes

EQUATION: C05623 + C00001 <=> C00389 + C00221
