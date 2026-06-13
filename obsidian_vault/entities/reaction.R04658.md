---
entity_id: "reaction.R04658"
entity_type: "reaction"
name: "CMP-3-deoxy-D-manno-oct-2-ulosonate:lipid IVA 3-deoxy-D-manno-oct-2-ulosonate transferase"
source_database: "KEGG"
source_id: "R04658"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04658"
---

# CMP-3-deoxy-D-manno-oct-2-ulosonate:lipid IVA 3-deoxy-D-manno-oct-2-ulosonate transferase

`reaction.R04658`

## Static

- Type: `reaction`
- Source: `KEGG:R04658`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate + CMP-3-deoxy-D-manno-octulosonate 3-Deoxy-D-manno-octulosonyl-lipid IV(A) + CMP

## Biological Role

Catalyzed by waaA (protein.P0AC75). Substrates: CMP-3-deoxy-D-manno-octulosonate (molecule.C04121), 2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate (molecule.C04919). Products: CMP (molecule.C00055), 3-Deoxy-D-manno-octulosonyl-lipid IV(A) (molecule.C06024).

## Annotation

2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate + CMP-3-deoxy-D-manno-octulosonate <=> 3-Deoxy-D-manno-octulosonyl-lipid IV(A) + CMP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AC75|protein.P0AC75]] `KEGG` `database` - via EC:2.4.99.12
- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `KEGG` `database` - C04919 + C04121 <=> C06024 + C00055
- `is_product_of` <-- [[molecule.C06024|molecule.C06024]] `KEGG` `database` - C04919 + C04121 <=> C06024 + C00055
- `is_substrate_of` <-- [[molecule.C04121|molecule.C04121]] `KEGG` `database` - C04919 + C04121 <=> C06024 + C00055
- `is_substrate_of` <-- [[molecule.C04919|molecule.C04919]] `KEGG` `database` - C04919 + C04121 <=> C06024 + C00055

## External IDs

- `KEGG:R04658`

## Notes

EQUATION: C04919 + C04121 <=> C06024 + C00055
