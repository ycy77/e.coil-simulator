---
entity_id: "reaction.R06171"
entity_type: "reaction"
name: "L-allo-threonine acetaldehyde-lyase (glycine-forming)"
source_database: "KEGG"
source_id: "R06171"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R06171"
---

# L-allo-threonine acetaldehyde-lyase (glycine-forming)

`reaction.R06171`

## Static

- Type: `reaction`
- Source: `KEGG:R06171`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Allothreonine Glycine + Acetaldehyde

## Biological Role

Catalyzed by ltaE (protein.P75823). Substrates: L-Allothreonine (molecule.C05519). Products: Glycine (molecule.C00037), Acetaldehyde (molecule.C00084).

## Annotation

L-Allothreonine <=> Glycine + Acetaldehyde

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P75823|protein.P75823]] `KEGG` `database` - via EC:4.1.2.48
- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `KEGG` `database` - C05519 <=> C00037 + C00084
- `is_product_of` <-- [[molecule.C00084|molecule.C00084]] `KEGG` `database` - C05519 <=> C00037 + C00084
- `is_substrate_of` <-- [[molecule.C05519|molecule.C05519]] `KEGG` `database` - C05519 <=> C00037 + C00084

## External IDs

- `KEGG:R06171`

## Notes

EQUATION: C05519 <=> C00037 + C00084
