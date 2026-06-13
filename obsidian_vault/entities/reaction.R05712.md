---
entity_id: "reaction.R05712"
entity_type: "reaction"
name: "ammonia:ferricytochrome-c oxidoreductase"
source_database: "KEGG"
source_id: "R05712"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05712"
---

# ammonia:ferricytochrome-c oxidoreductase

`reaction.R05712`

## Static

- Type: `reaction`
- Source: `KEGG:R05712`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Ammonia + 2 H2O + 6 Ferricytochrome c Nitrite + 6 Ferrocytochrome c + 6 H+

## Biological Role

Catalyzed by nrfA (protein.P0ABK9). Substrates: H2O (molecule.C00001), Ammonia (molecule.C00014). Products: H+ (molecule.C00080), Nitrite (molecule.C00088).

## Annotation

Ammonia + 2 H2O + 6 Ferricytochrome c <=> Nitrite + 6 Ferrocytochrome c + 6 H+

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0ABK9|protein.P0ABK9]] `KEGG` `database` - via EC:1.7.2.2
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00014 + 2 C00001 + 6 C00125 <=> C00088 + 6 C00126 + 6 C00080
- `is_product_of` <-- [[molecule.C00088|molecule.C00088]] `KEGG` `database` - C00014 + 2 C00001 + 6 C00125 <=> C00088 + 6 C00126 + 6 C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00014 + 2 C00001 + 6 C00125 <=> C00088 + 6 C00126 + 6 C00080
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00014 + 2 C00001 + 6 C00125 <=> C00088 + 6 C00126 + 6 C00080

## External IDs

- `KEGG:R05712`

## Notes

EQUATION: C00014 + 2 C00001 + 6 C00125 <=> C00088 + 6 C00126 + 6 C00080
