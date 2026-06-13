---
entity_id: "reaction.R07274"
entity_type: "reaction"
name: "O-phospho-L-serine:hydrogen-sulfide 2-amino-2-carboxyethyltransferase"
source_database: "KEGG"
source_id: "R07274"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07274"
---

# O-phospho-L-serine:hydrogen-sulfide 2-amino-2-carboxyethyltransferase

`reaction.R07274`

## Static

- Type: `reaction`
- Source: `KEGG:R07274`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

O-Phospho-L-serine + Hydrogen sulfide L-Cysteine + Orthophosphate

## Biological Role

Catalyzed by cysK (protein.P0ABK5). Substrates: Hydrogen sulfide (molecule.C00283), O-Phospho-L-serine (molecule.C01005). Products: Orthophosphate (molecule.C00009), L-Cysteine (molecule.C00097).

## Annotation

O-Phospho-L-serine + Hydrogen sulfide <=> L-Cysteine + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0ABK5|protein.P0ABK5]] `KEGG` `database` - via EC:2.5.1.47
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C01005 + C00283 <=> C00097 + C00009
- `is_product_of` <-- [[molecule.C00097|molecule.C00097]] `KEGG` `database` - C01005 + C00283 <=> C00097 + C00009
- `is_substrate_of` <-- [[molecule.C00283|molecule.C00283]] `KEGG` `database` - C01005 + C00283 <=> C00097 + C00009
- `is_substrate_of` <-- [[molecule.C01005|molecule.C01005]] `KEGG` `database` - C01005 + C00283 <=> C00097 + C00009

## External IDs

- `KEGG:R07274`

## Notes

EQUATION: C01005 + C00283 <=> C00097 + C00009
