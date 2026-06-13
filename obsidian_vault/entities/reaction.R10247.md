---
entity_id: "reaction.R10247"
entity_type: "reaction"
name: "1-deoxy-D-xylulose 5-phosphate:thiol sulfurtransferase"
source_database: "KEGG"
source_id: "R10247"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10247"
---

# 1-deoxy-D-xylulose 5-phosphate:thiol sulfurtransferase

`reaction.R10247`

## Static

- Type: `reaction`
- Source: `KEGG:R10247`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

1-Deoxy-D-xylulose 5-phosphate + Iminoglycine + Thiocarboxy-[sulfur-carrier protein] 2-[(2R,5Z)-2-Carboxy-4-methylthiazol-5(2H)-ylidene]ethyl phosphate + Sulfur-carrier protein + 2 H2O

## Biological Role

Catalyzed by thiG (protein.P30139). Substrates: 1-Deoxy-D-xylulose 5-phosphate (molecule.C11437), Iminoglycine (molecule.C15809), Thiocarboxy-[sulfur-carrier protein] (molecule.C15814). Products: H2O (molecule.C00001), Sulfur-carrier protein (molecule.C15810), 2-[(2R,5Z)-2-Carboxy-4-methylthiazol-5(2H)-ylidene]ethyl phosphate (molecule.C20246).

## Annotation

1-Deoxy-D-xylulose 5-phosphate + Iminoglycine + Thiocarboxy-[sulfur-carrier protein] <=> 2-[(2R,5Z)-2-Carboxy-4-methylthiazol-5(2H)-ylidene]ethyl phosphate + Sulfur-carrier protein + 2 H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P30139|protein.P30139]] `KEGG` `database` - via EC:2.8.1.10
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C11437 + C15809 + C15814 <=> C20246 + C15810 + 2 C00001
- `is_product_of` <-- [[molecule.C15810|molecule.C15810]] `KEGG` `database` - C11437 + C15809 + C15814 <=> C20246 + C15810 + 2 C00001
- `is_product_of` <-- [[molecule.C20246|molecule.C20246]] `KEGG` `database` - C11437 + C15809 + C15814 <=> C20246 + C15810 + 2 C00001
- `is_substrate_of` <-- [[molecule.C11437|molecule.C11437]] `KEGG` `database` - C11437 + C15809 + C15814 <=> C20246 + C15810 + 2 C00001
- `is_substrate_of` <-- [[molecule.C15809|molecule.C15809]] `KEGG` `database` - C11437 + C15809 + C15814 <=> C20246 + C15810 + 2 C00001
- `is_substrate_of` <-- [[molecule.C15814|molecule.C15814]] `KEGG` `database` - C11437 + C15809 + C15814 <=> C20246 + C15810 + 2 C00001

## External IDs

- `KEGG:R10247`

## Notes

EQUATION: C11437 + C15809 + C15814 <=> C20246 + C15810 + 2 C00001
