---
entity_id: "reaction.R01899"
entity_type: "reaction"
name: "isocitrate:NADP+ oxidoreductase"
source_database: "KEGG"
source_id: "R01899"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01899"
---

# isocitrate:NADP+ oxidoreductase

`reaction.R01899`

## Static

- Type: `reaction`
- Source: `KEGG:R01899`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Isocitrate + NADP+ Oxalosuccinate + NADPH + H+

## Biological Role

Catalyzed by icd (protein.P08200). Substrates: NADP+ (molecule.C00006), Isocitrate (molecule.C00311). Products: NADPH (molecule.C00005), H+ (molecule.C00080), Oxalosuccinate (molecule.C05379).

## Annotation

Isocitrate + NADP+ <=> Oxalosuccinate + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P08200|protein.P08200]] `KEGG` `database` - via EC:1.1.1.42
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00311 + C00006 <=> C05379 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00311 + C00006 <=> C05379 + C00005 + C00080
- `is_product_of` <-- [[molecule.C05379|molecule.C05379]] `KEGG` `database` - C00311 + C00006 <=> C05379 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00311 + C00006 <=> C05379 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00311|molecule.C00311]] `KEGG` `database` - C00311 + C00006 <=> C05379 + C00005 + C00080

## External IDs

- `KEGG:R01899`

## Notes

EQUATION: C00311 + C00006 <=> C05379 + C00005 + C00080
