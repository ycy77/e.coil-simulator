---
entity_id: "reaction.R11329"
entity_type: "reaction"
name: "Fe-coproporphyrin-III ferro-lyase (coproporphyrin-III-forming)"
source_database: "KEGG"
source_id: "R11329"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R11329"
---

# Fe-coproporphyrin-III ferro-lyase (coproporphyrin-III-forming)

`reaction.R11329`

## Static

- Type: `reaction`
- Source: `KEGG:R11329`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Fe-coproporphyrin III + 2 H+ Coproporphyrin III + Fe2+

## Biological Role

Catalyzed by hemH (protein.P23871). Substrates: H+ (molecule.C00080), Fe-coproporphyrin III (molecule.C21284). Products: Coproporphyrin III (molecule.C05770), Fe2+ (molecule.C14818).

## Annotation

Fe-coproporphyrin III + 2 H+ <=> Coproporphyrin III + Fe2+

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P23871|protein.P23871]] `KEGG` `database` - via EC:4.99.1.9
- `is_product_of` <-- [[molecule.C05770|molecule.C05770]] `KEGG` `database` - C21284 + 2 C00080 <=> C05770 + C14818
- `is_product_of` <-- [[molecule.C14818|molecule.C14818]] `KEGG` `database` - C21284 + 2 C00080 <=> C05770 + C14818
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C21284 + 2 C00080 <=> C05770 + C14818
- `is_substrate_of` <-- [[molecule.C21284|molecule.C21284]] `KEGG` `database` - C21284 + 2 C00080 <=> C05770 + C14818

## External IDs

- `KEGG:R11329`

## Notes

EQUATION: C21284 + 2 C00080 <=> C05770 + C14818
