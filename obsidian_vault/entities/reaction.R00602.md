---
entity_id: "reaction.R00602"
entity_type: "reaction"
name: "methanol:hydrogen-peroxide oxidoreductase"
source_database: "KEGG"
source_id: "R00602"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00602"
---

# methanol:hydrogen-peroxide oxidoreductase

`reaction.R00602`

## Static

- Type: `reaction`
- Source: `KEGG:R00602`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Methanol + Hydrogen peroxide Formaldehyde + 2 H2O

## Biological Role

Catalyzed by katG (protein.P13029), katE (protein.P21179). Substrates: Hydrogen peroxide (molecule.C00027), Methanol (molecule.C00132). Products: H2O (molecule.C00001), Formaldehyde (molecule.C00067).

## Annotation

Methanol + Hydrogen peroxide <=> Formaldehyde + 2 H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P13029|protein.P13029]] `KEGG` `database` - via EC:1.11.1.21
- `catalyzes` <-- [[protein.P21179|protein.P21179]] `KEGG` `database` - via EC:1.11.1.6
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00132 + C00027 <=> C00067 + 2 C00001
- `is_product_of` <-- [[molecule.C00067|molecule.C00067]] `KEGG` `database` - C00132 + C00027 <=> C00067 + 2 C00001
- `is_substrate_of` <-- [[molecule.C00027|molecule.C00027]] `KEGG` `database` - C00132 + C00027 <=> C00067 + 2 C00001
- `is_substrate_of` <-- [[molecule.C00132|molecule.C00132]] `KEGG` `database` - C00132 + C00027 <=> C00067 + 2 C00001

## External IDs

- `KEGG:R00602`

## Notes

EQUATION: C00132 + C00027 <=> C00067 + 2 C00001
