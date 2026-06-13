---
entity_id: "reaction.R03139"
entity_type: "reaction"
name: "primary-amine oxidase"
source_database: "KEGG"
source_id: "R03139"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03139"
---

# primary-amine oxidase

`reaction.R03139`

## Static

- Type: `reaction`
- Source: `KEGG:R03139`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

1,3-Diaminopropane + Oxygen + H2O 3-Aminopropanal + Ammonia + Hydrogen peroxide

## Biological Role

Catalyzed by tynA (protein.P46883). Substrates: H2O (molecule.C00001), Oxygen (molecule.C00007), 1,3-Diaminopropane (molecule.C00986). Products: Ammonia (molecule.C00014), Hydrogen peroxide (molecule.C00027), 3-Aminopropanal (molecule.C05665).

## Annotation

1,3-Diaminopropane + Oxygen + H2O <=> 3-Aminopropanal + Ammonia + Hydrogen peroxide

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P46883|protein.P46883]] `KEGG` `database` - via EC:1.4.3.21
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00986 + C00007 + C00001 <=> C05665 + C00014 + C00027
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `KEGG` `database` - C00986 + C00007 + C00001 <=> C05665 + C00014 + C00027
- `is_product_of` <-- [[molecule.C05665|molecule.C05665]] `KEGG` `database` - C00986 + C00007 + C00001 <=> C05665 + C00014 + C00027
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00986 + C00007 + C00001 <=> C05665 + C00014 + C00027
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - C00986 + C00007 + C00001 <=> C05665 + C00014 + C00027
- `is_substrate_of` <-- [[molecule.C00986|molecule.C00986]] `KEGG` `database` - C00986 + C00007 + C00001 <=> C05665 + C00014 + C00027

## External IDs

- `KEGG:R03139`

## Notes

EQUATION: C00986 + C00007 + C00001 <=> C05665 + C00014 + C00027
