---
entity_id: "reaction.R00770"
entity_type: "reaction"
name: "ITP:D-fructose-6-phosphate 1-phosphotransferase"
source_database: "KEGG"
source_id: "R00770"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00770"
---

# ITP:D-fructose-6-phosphate 1-phosphotransferase

`reaction.R00770`

## Static

- Type: `reaction`
- Source: `KEGG:R00770`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ITP + D-Fructose 6-phosphate IDP + D-Fructose 1,6-bisphosphate

## Biological Role

Catalyzed by pfkB (protein.P06999), pfkA (protein.P0A796). Substrates: ITP (molecule.C00081), D-Fructose 6-phosphate (molecule.C00085). Products: IDP (molecule.C00104), D-Fructose 1,6-bisphosphate (molecule.C00354).

## Annotation

ITP + D-Fructose 6-phosphate <=> IDP + D-Fructose 1,6-bisphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P06999|protein.P06999]] `KEGG` `database` - via EC:2.7.1.11
- `catalyzes` <-- [[protein.P0A796|protein.P0A796]] `KEGG` `database` - via EC:2.7.1.11
- `is_product_of` <-- [[molecule.C00104|molecule.C00104]] `KEGG` `database` - C00081 + C00085 <=> C00104 + C00354
- `is_product_of` <-- [[molecule.C00354|molecule.C00354]] `KEGG` `database` - C00081 + C00085 <=> C00104 + C00354
- `is_substrate_of` <-- [[molecule.C00081|molecule.C00081]] `KEGG` `database` - C00081 + C00085 <=> C00104 + C00354
- `is_substrate_of` <-- [[molecule.C00085|molecule.C00085]] `KEGG` `database` - C00081 + C00085 <=> C00104 + C00354

## External IDs

- `KEGG:R00770`

## Notes

EQUATION: C00081 + C00085 <=> C00104 + C00354
