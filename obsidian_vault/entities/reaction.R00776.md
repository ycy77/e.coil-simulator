---
entity_id: "reaction.R00776"
entity_type: "reaction"
name: "(S)-ureidoglycolate urea-lyase (glyoxylate-forming)"
source_database: "KEGG"
source_id: "R00776"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00776"
---

# (S)-ureidoglycolate urea-lyase (glyoxylate-forming)

`reaction.R00776`

## Static

- Type: `reaction`
- Source: `KEGG:R00776`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(S)-Ureidoglycolate Glyoxylate + Urea

## Biological Role

Catalyzed by allA (protein.P77731). Substrates: (S)-Ureidoglycolate (molecule.C00603). Products: Glyoxylate (molecule.C00048), Urea (molecule.C00086).

## Annotation

(S)-Ureidoglycolate <=> Glyoxylate + Urea

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P77731|protein.P77731]] `KEGG` `database` - via EC:4.3.2.3
- `is_product_of` <-- [[molecule.C00048|molecule.C00048]] `KEGG` `database` - C00603 <=> C00048 + C00086
- `is_product_of` <-- [[molecule.C00086|molecule.C00086]] `KEGG` `database` - C00603 <=> C00048 + C00086
- `is_substrate_of` <-- [[molecule.C00603|molecule.C00603]] `KEGG` `database` - C00603 <=> C00048 + C00086

## External IDs

- `KEGG:R00776`

## Notes

EQUATION: C00603 <=> C00048 + C00086
