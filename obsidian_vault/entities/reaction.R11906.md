---
entity_id: "reaction.R11906"
entity_type: "reaction"
name: "isoniazid:hydrogen-peroxide oxidoreductase"
source_database: "KEGG"
source_id: "R11906"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R11906"
---

# isoniazid:hydrogen-peroxide oxidoreductase

`reaction.R11906`

## Static

- Type: `reaction`
- Source: `KEGG:R11906`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Isoniazid + Hydrogen peroxide Isonicotinoyl radical + Diimine + 2 H2O

## Biological Role

Catalyzed by katG (protein.P13029). Substrates: Hydrogen peroxide (molecule.C00027). Products: H2O (molecule.C00001).

## Annotation

Isoniazid + Hydrogen peroxide <=> Isonicotinoyl radical + Diimine + 2 H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P13029|protein.P13029]] `KEGG` `database` - via EC:1.11.1.21
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C07054 + C00027 <=> C21754 + C05360 + 2 C00001
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `KEGG` `database` - C07054 + C00027 <=> C21754 + C05360 + 2 C00001

## External IDs

- `KEGG:R11906`

## Notes

EQUATION: C07054 + C00027 <=> C21754 + C05360 + 2 C00001
