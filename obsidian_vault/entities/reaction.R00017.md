---
entity_id: "reaction.R00017"
entity_type: "reaction"
name: "ferrocytochrome-c:hydrogen-peroxide oxidoreductase"
source_database: "KEGG"
source_id: "R00017"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00017"
---

# ferrocytochrome-c:hydrogen-peroxide oxidoreductase

`reaction.R00017`

## Static

- Type: `reaction`
- Source: `KEGG:R00017`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Hydrogen peroxide + 2 Ferrocytochrome c 2 Ferricytochrome c + 2 H2O

## Biological Role

Catalyzed by ccp (protein.P37197). Substrates: Hydrogen peroxide (molecule.C00027). Products: H2O (molecule.C00001).

## Annotation

Hydrogen peroxide + 2 Ferrocytochrome c <=> 2 Ferricytochrome c + 2 H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P37197|protein.P37197]] `KEGG` `database` - via EC:1.11.1.5
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00027 + 2 C00126 <=> 2 C00125 + 2 C00001
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `KEGG` `database` - C00027 + 2 C00126 <=> 2 C00125 + 2 C00001

## External IDs

- `KEGG:R00017`

## Notes

EQUATION: C00027 + 2 C00126 <=> 2 C00125 + 2 C00001
