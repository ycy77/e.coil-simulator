---
entity_id: "reaction.R01878"
entity_type: "reaction"
name: "cytidine aminohydrolase"
source_database: "KEGG"
source_id: "R01878"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01878"
---

# cytidine aminohydrolase

`reaction.R01878`

## Static

- Type: `reaction`
- Source: `KEGG:R01878`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Cytidine + H2O Uridine + Ammonia

## Biological Role

Catalyzed by cdd (protein.P0ABF6). Substrates: H2O (molecule.C00001), Cytidine (molecule.C00475). Products: Ammonia (molecule.C00014), Uridine (molecule.C00299).

## Annotation

Cytidine + H2O <=> Uridine + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0ABF6|protein.P0ABF6]] `KEGG` `database` - via EC:3.5.4.5
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00475 + C00001 <=> C00299 + C00014
- `is_product_of` <-- [[molecule.C00299|molecule.C00299]] `KEGG` `database` - C00475 + C00001 <=> C00299 + C00014
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00475 + C00001 <=> C00299 + C00014
- `is_substrate_of` <-- [[molecule.C00475|molecule.C00475]] `KEGG` `database` - C00475 + C00001 <=> C00299 + C00014

## External IDs

- `KEGG:R01878`

## Notes

EQUATION: C00475 + C00001 <=> C00299 + C00014
