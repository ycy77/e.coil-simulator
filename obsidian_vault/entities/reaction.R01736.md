---
entity_id: "reaction.R01736"
entity_type: "reaction"
name: "(R)-S-lactoylglutathione hydrolase"
source_database: "KEGG"
source_id: "R01736"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01736"
---

# (R)-S-lactoylglutathione hydrolase

`reaction.R01736`

## Static

- Type: `reaction`
- Source: `KEGG:R01736`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

(R)-S-Lactoylglutathione + H2O Glutathione + (R)-Lactate

## Biological Role

Catalyzed by gloB (protein.P0AC84), gloC (protein.P75849). Substrates: H2O (molecule.C00001), (R)-S-Lactoylglutathione (molecule.C03451). Products: Glutathione (molecule.C00051), (R)-Lactate (molecule.C00256).

## Annotation

(R)-S-Lactoylglutathione + H2O <=> Glutathione + (R)-Lactate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AC84|protein.P0AC84]] `KEGG` `database` - via EC:3.1.2.6
- `catalyzes` <-- [[protein.P75849|protein.P75849]] `KEGG` `database` - via EC:3.1.2.6
- `is_product_of` <-- [[molecule.C00051|molecule.C00051]] `KEGG` `database` - C03451 + C00001 <=> C00051 + C00256
- `is_product_of` <-- [[molecule.C00256|molecule.C00256]] `KEGG` `database` - C03451 + C00001 <=> C00051 + C00256
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C03451 + C00001 <=> C00051 + C00256
- `is_substrate_of` <-- [[molecule.C03451|molecule.C03451]] `KEGG` `database` - C03451 + C00001 <=> C00051 + C00256

## External IDs

- `KEGG:R01736`

## Notes

EQUATION: C03451 + C00001 <=> C00051 + C00256
