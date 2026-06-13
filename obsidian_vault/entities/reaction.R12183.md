---
entity_id: "reaction.R12183"
entity_type: "reaction"
name: "ATP:cob(II)alamin Cobeta-adenosyltransferase"
source_database: "KEGG"
source_id: "R12183"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12183"
---

# ATP:cob(II)alamin Cobeta-adenosyltransferase

`reaction.R12183`

## Static

- Type: `reaction`
- Source: `KEGG:R12183`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2 ATP + 2 Cob(II)alamin + [Reduced NADPH---hemoprotein reductase] 2 Triphosphate + 2 Cobamide coenzyme + [Oxidized NADPH---hemoprotein reductase]

## Biological Role

Catalyzed by btuR (protein.P0A9H5). Substrates: ATP (molecule.C00002), Cob(II)alamin (molecule.C00541). Products: Cobamide coenzyme (molecule.C00194), Triphosphate (molecule.C00536).

## Annotation

2 ATP + 2 Cob(II)alamin + [Reduced NADPH---hemoprotein reductase] <=> 2 Triphosphate + 2 Cobamide coenzyme + [Oxidized NADPH---hemoprotein reductase]

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A9H5|protein.P0A9H5]] `KEGG` `database` - via EC:2.5.1.17
- `is_product_of` <-- [[molecule.C00194|molecule.C00194]] `KEGG` `database` - 2 C00002 + 2 C00541 + C03024 <=> 2 C00536 + 2 C00194 + C03161
- `is_product_of` <-- [[molecule.C00536|molecule.C00536]] `KEGG` `database` - 2 C00002 + 2 C00541 + C03024 <=> 2 C00536 + 2 C00194 + C03161
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - 2 C00002 + 2 C00541 + C03024 <=> 2 C00536 + 2 C00194 + C03161
- `is_substrate_of` <-- [[molecule.C00541|molecule.C00541]] `KEGG` `database` - 2 C00002 + 2 C00541 + C03024 <=> 2 C00536 + 2 C00194 + C03161

## External IDs

- `KEGG:R12183`

## Notes

EQUATION: 2 C00002 + 2 C00541 + C03024 <=> 2 C00536 + 2 C00194 + C03161
