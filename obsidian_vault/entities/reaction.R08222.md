---
entity_id: "reaction.R08222"
entity_type: "reaction"
name: "5'-deoxy-5-fluorouridine:phosphate deoxy-alpha-D-ribosyltransferase"
source_database: "KEGG"
source_id: "R08222"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R08222"
---

# 5'-deoxy-5-fluorouridine:phosphate deoxy-alpha-D-ribosyltransferase

`reaction.R08222`

## Static

- Type: `reaction`
- Source: `KEGG:R08222`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5'-Deoxy-5-fluorouridine + Orthophosphate 5-FU + 5-Deoxyribose-1-phosphate

## Biological Role

Catalyzed by deoA (protein.P07650). Substrates: Orthophosphate (molecule.C00009).

## Annotation

5'-Deoxy-5-fluorouridine + Orthophosphate <=> 5-FU + 5-Deoxyribose-1-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P07650|protein.P07650]] `KEGG` `database` - via EC:2.4.2.4
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C12739 + C00009 <=> C07649 + C16637

## External IDs

- `KEGG:R08222`

## Notes

EQUATION: C12739 + C00009 <=> C07649 + C16637
