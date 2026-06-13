---
entity_id: "reaction.R00579"
entity_type: "reaction"
name: "glutamine racemase"
source_database: "KEGG"
source_id: "R00579"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00579"
---

# glutamine racemase

`reaction.R00579`

## Static

- Type: `reaction`
- Source: `KEGG:R00579`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Glutamine D-Glutamine

## Biological Role

Catalyzed by ygeA (protein.P03813). Substrates: L-Glutamine (molecule.C00064). Products: D-Glutamine (molecule.C00819).

## Annotation

L-Glutamine <=> D-Glutamine

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P03813|protein.P03813]] `KEGG` `database` - via EC:5.1.1.10
- `is_product_of` <-- [[molecule.C00819|molecule.C00819]] `KEGG` `database` - C00064 <=> C00819
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `KEGG` `database` - C00064 <=> C00819

## External IDs

- `KEGG:R00579`

## Notes

EQUATION: C00064 <=> C00819
