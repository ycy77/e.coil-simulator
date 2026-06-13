---
entity_id: "reaction.R02596"
entity_type: "reaction"
name: "donor:hydrogen-peroxide oxidoreductase"
source_database: "KEGG"
source_id: "R02596"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02596"
---

# donor:hydrogen-peroxide oxidoreductase

`reaction.R02596`

## Static

- Type: `reaction`
- Source: `KEGG:R02596`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Coniferyl alcohol Guaiacyl lignin

## Biological Role

Catalyzed by katG (protein.P13029). Substrates: Coniferyl alcohol (molecule.C00590).

## Annotation

Coniferyl alcohol <=> Guaiacyl lignin

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P13029|protein.P13029]] `KEGG` `database` - via EC:1.11.1.21
- `is_substrate_of` <-- [[molecule.C00590|molecule.C00590]] `KEGG` `database` - C00590 <=> C15805

## External IDs

- `KEGG:R02596`

## Notes

EQUATION: C00590 <=> C15805
