---
entity_id: "reaction.R12152"
entity_type: "reaction"
name: "R12152"
source_database: "KEGG"
source_id: "R12152"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12152"
---

# R12152

`reaction.R12152`

## Static

- Type: `reaction`
- Source: `KEGG:R12152`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N-(5'-Phospho-D-1'-ribulosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide + Ammonia 1-(5'-Phosphoribosyl)-5-amino-4-imidazolecarboxamide + D-erythro-1-(Imidazol-4-yl)glycerol 3-phosphate + H2O

## Biological Role

Catalyzed by hisH (protein.P60595), hisF (protein.P60664). Substrates: Ammonia (molecule.C00014), N-(5'-Phospho-D-1'-ribulosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide (molecule.C04916). Products: H2O (molecule.C00001), D-erythro-1-(Imidazol-4-yl)glycerol 3-phosphate (molecule.C04666), 1-(5'-Phosphoribosyl)-5-amino-4-imidazolecarboxamide (molecule.C04677).

## Annotation

N-(5'-Phospho-D-1'-ribulosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide + Ammonia <=> 1-(5'-Phosphoribosyl)-5-amino-4-imidazolecarboxamide + D-erythro-1-(Imidazol-4-yl)glycerol 3-phosphate + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P60595|protein.P60595]] `KEGG` `database` - via EC:4.3.2.10
- `catalyzes` <-- [[protein.P60664|protein.P60664]] `KEGG` `database` - via EC:4.3.2.10
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C04916 + C00014 <=> C04677 + C04666 + C00001
- `is_product_of` <-- [[molecule.C04666|molecule.C04666]] `KEGG` `database` - C04916 + C00014 <=> C04677 + C04666 + C00001
- `is_product_of` <-- [[molecule.C04677|molecule.C04677]] `KEGG` `database` - C04916 + C00014 <=> C04677 + C04666 + C00001
- `is_substrate_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C04916 + C00014 <=> C04677 + C04666 + C00001
- `is_substrate_of` <-- [[molecule.C04916|molecule.C04916]] `KEGG` `database` - C04916 + C00014 <=> C04677 + C04666 + C00001

## External IDs

- `KEGG:R12152`

## Notes

EQUATION: C04916 + C00014 <=> C04677 + C04666 + C00001
