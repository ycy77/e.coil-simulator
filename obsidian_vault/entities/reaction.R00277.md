---
entity_id: "reaction.R00277"
entity_type: "reaction"
name: "pyridoxamine-5'-phosphate:oxygen oxidoreductase (deaminating)"
source_database: "KEGG"
source_id: "R00277"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00277"
---

# pyridoxamine-5'-phosphate:oxygen oxidoreductase (deaminating)

`reaction.R00277`

## Static

- Type: `reaction`
- Source: `KEGG:R00277`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Pyridoxamine phosphate + H2O + Oxygen Pyridoxal phosphate + Ammonia + Hydrogen peroxide

## Biological Role

Catalyzed by pdxH (protein.P0AFI7). Substrates: H2O (molecule.C00001), Oxygen (molecule.C00007), Pyridoxamine phosphate (molecule.C00647). Products: Ammonia (molecule.C00014), Pyridoxal phosphate (molecule.C00018), Hydrogen peroxide (molecule.C00027).

## Annotation

Pyridoxamine phosphate + H2O + Oxygen <=> Pyridoxal phosphate + Ammonia + Hydrogen peroxide

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AFI7|protein.P0AFI7]] `KEGG` `database` - via EC:1.4.3.5
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00647 + C00001 + C00007 <=> C00018 + C00014 + C00027
- `is_product_of` <-- [[molecule.C00018|molecule.C00018]] `KEGG` `database` - C00647 + C00001 + C00007 <=> C00018 + C00014 + C00027
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `KEGG` `database` - C00647 + C00001 + C00007 <=> C00018 + C00014 + C00027
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00647 + C00001 + C00007 <=> C00018 + C00014 + C00027
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - C00647 + C00001 + C00007 <=> C00018 + C00014 + C00027
- `is_substrate_of` <-- [[molecule.C00647|molecule.C00647]] `KEGG` `database` - C00647 + C00001 + C00007 <=> C00018 + C00014 + C00027

## External IDs

- `KEGG:R00277`

## Notes

EQUATION: C00647 + C00001 + C00007 <=> C00018 + C00014 + C00027
