---
entity_id: "reaction.R00115"
entity_type: "reaction"
name: "glutathione:NADP+ oxidoreductase"
source_database: "KEGG"
source_id: "R00115"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00115"
---

# glutathione:NADP+ oxidoreductase

`reaction.R00115`

## Static

- Type: `reaction`
- Source: `KEGG:R00115`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2 Glutathione + NADP+ Glutathione disulfide + NADPH + H+

## Biological Role

Catalyzed by gor (protein.P06715). Substrates: NADP+ (molecule.C00006), Glutathione (molecule.C00051). Products: NADPH (molecule.C00005), H+ (molecule.C00080), Glutathione disulfide (molecule.C00127).

## Annotation

2 Glutathione + NADP+ <=> Glutathione disulfide + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P06715|protein.P06715]] `KEGG` `database` - via EC:1.8.1.7
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - 2 C00051 + C00006 <=> C00127 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - 2 C00051 + C00006 <=> C00127 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `KEGG` `database` - 2 C00051 + C00006 <=> C00127 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - 2 C00051 + C00006 <=> C00127 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `KEGG` `database` - 2 C00051 + C00006 <=> C00127 + C00005 + C00080

## External IDs

- `KEGG:R00115`

## Notes

EQUATION: 2 C00051 + C00006 <=> C00127 + C00005 + C00080
