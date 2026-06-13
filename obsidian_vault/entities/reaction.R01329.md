---
entity_id: "reaction.R01329"
entity_type: "reaction"
name: "epimelibiose galactohydrolase"
source_database: "KEGG"
source_id: "R01329"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01329"
---

# epimelibiose galactohydrolase

`reaction.R01329`

## Static

- Type: `reaction`
- Source: `KEGG:R01329`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Epimelibiose + H2O D-Mannose + D-Galactose

## Biological Role

Catalyzed by melA (protein.P06720). Substrates: H2O (molecule.C00001), Epimelibiose (molecule.C05400). Products: D-Galactose (molecule.C00124), D-Mannose (molecule.C00159).

## Annotation

Epimelibiose + H2O <=> D-Mannose + D-Galactose

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P06720|protein.P06720]] `KEGG` `database` - via EC:3.2.1.22
- `is_product_of` <-- [[molecule.C00124|molecule.C00124]] `KEGG` `database` - C05400 + C00001 <=> C00159 + C00124
- `is_product_of` <-- [[molecule.C00159|molecule.C00159]] `KEGG` `database` - C05400 + C00001 <=> C00159 + C00124
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C05400 + C00001 <=> C00159 + C00124
- `is_substrate_of` <-- [[molecule.C05400|molecule.C05400]] `KEGG` `database` - C05400 + C00001 <=> C00159 + C00124

## External IDs

- `KEGG:R01329`

## Notes

EQUATION: C05400 + C00001 <=> C00159 + C00124
