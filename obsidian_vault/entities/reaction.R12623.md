---
entity_id: "reaction.R12623"
entity_type: "reaction"
name: "(Z)-2-methylureidoacrylate amidohydrolase"
source_database: "KEGG"
source_id: "R12623"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12623"
---

# (Z)-2-methylureidoacrylate amidohydrolase

`reaction.R12623`

## Static

- Type: `reaction`
- Source: `KEGG:R12623`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Methylureidoacrylate + H2O Methylaminoacrylate + CO2 + Ammonia

## Biological Role

Catalyzed by rutB (protein.P75897). Substrates: H2O (molecule.C00001). Products: CO2 (molecule.C00011), Ammonia (molecule.C00014).

## Annotation

Methylureidoacrylate + H2O <=> Methylaminoacrylate + CO2 + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P75897|protein.P75897]] `KEGG` `database` - via EC:3.5.1.110
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C20256 + C00001 <=> C20255 + C00011 + C00014
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C20256 + C00001 <=> C20255 + C00011 + C00014
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C20256 + C00001 <=> C20255 + C00011 + C00014

## External IDs

- `KEGG:R12623`

## Notes

EQUATION: C20256 + C00001 <=> C20255 + C00011 + C00014
