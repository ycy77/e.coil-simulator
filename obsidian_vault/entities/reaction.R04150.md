---
entity_id: "reaction.R04150"
entity_type: "reaction"
name: "O-succinylbenzoyl-CoA 1,4-dihydroxy-2-naphthoate-lyase"
source_database: "KEGG"
source_id: "R04150"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04150"
---

# O-succinylbenzoyl-CoA 1,4-dihydroxy-2-naphthoate-lyase

`reaction.R04150`

## Static

- Type: `reaction`
- Source: `KEGG:R04150`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Succinylbenzoyl-CoA 1,4-Dihydroxy-2-naphthoate + CoA

## Biological Role

Catalyzed by menB (protein.P0ABU0). Substrates: 2-Succinylbenzoyl-CoA (molecule.C03160). Products: CoA (molecule.C00010), 1,4-Dihydroxy-2-naphthoate (molecule.C03657).

## Annotation

2-Succinylbenzoyl-CoA <=> 1,4-Dihydroxy-2-naphthoate + CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0ABU0|protein.P0ABU0]] `KEGG` `database` - via EC:4.1.3.36
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C03160 <=> C03657 + C00010
- `is_product_of` <-- [[molecule.C03657|molecule.C03657]] `KEGG` `database` - C03160 <=> C03657 + C00010
- `is_substrate_of` <-- [[molecule.C03160|molecule.C03160]] `KEGG` `database` - C03160 <=> C03657 + C00010

## External IDs

- `KEGG:R04150`

## Notes

EQUATION: C03160 <=> C03657 + C00010
