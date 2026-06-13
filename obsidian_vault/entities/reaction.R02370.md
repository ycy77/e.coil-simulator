---
entity_id: "reaction.R02370"
entity_type: "reaction"
name: "cytidine 3'-phosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R02370"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02370"
---

# cytidine 3'-phosphate phosphohydrolase

`reaction.R02370`

## Static

- Type: `reaction`
- Source: `KEGG:R02370`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3'-CMP + H2O Cytidine + Orthophosphate

## Biological Role

Catalyzed by cpdB (protein.P08331), surE (protein.P0A840). Substrates: H2O (molecule.C00001), 3'-CMP (molecule.C05822). Products: Orthophosphate (molecule.C00009), Cytidine (molecule.C00475).

## Annotation

3'-CMP + H2O <=> Cytidine + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P08331|protein.P08331]] `KEGG` `database` - via EC:3.1.3.6
- `catalyzes` <-- [[protein.P0A840|protein.P0A840]] `KEGG` `database` - via EC:3.1.3.6
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C05822 + C00001 <=> C00475 + C00009
- `is_product_of` <-- [[molecule.C00475|molecule.C00475]] `KEGG` `database` - C05822 + C00001 <=> C00475 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C05822 + C00001 <=> C00475 + C00009
- `is_substrate_of` <-- [[molecule.C05822|molecule.C05822]] `KEGG` `database` - C05822 + C00001 <=> C00475 + C00009

## External IDs

- `KEGG:R02370`

## Notes

EQUATION: C05822 + C00001 <=> C00475 + C00009
