---
entity_id: "reaction.R07268"
entity_type: "reaction"
name: "ATP:cobinamide Cobeta-adenosyltransferase"
source_database: "KEGG"
source_id: "R07268"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07268"
---

# ATP:cobinamide Cobeta-adenosyltransferase

`reaction.R07268`

## Static

- Type: `reaction`
- Source: `KEGG:R07268`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Cobinamide Triphosphate + Adenosyl cobinamide

## Biological Role

Catalyzed by btuR (protein.P0A9H5). Substrates: ATP (molecule.C00002), Cobinamide (molecule.C05774). Products: Triphosphate (molecule.C00536), Adenosyl cobinamide (molecule.C06508).

## Annotation

ATP + Cobinamide <=> Triphosphate + Adenosyl cobinamide

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A9H5|protein.P0A9H5]] `KEGG` `database` - via EC:2.5.1.17
- `is_product_of` <-- [[molecule.C00536|molecule.C00536]] `KEGG` `database` - C00002 + C05774 <=> C00536 + C06508
- `is_product_of` <-- [[molecule.C06508|molecule.C06508]] `KEGG` `database` - C00002 + C05774 <=> C00536 + C06508
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C05774 <=> C00536 + C06508
- `is_substrate_of` <-- [[molecule.C05774|molecule.C05774]] `KEGG` `database` - C00002 + C05774 <=> C00536 + C06508

## External IDs

- `KEGG:R07268`

## Notes

EQUATION: C00002 + C05774 <=> C00536 + C06508
