---
entity_id: "reaction.R03458"
entity_type: "reaction"
name: "5-amino-6-(5-phosphoribitylamino)uracil:NADP+ 1'-oxidoreductase"
source_database: "KEGG"
source_id: "R03458"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03458"
---

# 5-amino-6-(5-phosphoribitylamino)uracil:NADP+ 1'-oxidoreductase

`reaction.R03458`

## Static

- Type: `reaction`
- Source: `KEGG:R03458`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-Amino-6-(5'-phospho-D-ribitylamino)uracil + NADP+ 5-Amino-6-(5'-phosphoribosylamino)uracil + NADPH + H+

## Biological Role

Catalyzed by ribD (protein.P25539). Substrates: NADP+ (molecule.C00006), 5-Amino-6-(5'-phospho-D-ribitylamino)uracil (molecule.C04454). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 5-Amino-6-(5'-phosphoribosylamino)uracil (molecule.C01268).

## Annotation

5-Amino-6-(5'-phospho-D-ribitylamino)uracil + NADP+ <=> 5-Amino-6-(5'-phosphoribosylamino)uracil + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P25539|protein.P25539]] `KEGG` `database` - via EC:1.1.1.193
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C04454 + C00006 <=> C01268 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C04454 + C00006 <=> C01268 + C00005 + C00080
- `is_product_of` <-- [[molecule.C01268|molecule.C01268]] `KEGG` `database` - C04454 + C00006 <=> C01268 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C04454 + C00006 <=> C01268 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C04454|molecule.C04454]] `KEGG` `database` - C04454 + C00006 <=> C01268 + C00005 + C00080

## External IDs

- `KEGG:R03458`

## Notes

EQUATION: C04454 + C00006 <=> C01268 + C00005 + C00080
