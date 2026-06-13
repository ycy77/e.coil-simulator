---
entity_id: "reaction.R00751"
entity_type: "reaction"
name: "L-threonine acetaldehyde-lyase (glycine-forming)"
source_database: "KEGG"
source_id: "R00751"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00751"
---

# L-threonine acetaldehyde-lyase (glycine-forming)

`reaction.R00751`

## Static

- Type: `reaction`
- Source: `KEGG:R00751`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Threonine Glycine + Acetaldehyde

## Biological Role

Catalyzed by ltaE (protein.P75823). Substrates: L-Threonine (molecule.C00188). Products: Glycine (molecule.C00037), Acetaldehyde (molecule.C00084).

## Annotation

L-Threonine <=> Glycine + Acetaldehyde

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P75823|protein.P75823]] `KEGG` `database` - via EC:4.1.2.48
- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `KEGG` `database` - C00188 <=> C00037 + C00084
- `is_product_of` <-- [[molecule.C00084|molecule.C00084]] `KEGG` `database` - C00188 <=> C00037 + C00084
- `is_substrate_of` <-- [[molecule.C00188|molecule.C00188]] `KEGG` `database` - C00188 <=> C00037 + C00084

## External IDs

- `KEGG:R00751`

## Notes

EQUATION: C00188 <=> C00037 + C00084
