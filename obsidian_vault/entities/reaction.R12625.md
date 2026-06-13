---
entity_id: "reaction.R12625"
entity_type: "reaction"
name: "(Z)-3-ureidoacrylate amidohydrolase"
source_database: "KEGG"
source_id: "R12625"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12625"
---

# (Z)-3-ureidoacrylate amidohydrolase

`reaction.R12625`

## Static

- Type: `reaction`
- Source: `KEGG:R12625`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Ureidoacrylate + H2O Aminoacrylate + CO2 + Ammonia

## Biological Role

Catalyzed by rutB (protein.P75897). Substrates: H2O (molecule.C00001), Ureidoacrylate (molecule.C20254). Products: CO2 (molecule.C00011), Ammonia (molecule.C00014), Aminoacrylate (molecule.C20253).

## Annotation

Ureidoacrylate + H2O <=> Aminoacrylate + CO2 + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P75897|protein.P75897]] `KEGG` `database` - via EC:3.5.1.110
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C20254 + C00001 <=> C20253 + C00011 + C00014
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C20254 + C00001 <=> C20253 + C00011 + C00014
- `is_product_of` <-- [[molecule.C20253|molecule.C20253]] `KEGG` `database` - C20254 + C00001 <=> C20253 + C00011 + C00014
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C20254 + C00001 <=> C20253 + C00011 + C00014
- `is_substrate_of` <-- [[molecule.C20254|molecule.C20254]] `KEGG` `database` - C20254 + C00001 <=> C20253 + C00011 + C00014

## External IDs

- `KEGG:R12625`

## Notes

EQUATION: C20254 + C00001 <=> C20253 + C00011 + C00014
