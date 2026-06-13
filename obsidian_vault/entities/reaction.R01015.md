---
entity_id: "reaction.R01015"
entity_type: "reaction"
name: "D-glyceraldehyde-3-phosphate aldose-ketose-isomerase"
source_database: "KEGG"
source_id: "R01015"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01015"
---

# D-glyceraldehyde-3-phosphate aldose-ketose-isomerase

`reaction.R01015`

## Static

- Type: `reaction`
- Source: `KEGG:R01015`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Glyceraldehyde 3-phosphate Glycerone phosphate

## Biological Role

Catalyzed by tpiA (protein.P0A858). Substrates: D-Glyceraldehyde 3-phosphate (molecule.C00118). Products: Glycerone phosphate (molecule.C00111).

## Annotation

D-Glyceraldehyde 3-phosphate <=> Glycerone phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P0A858|protein.P0A858]] `KEGG` `database` - via EC:5.3.1.1
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `KEGG` `database` - C00118 <=> C00111
- `is_substrate_of` <-- [[molecule.C00118|molecule.C00118]] `KEGG` `database` - C00118 <=> C00111

## External IDs

- `KEGG:R01015`

## Notes

EQUATION: C00118 <=> C00111
