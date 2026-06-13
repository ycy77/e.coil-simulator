---
entity_id: "reaction.R00719"
entity_type: "reaction"
name: "ITP phosphohydrolase"
source_database: "KEGG"
source_id: "R00719"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00719"
---

# ITP phosphohydrolase

`reaction.R00719`

## Static

- Type: `reaction`
- Source: `KEGG:R00719`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ITP + H2O IDP + Orthophosphate

## Biological Role

Catalyzed by yjjX (protein.P39411). Substrates: H2O (molecule.C00001), ITP (molecule.C00081). Products: Orthophosphate (molecule.C00009), IDP (molecule.C00104).

## Annotation

ITP + H2O <=> IDP + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P39411|protein.P39411]] `KEGG` `database` - via EC:3.6.1.73
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00081 + C00001 <=> C00104 + C00009
- `is_product_of` <-- [[molecule.C00104|molecule.C00104]] `KEGG` `database` - C00081 + C00001 <=> C00104 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00081 + C00001 <=> C00104 + C00009
- `is_substrate_of` <-- [[molecule.C00081|molecule.C00081]] `KEGG` `database` - C00081 + C00001 <=> C00104 + C00009

## External IDs

- `KEGG:R00719`

## Notes

EQUATION: C00081 + C00001 <=> C00104 + C00009
