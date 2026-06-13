---
entity_id: "reaction.R02382"
entity_type: "reaction"
name: "tyramine:oxygen oxidoreductase(deaminating)(flavin-containing)"
source_database: "KEGG"
source_id: "R02382"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02382"
---

# tyramine:oxygen oxidoreductase(deaminating)(flavin-containing)

`reaction.R02382`

## Static

- Type: `reaction`
- Source: `KEGG:R02382`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Tyramine + H2O + Oxygen 4-Hydroxyphenylacetaldehyde + Ammonia + Hydrogen peroxide

## Biological Role

Catalyzed by tynA (protein.P46883). Substrates: H2O (molecule.C00001), Oxygen (molecule.C00007), Tyramine (molecule.C00483). Products: Ammonia (molecule.C00014), Hydrogen peroxide (molecule.C00027), 4-Hydroxyphenylacetaldehyde (molecule.C03765).

## Annotation

Tyramine + H2O + Oxygen <=> 4-Hydroxyphenylacetaldehyde + Ammonia + Hydrogen peroxide

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P46883|protein.P46883]] `KEGG` `database` - via EC:1.4.3.21
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C00483 + C00001 + C00007 <=> C03765 + C00014 + C00027
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `KEGG` `database` - C00483 + C00001 + C00007 <=> C03765 + C00014 + C00027
- `is_product_of` <-- [[molecule.C03765|molecule.C03765]] `KEGG` `database` - C00483 + C00001 + C00007 <=> C03765 + C00014 + C00027
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00483 + C00001 + C00007 <=> C03765 + C00014 + C00027
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - C00483 + C00001 + C00007 <=> C03765 + C00014 + C00027
- `is_substrate_of` <-- [[molecule.C00483|molecule.C00483]] `KEGG` `database` - C00483 + C00001 + C00007 <=> C03765 + C00014 + C00027

## External IDs

- `KEGG:R02382`

## Notes

EQUATION: C00483 + C00001 + C00007 <=> C03765 + C00014 + C00027
