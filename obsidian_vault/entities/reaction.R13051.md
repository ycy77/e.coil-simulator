---
entity_id: "reaction.R13051"
entity_type: "reaction"
name: "daidzein 7-O-glucoside glucohydrolase"
source_database: "KEGG"
source_id: "R13051"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R13051"
---

# daidzein 7-O-glucoside glucohydrolase

`reaction.R13051`

## Static

- Type: `reaction`
- Source: `KEGG:R13051`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Daidzin + H2O Daidzein + beta-D-Glucose

## Biological Role

Catalyzed by bglX (protein.P33363). Substrates: H2O (molecule.C00001), Daidzin (molecule.C10216). Products: beta-D-Glucose (molecule.C00221), Daidzein (molecule.C10208).

## Annotation

Daidzin + H2O <=> Daidzein + beta-D-Glucose

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P33363|protein.P33363]] `KEGG` `database` - via EC:3.2.1.21
- `is_product_of` <-- [[molecule.C00221|molecule.C00221]] `KEGG` `database` - C10216 + C00001 <=> C10208 + C00221
- `is_product_of` <-- [[molecule.C10208|molecule.C10208]] `KEGG` `database` - C10216 + C00001 <=> C10208 + C00221
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C10216 + C00001 <=> C10208 + C00221
- `is_substrate_of` <-- [[molecule.C10216|molecule.C10216]] `KEGG` `database` - C10216 + C00001 <=> C10208 + C00221

## External IDs

- `KEGG:R13051`

## Notes

EQUATION: C10216 + C00001 <=> C10208 + C00221
