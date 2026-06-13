---
entity_id: "reaction.R05850"
entity_type: "reaction"
name: "L-ribulose-5-phosphate 4-epimerase"
source_database: "KEGG"
source_id: "R05850"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05850"
---

# L-ribulose-5-phosphate 4-epimerase

`reaction.R05850`

## Static

- Type: `reaction`
- Source: `KEGG:R05850`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Ribulose 5-phosphate D-Xylulose 5-phosphate

## Biological Role

Catalyzed by araD (protein.P08203), sgbE (protein.P37680), ulaF (protein.P39306). Substrates: L-Ribulose 5-phosphate (molecule.C01101). Products: D-Xylulose 5-phosphate (molecule.C00231).

## Annotation

L-Ribulose 5-phosphate <=> D-Xylulose 5-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P08203|protein.P08203]] `KEGG` `database` - via EC:5.1.3.4
- `catalyzes` <-- [[protein.P37680|protein.P37680]] `KEGG` `database` - via EC:5.1.3.4
- `catalyzes` <-- [[protein.P39306|protein.P39306]] `KEGG` `database` - via EC:5.1.3.4
- `is_product_of` <-- [[molecule.C00231|molecule.C00231]] `KEGG` `database` - C01101 <=> C00231
- `is_substrate_of` <-- [[molecule.C01101|molecule.C01101]] `KEGG` `database` - C01101 <=> C00231

## External IDs

- `KEGG:R05850`

## Notes

EQUATION: C01101 <=> C00231
