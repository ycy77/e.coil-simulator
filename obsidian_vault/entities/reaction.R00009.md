---
entity_id: "reaction.R00009"
entity_type: "reaction"
name: "hydrogen-peroxide:hydrogen-peroxide oxidoreductase"
source_database: "KEGG"
source_id: "R00009"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00009"
---

# hydrogen-peroxide:hydrogen-peroxide oxidoreductase

`reaction.R00009`

## Static

- Type: `reaction`
- Source: `KEGG:R00009`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2 Hydrogen peroxide Oxygen + 2 H2O

## Biological Role

Catalyzed by katG (protein.P13029), katE (protein.P21179). Substrates: Hydrogen peroxide (molecule.C00027). Products: H2O (molecule.C00001), Oxygen (molecule.C00007).

## Annotation

2 Hydrogen peroxide <=> Oxygen + 2 H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P13029|protein.P13029]] `KEGG` `database` - via EC:1.11.1.21
- `catalyzes` <-- [[protein.P21179|protein.P21179]] `KEGG` `database` - via EC:1.11.1.6
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - 2 C00027 <=> C00007 + 2 C00001
- `is_product_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - 2 C00027 <=> C00007 + 2 C00001
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `KEGG` `database` - 2 C00027 <=> C00007 + 2 C00001

## External IDs

- `KEGG:R00009`

## Notes

EQUATION: 2 C00027 <=> C00007 + 2 C00001
