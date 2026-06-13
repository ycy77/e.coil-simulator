---
entity_id: "reaction.R05389"
entity_type: "reaction"
name: "2-hydroxy-5-methyl-cis,cis-muconate 2-oxo-5-methyl-cis-muconate isomerase"
source_database: "KEGG"
source_id: "R05389"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05389"
---

# 2-hydroxy-5-methyl-cis,cis-muconate 2-oxo-5-methyl-cis-muconate isomerase

`reaction.R05389`

## Static

- Type: `reaction`
- Source: `KEGG:R05389`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Hydroxy-5-methyl-cis,cis-muconate 2-Oxo-5-methyl-cis-muconate

## Biological Role

Catalyzed by pptA (protein.P31992). Substrates: 2-Hydroxy-5-methyl-cis,cis-muconate (molecule.C07478). Products: 2-Oxo-5-methyl-cis-muconate (molecule.C07479).

## Annotation

2-Hydroxy-5-methyl-cis,cis-muconate <=> 2-Oxo-5-methyl-cis-muconate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P31992|protein.P31992]] `KEGG` `database` - via EC:5.3.2.6
- `is_product_of` <-- [[molecule.C07479|molecule.C07479]] `KEGG` `database` - C07478 <=> C07479
- `is_substrate_of` <-- [[molecule.C07478|molecule.C07478]] `KEGG` `database` - C07478 <=> C07479

## External IDs

- `KEGG:R05389`

## Notes

EQUATION: C07478 <=> C07479
