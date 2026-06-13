---
entity_id: "reaction.R00481"
entity_type: "reaction"
name: "L-aspartate:oxygen oxidoreductase"
source_database: "KEGG"
source_id: "R00481"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00481"
---

# L-aspartate:oxygen oxidoreductase

`reaction.R00481`

## Static

- Type: `reaction`
- Source: `KEGG:R00481`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Aspartate + Oxygen Iminoaspartate + Hydrogen peroxide

## Biological Role

Catalyzed by nadB (protein.P10902). Substrates: Oxygen (molecule.C00007), L-Aspartate (molecule.C00049). Products: Hydrogen peroxide (molecule.C00027), Iminoaspartate (molecule.C05840).

## Annotation

L-Aspartate + Oxygen <=> Iminoaspartate + Hydrogen peroxide

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P10902|protein.P10902]] `KEGG` `database` - via EC:1.4.3.16
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `KEGG` `database` - C00049 + C00007 <=> C05840 + C00027
- `is_product_of` <-- [[molecule.C05840|molecule.C05840]] `KEGG` `database` - C00049 + C00007 <=> C05840 + C00027
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - C00049 + C00007 <=> C05840 + C00027
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `KEGG` `database` - C00049 + C00007 <=> C05840 + C00027

## External IDs

- `KEGG:R00481`

## Notes

EQUATION: C00049 + C00007 <=> C05840 + C00027
