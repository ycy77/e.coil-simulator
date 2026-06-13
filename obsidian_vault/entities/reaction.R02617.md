---
entity_id: "reaction.R02617"
entity_type: "reaction"
name: "2,3-dehydroacyl-CoA:sn-glycerol-3-phosphate O-acyltransferase"
source_database: "KEGG"
source_id: "R02617"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02617"
---

# 2,3-dehydroacyl-CoA:sn-glycerol-3-phosphate O-acyltransferase

`reaction.R02617`

## Static

- Type: `reaction`
- Source: `KEGG:R02617`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2,3-Dehydroacyl-CoA + sn-Glycerol 3-phosphate CoA + 1-Acyl-sn-glycerol 3-phosphate

## Biological Role

Catalyzed by plsB (protein.P0A7A7). Substrates: sn-Glycerol 3-phosphate (molecule.C00093). Products: CoA (molecule.C00010), 1-Acyl-sn-glycerol 3-phosphate (molecule.C00681).

## Annotation

2,3-Dehydroacyl-CoA + sn-Glycerol 3-phosphate <=> CoA + 1-Acyl-sn-glycerol 3-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A7A7|protein.P0A7A7]] `KEGG` `database` - via EC:2.3.1.15
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00605 + C00093 <=> C00010 + C00681
- `is_product_of` <-- [[molecule.C00681|molecule.C00681]] `KEGG` `database` - C00605 + C00093 <=> C00010 + C00681
- `is_substrate_of` <-- [[molecule.C00093|molecule.C00093]] `KEGG` `database` - C00605 + C00093 <=> C00010 + C00681

## External IDs

- `KEGG:R02617`

## Notes

EQUATION: C00605 + C00093 <=> C00010 + C00681
