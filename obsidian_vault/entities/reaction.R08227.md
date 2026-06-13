---
entity_id: "reaction.R08227"
entity_type: "reaction"
name: "5,6-dihydro-5-fluorouracil amidohydrolase"
source_database: "KEGG"
source_id: "R08227"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R08227"
---

# 5,6-dihydro-5-fluorouracil amidohydrolase

`reaction.R08227`

## Static

- Type: `reaction`
- Source: `KEGG:R08227`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5,6-Dihydro-5-fluorouracil + H2O alpha-Fluoro-beta-ureidopropionic acid

## Biological Role

Catalyzed by hyuA (protein.Q46806). Substrates: H2O (molecule.C00001).

## Annotation

5,6-Dihydro-5-fluorouracil + H2O <=> alpha-Fluoro-beta-ureidopropionic acid

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.Q46806|protein.Q46806]] `KEGG` `database` - via EC:3.5.2.2
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C16630 + C00001 <=> C16631

## External IDs

- `KEGG:R08227`

## Notes

EQUATION: C16630 + C00001 <=> C16631
