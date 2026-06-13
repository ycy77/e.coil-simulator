---
entity_id: "reaction.R00223"
entity_type: "reaction"
name: "serine ammonia-lyase (pyruvate-forming)"
source_database: "KEGG"
source_id: "R00223"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00223"
---

# serine ammonia-lyase (pyruvate-forming)

`reaction.R00223`

## Static

- Type: `reaction`
- Source: `KEGG:R00223`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Serine Pyruvate + Ammonia

## Biological Role

Catalyzed by ygeX (protein.P66899). Substrates: Serine (molecule.C00716). Products: Ammonia (molecule.C00014), Pyruvate (molecule.C00022).

## Annotation

Serine <=> Pyruvate + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P66899|protein.P66899]] `KEGG` `database` - via EC:4.3.1.15
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00716 <=> C00022 + C00014
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00716 <=> C00022 + C00014
- `is_substrate_of` <-- [[molecule.C00716|molecule.C00716]] `KEGG` `database` - C00716 <=> C00022 + C00014

## External IDs

- `KEGG:R00223`

## Notes

EQUATION: C00716 <=> C00022 + C00014
