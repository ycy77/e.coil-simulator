---
entity_id: "reaction.R07769"
entity_type: "reaction"
name: "lipoyl-[acp]:protein N6-lipoyltransferase"
source_database: "KEGG"
source_id: "R07769"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07769"
---

# lipoyl-[acp]:protein N6-lipoyltransferase

`reaction.R07769`

## Static

- Type: `reaction`
- Source: `KEGG:R07769`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Lipoyl-[acp] + [Lipoyl-carrier protein]-L-lysine Protein N6-(lipoyl)lysine + Acyl-carrier protein

## Biological Role

Catalyzed by lipB (protein.P60720). Products: Acyl-carrier protein (molecule.C00229).

## Annotation

Lipoyl-[acp] + [Lipoyl-carrier protein]-L-lysine <=> Protein N6-(lipoyl)lysine + Acyl-carrier protein

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P60720|protein.P60720]] `KEGG` `database` - via EC:2.3.1.181
- `is_product_of` <-- [[molecule.C00229|molecule.C00229]] `KEGG` `database` - C16239 + C16240 <=> C16237 + C00229

## External IDs

- `KEGG:R07769`

## Notes

EQUATION: C16239 + C16240 <=> C16237 + C00229
