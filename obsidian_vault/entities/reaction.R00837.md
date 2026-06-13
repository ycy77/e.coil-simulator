---
entity_id: "reaction.R00837"
entity_type: "reaction"
name: "alpha,alpha-trehalose-6-phosphate phosphoglucohydrolase"
source_database: "KEGG"
source_id: "R00837"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00837"
---

# alpha,alpha-trehalose-6-phosphate phosphoglucohydrolase

`reaction.R00837`

## Static

- Type: `reaction`
- Source: `KEGG:R00837`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

H2O + alpha,alpha'-Trehalose 6-phosphate D-Glucose + D-Glucose 6-phosphate

## Biological Role

Catalyzed by treC (protein.P28904). Substrates: H2O (molecule.C00001), alpha,alpha'-Trehalose 6-phosphate (molecule.C00689). Products: D-Glucose (molecule.C00031), D-Glucose 6-phosphate (molecule.C00092).

## Annotation

H2O + alpha,alpha'-Trehalose 6-phosphate <=> D-Glucose + D-Glucose 6-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P28904|protein.P28904]] `KEGG` `database` - via EC:3.2.1.93
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `KEGG` `database` - C00001 + C00689 <=> C00031 + C00092
- `is_product_of` <-- [[molecule.C00092|molecule.C00092]] `KEGG` `database` - C00001 + C00689 <=> C00031 + C00092
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00001 + C00689 <=> C00031 + C00092
- `is_substrate_of` <-- [[molecule.C00689|molecule.C00689]] `KEGG` `database` - C00001 + C00689 <=> C00031 + C00092

## External IDs

- `KEGG:R00837`

## Notes

EQUATION: C00001 + C00689 <=> C00031 + C00092
