---
entity_id: "reaction.R00357"
entity_type: "reaction"
name: "L-aspartic acid:oxygen oxidoreductase (deaminating)"
source_database: "KEGG"
source_id: "R00357"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00357"
---

# L-aspartic acid:oxygen oxidoreductase (deaminating)

`reaction.R00357`

## Static

- Type: `reaction`
- Source: `KEGG:R00357`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Aspartate + H2O + Oxygen Oxaloacetate + Ammonia + Hydrogen peroxide

## Biological Role

Catalyzed by nadB (protein.P10902). Substrates: H2O (molecule.C00001), Oxygen (molecule.C00007), L-Aspartate (molecule.C00049). Products: Ammonia (molecule.C00014), Hydrogen peroxide (molecule.C00027), Oxaloacetate (molecule.C00036).

## Annotation

L-Aspartate + H2O + Oxygen <=> Oxaloacetate + Ammonia + Hydrogen peroxide

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P10902|protein.P10902]] `KEGG` `database` - via EC:1.4.3.16
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00049 + C00001 + C00007 <=> C00036 + C00014 + C00027
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `KEGG` `database` - C00049 + C00001 + C00007 <=> C00036 + C00014 + C00027
- `is_product_of` <-- [[molecule.C00036|molecule.C00036]] `KEGG` `database` - C00049 + C00001 + C00007 <=> C00036 + C00014 + C00027
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00049 + C00001 + C00007 <=> C00036 + C00014 + C00027
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - C00049 + C00001 + C00007 <=> C00036 + C00014 + C00027
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `KEGG` `database` - C00049 + C00001 + C00007 <=> C00036 + C00014 + C00027

## External IDs

- `KEGG:R00357`

## Notes

EQUATION: C00049 + C00001 + C00007 <=> C00036 + C00014 + C00027
