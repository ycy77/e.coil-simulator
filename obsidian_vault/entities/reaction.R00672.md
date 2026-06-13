---
entity_id: "reaction.R00672"
entity_type: "reaction"
name: "ornithine racemase"
source_database: "KEGG"
source_id: "R00672"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00672"
---

# ornithine racemase

`reaction.R00672`

## Static

- Type: `reaction`
- Source: `KEGG:R00672`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Ornithine D-Ornithine

## Biological Role

Catalyzed by ygeA (protein.P03813). Substrates: L-Ornithine (molecule.C00077). Products: D-Ornithine (molecule.C00515).

## Annotation

L-Ornithine <=> D-Ornithine

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P03813|protein.P03813]] `KEGG` `database` - via EC:5.1.1.10
- `is_product_of` <-- [[molecule.C00515|molecule.C00515]] `KEGG` `database` - C00077 <=> C00515
- `is_substrate_of` <-- [[molecule.C00077|molecule.C00077]] `KEGG` `database` - C00077 <=> C00515

## External IDs

- `KEGG:R00672`

## Notes

EQUATION: C00077 <=> C00515
