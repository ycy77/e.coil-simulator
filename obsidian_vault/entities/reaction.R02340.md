---
entity_id: "reaction.R02340"
entity_type: "reaction"
name: "(1S,2R)-1-C-(indol-3-yl)glycerol 3-phosphate D-glyceraldehyde-3-phosphate-lyase"
source_database: "KEGG"
source_id: "R02340"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02340"
---

# (1S,2R)-1-C-(indol-3-yl)glycerol 3-phosphate D-glyceraldehyde-3-phosphate-lyase

`reaction.R02340`

## Static

- Type: `reaction`
- Source: `KEGG:R02340`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Indoleglycerol phosphate Indole + D-Glyceraldehyde 3-phosphate

## Biological Role

Catalyzed by trpA (protein.P0A877), trpB (protein.P0A879). Substrates: Indoleglycerol phosphate (molecule.C03506). Products: D-Glyceraldehyde 3-phosphate (molecule.C00118), Indole (molecule.C00463).

## Annotation

Indoleglycerol phosphate <=> Indole + D-Glyceraldehyde 3-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A877|protein.P0A877]] `KEGG` `database` - via EC:4.2.1.20
- `catalyzes` <-- [[protein.P0A879|protein.P0A879]] `KEGG` `database` - via EC:4.2.1.20
- `is_product_of` <-- [[molecule.C00118|molecule.C00118]] `KEGG` `database` - C03506 <=> C00463 + C00118
- `is_product_of` <-- [[molecule.C00463|molecule.C00463]] `KEGG` `database` - C03506 <=> C00463 + C00118
- `is_substrate_of` <-- [[molecule.C03506|molecule.C03506]] `KEGG` `database` - C03506 <=> C00463 + C00118

## External IDs

- `KEGG:R02340`

## Notes

EQUATION: C03506 <=> C00463 + C00118
