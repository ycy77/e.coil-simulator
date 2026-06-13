---
entity_id: "reaction.R02110"
entity_type: "reaction"
name: "1,4-alpha-D-glucan:1,4-alpha-D-glucan 6-alpha-D-(1,4-alpha-D-glucano)-transferase"
source_database: "KEGG"
source_id: "R02110"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02110"
---

# 1,4-alpha-D-glucan:1,4-alpha-D-glucan 6-alpha-D-(1,4-alpha-D-glucano)-transferase

`reaction.R02110`

## Static

- Type: `reaction`
- Source: `KEGG:R02110`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Amylose Starch

## Biological Role

Catalyzed by glgB (protein.P07762). Substrates: Amylose (molecule.C00718). Products: Starch (molecule.C00369).

## Annotation

Amylose <=> Starch

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P07762|protein.P07762]] `KEGG` `database` - via EC:2.4.1.18
- `is_product_of` <-- [[molecule.C00369|molecule.C00369]] `KEGG` `database` - C00718 <=> C00369
- `is_substrate_of` <-- [[molecule.C00718|molecule.C00718]] `KEGG` `database` - C00718 <=> C00369

## External IDs

- `KEGG:R02110`

## Notes

EQUATION: C00718 <=> C00369
