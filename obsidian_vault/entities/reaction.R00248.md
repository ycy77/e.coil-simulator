---
entity_id: "reaction.R00248"
entity_type: "reaction"
name: "L-glutamate:NADP+ oxidoreductase (deaminating)"
source_database: "KEGG"
source_id: "R00248"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00248"
---

# L-glutamate:NADP+ oxidoreductase (deaminating)

`reaction.R00248`

## Static

- Type: `reaction`
- Source: `KEGG:R00248`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Glutamate + NADP+ + H2O 2-Oxoglutarate + Ammonia + NADPH + H+

## Biological Role

Catalyzed by gdhA (protein.P00370), gltB (protein.P09831), gltD (protein.P09832). Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006), L-Glutamate (molecule.C00025). Products: NADPH (molecule.C00005), Ammonia (molecule.C00014), 2-Oxoglutarate (molecule.C00026), H+ (molecule.C00080).

## Annotation

L-Glutamate + NADP+ + H2O <=> 2-Oxoglutarate + Ammonia + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P00370|protein.P00370]] `KEGG` `database` - via EC:1.4.1.4
- `catalyzes` <-- [[protein.P09831|protein.P09831]] `KEGG` `database` - via EC:1.4.1.13
- `catalyzes` <-- [[protein.P09832|protein.P09832]] `KEGG` `database` - via EC:1.4.1.13
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C00025 + C00006 + C00001 <=> C00026 + C00014 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00025 + C00006 + C00001 <=> C00026 + C00014 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `KEGG` `database` - C00025 + C00006 + C00001 <=> C00026 + C00014 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00025 + C00006 + C00001 <=> C00026 + C00014 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00025 + C00006 + C00001 <=> C00026 + C00014 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C00025 + C00006 + C00001 <=> C00026 + C00014 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00025 + C00006 + C00001 <=> C00026 + C00014 + C00005 + C00080

## External IDs

- `KEGG:R00248`

## Notes

EQUATION: C00025 + C00006 + C00001 <=> C00026 + C00014 + C00005 + C00080
