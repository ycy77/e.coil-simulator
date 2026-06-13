---
entity_id: "reaction.R08229"
entity_type: "reaction"
name: "5-fluorouridine:phosphate alpha-D-ribosyltransferase"
source_database: "KEGG"
source_id: "R08229"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R08229"
---

# 5-fluorouridine:phosphate alpha-D-ribosyltransferase

`reaction.R08229`

## Static

- Type: `reaction`
- Source: `KEGG:R08229`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-FU + alpha-D-Ribose 1-phosphate 5-Fluorouridine + Orthophosphate

## Biological Role

Catalyzed by udp (protein.P12758). Substrates: alpha-D-Ribose 1-phosphate (molecule.C00620). Products: Orthophosphate (molecule.C00009).

## Annotation

5-FU + alpha-D-Ribose 1-phosphate <=> 5-Fluorouridine + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P12758|protein.P12758]] `KEGG` `database` - via EC:2.4.2.3
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C07649 + C00620 <=> C16633 + C00009
- `is_substrate_of` <-- [[molecule.C00620|molecule.C00620]] `KEGG` `database` - C07649 + C00620 <=> C16633 + C00009

## External IDs

- `KEGG:R08229`

## Notes

EQUATION: C07649 + C00620 <=> C16633 + C00009
