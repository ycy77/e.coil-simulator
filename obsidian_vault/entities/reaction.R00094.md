---
entity_id: "reaction.R00094"
entity_type: "reaction"
name: "glutathione:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R00094"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00094"
---

# glutathione:NAD+ oxidoreductase

`reaction.R00094`

## Static

- Type: `reaction`
- Source: `KEGG:R00094`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2 Glutathione + NAD+ Glutathione disulfide + NADH + H+

## Biological Role

Catalyzed by gor (protein.P06715). Substrates: NAD+ (molecule.C00003), Glutathione (molecule.C00051). Products: NADH (molecule.C00004), H+ (molecule.C00080), Glutathione disulfide (molecule.C00127).

## Annotation

2 Glutathione + NAD+ <=> Glutathione disulfide + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P06715|protein.P06715]] `KEGG` `database` - via EC:1.8.1.7
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - 2 C00051 + C00003 <=> C00127 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - 2 C00051 + C00003 <=> C00127 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `KEGG` `database` - 2 C00051 + C00003 <=> C00127 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - 2 C00051 + C00003 <=> C00127 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `KEGG` `database` - 2 C00051 + C00003 <=> C00127 + C00004 + C00080

## External IDs

- `KEGG:R00094`

## Notes

EQUATION: 2 C00051 + C00003 <=> C00127 + C00004 + C00080
