---
entity_id: "reaction.R08230"
entity_type: "reaction"
name: "5-fluorodeoxyuridine:phosphate deoxy-alpha-D-ribosyltransferase"
source_database: "KEGG"
source_id: "R08230"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R08230"
---

# 5-fluorodeoxyuridine:phosphate deoxy-alpha-D-ribosyltransferase

`reaction.R08230`

## Static

- Type: `reaction`
- Source: `KEGG:R08230`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-FU + 2-Deoxy-D-ribose 1-phosphate 5-Fluorodeoxyuridine + Orthophosphate

## Biological Role

Catalyzed by deoA (protein.P07650). Substrates: 2-Deoxy-D-ribose 1-phosphate (molecule.C00672). Products: Orthophosphate (molecule.C00009).

## Annotation

5-FU + 2-Deoxy-D-ribose 1-phosphate <=> 5-Fluorodeoxyuridine + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P07650|protein.P07650]] `KEGG` `database` - via EC:2.4.2.4
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C07649 + C00672 <=> C11736 + C00009
- `is_substrate_of` <-- [[molecule.C00672|molecule.C00672]] `KEGG` `database` - C07649 + C00672 <=> C11736 + C00009

## External IDs

- `KEGG:R08230`

## Notes

EQUATION: C07649 + C00672 <=> C11736 + C00009
