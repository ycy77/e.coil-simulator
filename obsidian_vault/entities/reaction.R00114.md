---
entity_id: "reaction.R00114"
entity_type: "reaction"
name: "L-glutamate:NADP+ oxidoreductase (transaminating)"
source_database: "KEGG"
source_id: "R00114"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00114"
---

# L-glutamate:NADP+ oxidoreductase (transaminating)

`reaction.R00114`

## Static

- Type: `reaction`
- Source: `KEGG:R00114`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2 L-Glutamate + NADP+ L-Glutamine + 2-Oxoglutarate + NADPH + H+

## Biological Role

Catalyzed by gltB (protein.P09831), gltD (protein.P09832). Substrates: NADP+ (molecule.C00006), L-Glutamate (molecule.C00025). Products: NADPH (molecule.C00005), 2-Oxoglutarate (molecule.C00026), L-Glutamine (molecule.C00064), H+ (molecule.C00080).

## Annotation

2 L-Glutamate + NADP+ <=> L-Glutamine + 2-Oxoglutarate + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P09831|protein.P09831]] `KEGG` `database` - via EC:1.4.1.13
- `catalyzes` <-- [[protein.P09832|protein.P09832]] `KEGG` `database` - via EC:1.4.1.13
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - 2 C00025 + C00006 <=> C00064 + C00026 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `KEGG` `database` - 2 C00025 + C00006 <=> C00064 + C00026 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00064|molecule.C00064]] `KEGG` `database` - 2 C00025 + C00006 <=> C00064 + C00026 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - 2 C00025 + C00006 <=> C00064 + C00026 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - 2 C00025 + C00006 <=> C00064 + C00026 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - 2 C00025 + C00006 <=> C00064 + C00026 + C00005 + C00080

## External IDs

- `KEGG:R00114`

## Notes

EQUATION: 2 C00025 + C00006 <=> C00064 + C00026 + C00005 + C00080
