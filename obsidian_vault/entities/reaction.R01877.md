---
entity_id: "reaction.R01877"
entity_type: "reaction"
name: "uridine 3'-monophosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R01877"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01877"
---

# uridine 3'-monophosphate phosphohydrolase

`reaction.R01877`

## Static

- Type: `reaction`
- Source: `KEGG:R01877`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3'-UMP + H2O Uridine + Orthophosphate

## Biological Role

Catalyzed by cpdB (protein.P08331), surE (protein.P0A840). Substrates: H2O (molecule.C00001), 3'-UMP (molecule.C01368). Products: Orthophosphate (molecule.C00009), Uridine (molecule.C00299).

## Annotation

3'-UMP + H2O <=> Uridine + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P08331|protein.P08331]] `KEGG` `database` - via EC:3.1.3.6
- `catalyzes` <-- [[protein.P0A840|protein.P0A840]] `KEGG` `database` - via EC:3.1.3.6
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C01368 + C00001 <=> C00299 + C00009
- `is_product_of` <-- [[molecule.C00299|molecule.C00299]] `KEGG` `database` - C01368 + C00001 <=> C00299 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01368 + C00001 <=> C00299 + C00009
- `is_substrate_of` <-- [[molecule.C01368|molecule.C01368]] `KEGG` `database` - C01368 + C00001 <=> C00299 + C00009

## External IDs

- `KEGG:R01877`

## Notes

EQUATION: C01368 + C00001 <=> C00299 + C00009
