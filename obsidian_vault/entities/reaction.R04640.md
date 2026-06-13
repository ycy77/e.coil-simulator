---
entity_id: "reaction.R04640"
entity_type: "reaction"
name: "N-(5'-phospho-D-ribosylformimino)-5-amino-1- (5''-phospho-D-ribosyl)-4-imidazolecarboxamide ketol-isomerase;"
source_database: "KEGG"
source_id: "R04640"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04640"
---

# N-(5'-phospho-D-ribosylformimino)-5-amino-1- (5''-phospho-D-ribosyl)-4-imidazolecarboxamide ketol-isomerase;

`reaction.R04640`

## Static

- Type: `reaction`
- Source: `KEGG:R04640`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-(5-Phospho-D-ribosylaminoformimino)-1-(5-phosphoribosyl)-imidazole-4-carboxamide N-(5'-Phospho-D-1'-ribulosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide

## Biological Role

Catalyzed by hisA (protein.P10371). Substrates: 5-(5-Phospho-D-ribosylaminoformimino)-1-(5-phosphoribosyl)-imidazole-4-carboxamide (molecule.C04896). Products: N-(5'-Phospho-D-1'-ribulosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide (molecule.C04916).

## Annotation

5-(5-Phospho-D-ribosylaminoformimino)-1-(5-phosphoribosyl)-imidazole-4-carboxamide <=> N-(5'-Phospho-D-1'-ribulosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P10371|protein.P10371]] `KEGG` `database` - via EC:5.3.1.16
- `is_product_of` <-- [[molecule.C04916|molecule.C04916]] `KEGG` `database` - C04896 <=> C04916
- `is_substrate_of` <-- [[molecule.C04896|molecule.C04896]] `KEGG` `database` - C04896 <=> C04916

## External IDs

- `KEGG:R04640`

## Notes

EQUATION: C04896 <=> C04916
