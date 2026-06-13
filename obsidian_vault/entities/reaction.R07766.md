---
entity_id: "reaction.R07766"
entity_type: "reaction"
name: "octanoyl-[acp]:protein N6-octanoyltransferase"
source_database: "KEGG"
source_id: "R07766"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07766"
---

# octanoyl-[acp]:protein N6-octanoyltransferase

`reaction.R07766`

## Static

- Type: `reaction`
- Source: `KEGG:R07766`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Octanoyl-[acp] + [Lipoyl-carrier protein]-L-lysine [Protein]-N6-(octanoyl)-L-lysine + Acyl-carrier protein

## Biological Role

Catalyzed by lipB (protein.P60720). Substrates: Octanoyl-[acp] (molecule.C05752). Products: Acyl-carrier protein (molecule.C00229).

## Annotation

Octanoyl-[acp] + [Lipoyl-carrier protein]-L-lysine <=> [Protein]-N6-(octanoyl)-L-lysine + Acyl-carrier protein

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P60720|protein.P60720]] `KEGG` `database` - via EC:2.3.1.181
- `is_product_of` <-- [[molecule.C00229|molecule.C00229]] `KEGG` `database` - C05752 + C16240 <=> C16236 + C00229
- `is_substrate_of` <-- [[molecule.C05752|molecule.C05752]] `KEGG` `database` - C05752 + C16240 <=> C16236 + C00229

## External IDs

- `KEGG:R07766`

## Notes

EQUATION: C05752 + C16240 <=> C16236 + C00229
