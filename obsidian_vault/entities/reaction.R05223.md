---
entity_id: "reaction.R05223"
entity_type: "reaction"
name: "R05223"
source_database: "KEGG"
source_id: "R05223"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R05223"
---

# R05223

`reaction.R05223`

## Static

- Type: `reaction`
- Source: `KEGG:R05223`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Cobamide coenzyme + GMP Adenosine-GDP-cobinamide + alpha-Ribazole

## Biological Role

Catalyzed by cobS (protein.P36561). Substrates: GMP (molecule.C00144), Cobamide coenzyme (molecule.C00194). Products: alpha-Ribazole (molecule.C05775), Adenosine-GDP-cobinamide (molecule.C06510).

## Annotation

Cobamide coenzyme + GMP <=> Adenosine-GDP-cobinamide + alpha-Ribazole

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P36561|protein.P36561]] `KEGG` `database` - via EC:2.7.8.26
- `is_product_of` <-- [[molecule.C05775|molecule.C05775]] `KEGG` `database` - C00194 + C00144 <=> C06510 + C05775
- `is_product_of` <-- [[molecule.C06510|molecule.C06510]] `KEGG` `database` - C00194 + C00144 <=> C06510 + C05775
- `is_substrate_of` <-- [[molecule.C00144|molecule.C00144]] `KEGG` `database` - C00194 + C00144 <=> C06510 + C05775
- `is_substrate_of` <-- [[molecule.C00194|molecule.C00194]] `KEGG` `database` - C00194 + C00144 <=> C06510 + C05775

## External IDs

- `KEGG:R05223`

## Notes

EQUATION: C00194 + C00144 <=> C06510 + C05775
