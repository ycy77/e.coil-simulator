---
entity_id: "reaction.R00787"
entity_type: "reaction"
name: "ammonia:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R00787"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00787"
---

# ammonia:NAD+ oxidoreductase

`reaction.R00787`

## Static

- Type: `reaction`
- Source: `KEGG:R00787`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Ammonia + 3 NAD+ + 2 H2O Nitrite + 3 NADH + 3 H+

## Biological Role

Catalyzed by nirB (protein.P08201), nirD (protein.P0A9I8). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), Ammonia (molecule.C00014). Products: NADH (molecule.C00004), H+ (molecule.C00080), Nitrite (molecule.C00088).

## Annotation

Ammonia + 3 NAD+ + 2 H2O <=> Nitrite + 3 NADH + 3 H+

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P08201|protein.P08201]] `KEGG` `database` - via EC:1.7.1.15
- `catalyzes` <-- [[protein.P0A9I8|protein.P0A9I8]] `KEGG` `database` - via EC:1.7.1.15
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00014 + 3 C00003 + 2 C00001 <=> C00088 + 3 C00004 + 3 C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00014 + 3 C00003 + 2 C00001 <=> C00088 + 3 C00004 + 3 C00080
- `is_product_of` <-- [[molecule.C00088|molecule.C00088]] `KEGG` `database` - C00014 + 3 C00003 + 2 C00001 <=> C00088 + 3 C00004 + 3 C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00014 + 3 C00003 + 2 C00001 <=> C00088 + 3 C00004 + 3 C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00014 + 3 C00003 + 2 C00001 <=> C00088 + 3 C00004 + 3 C00080
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00014 + 3 C00003 + 2 C00001 <=> C00088 + 3 C00004 + 3 C00080

## External IDs

- `KEGG:R00787`

## Notes

EQUATION: C00014 + 3 C00003 + 2 C00001 <=> C00088 + 3 C00004 + 3 C00080
