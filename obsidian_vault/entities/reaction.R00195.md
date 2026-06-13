---
entity_id: "reaction.R00195"
entity_type: "reaction"
name: "2,3-diaminopropanoate ammonia-lyase (adding water; pyruvate-forming)"
source_database: "KEGG"
source_id: "R00195"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00195"
---

# 2,3-diaminopropanoate ammonia-lyase (adding water; pyruvate-forming)

`reaction.R00195`

## Static

- Type: `reaction`
- Source: `KEGG:R00195`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2,3-Diaminopropanoate + H2O Pyruvate + 2 Ammonia

## Biological Role

Catalyzed by ygeX (protein.P66899). Substrates: H2O (molecule.C00001). Products: Ammonia (molecule.C00014), Pyruvate (molecule.C00022).

## Annotation

2,3-Diaminopropanoate + H2O <=> Pyruvate + 2 Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P66899|protein.P66899]] `KEGG` `database` - via EC:4.3.1.15
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C06393 + C00001 <=> C00022 + 2 C00014
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C06393 + C00001 <=> C00022 + 2 C00014
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C06393 + C00001 <=> C00022 + 2 C00014

## External IDs

- `KEGG:R00195`

## Notes

EQUATION: C06393 + C00001 <=> C00022 + 2 C00014
