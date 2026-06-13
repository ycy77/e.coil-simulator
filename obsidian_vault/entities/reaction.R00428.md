---
entity_id: "reaction.R00428"
entity_type: "reaction"
name: "GTP 8,9-hydrolase"
source_database: "KEGG"
source_id: "R00428"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00428"
---

# GTP 8,9-hydrolase

`reaction.R00428`

## Static

- Type: `reaction`
- Source: `KEGG:R00428`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GTP + H2O Formamidopyrimidine nucleoside triphosphate

## Biological Role

Catalyzed by folE (protein.P0A6T5). Substrates: H2O (molecule.C00001), GTP (molecule.C00044). Products: Formamidopyrimidine nucleoside triphosphate (molecule.C05922).

## Annotation

GTP + H2O <=> Formamidopyrimidine nucleoside triphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A6T5|protein.P0A6T5]] `KEGG` `database` - via EC:3.5.4.16
- `is_product_of` <-- [[molecule.C05922|molecule.C05922]] `KEGG` `database` - C00044 + C00001 <=> C05922
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00044 + C00001 <=> C05922
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `KEGG` `database` - C00044 + C00001 <=> C05922

## External IDs

- `KEGG:R00428`

## Notes

EQUATION: C00044 + C00001 <=> C05922
