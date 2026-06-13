---
entity_id: "reaction.R00424"
entity_type: "reaction"
name: "GTP 7,8-8,9-dihydrolase"
source_database: "KEGG"
source_id: "R00424"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00424"
---

# GTP 7,8-8,9-dihydrolase

`reaction.R00424`

## Static

- Type: `reaction`
- Source: `KEGG:R00424`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GTP + H2O 7,8-Dihydroneopterin 3'-triphosphate + Formate

## Biological Role

Catalyzed by folE (protein.P0A6T5). Substrates: H2O (molecule.C00001), GTP (molecule.C00044). Products: Formate (molecule.C00058), 7,8-Dihydroneopterin 3'-triphosphate (molecule.C04895).

## Annotation

GTP + H2O <=> 7,8-Dihydroneopterin 3'-triphosphate + Formate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A6T5|protein.P0A6T5]] `KEGG` `database` - via EC:3.5.4.16
- `is_product_of` <-- [[molecule.C00058|molecule.C00058]] `KEGG` `database` - C00044 + C00001 <=> C04895 + C00058
- `is_product_of` <-- [[molecule.C04895|molecule.C04895]] `KEGG` `database` - C00044 + C00001 <=> C04895 + C00058
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00044 + C00001 <=> C04895 + C00058
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `KEGG` `database` - C00044 + C00001 <=> C04895 + C00058

## External IDs

- `KEGG:R00424`

## Notes

EQUATION: C00044 + C00001 <=> C04895 + C00058
