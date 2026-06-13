---
entity_id: "reaction.R01150"
entity_type: "reaction"
name: "D-alanine:D-alanine ligase (ADP-forming)"
source_database: "KEGG"
source_id: "R01150"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01150"
---

# D-alanine:D-alanine ligase (ADP-forming)

`reaction.R01150`

## Static

- Type: `reaction`
- Source: `KEGG:R01150`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + 2 D-Alanine ADP + Orthophosphate + D-Alanyl-D-alanine

## Biological Role

Catalyzed by ddlB (protein.P07862), ddlA (protein.P0A6J8). Substrates: ATP (molecule.C00002), D-Alanine (molecule.C00133). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009), D-Alanyl-D-alanine (molecule.C00993).

## Annotation

ATP + 2 D-Alanine <=> ADP + Orthophosphate + D-Alanyl-D-alanine

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P07862|protein.P07862]] `KEGG` `database` - via EC:6.3.2.4
- `catalyzes` <-- [[protein.P0A6J8|protein.P0A6J8]] `KEGG` `database` - via EC:6.3.2.4
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + 2 C00133 <=> C00008 + C00009 + C00993
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00002 + 2 C00133 <=> C00008 + C00009 + C00993
- `is_product_of` <-- [[molecule.C00993|molecule.C00993]] `KEGG` `database` - C00002 + 2 C00133 <=> C00008 + C00009 + C00993
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + 2 C00133 <=> C00008 + C00009 + C00993
- `is_substrate_of` <-- [[molecule.C00133|molecule.C00133]] `KEGG` `database` - C00002 + 2 C00133 <=> C00008 + C00009 + C00993

## External IDs

- `KEGG:R01150`

## Notes

EQUATION: C00002 + 2 C00133 <=> C00008 + C00009 + C00993
