---
entity_id: "reaction.R02613"
entity_type: "reaction"
name: "phenethylamine:oxygen oxidoreductase (deaminating)"
source_database: "KEGG"
source_id: "R02613"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02613"
---

# phenethylamine:oxygen oxidoreductase (deaminating)

`reaction.R02613`

## Static

- Type: `reaction`
- Source: `KEGG:R02613`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Phenethylamine + Oxygen + H2O Phenylacetaldehyde + Ammonia + Hydrogen peroxide

## Biological Role

Catalyzed by tynA (protein.P46883). Substrates: H2O (molecule.C00001), Oxygen (molecule.C00007), Phenethylamine (molecule.C05332). Products: Ammonia (molecule.C00014), Hydrogen peroxide (molecule.C00027), Phenylacetaldehyde (molecule.C00601).

## Annotation

Phenethylamine + Oxygen + H2O <=> Phenylacetaldehyde + Ammonia + Hydrogen peroxide

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P46883|protein.P46883]] `KEGG` `database` - via EC:1.4.3.21
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C05332 + C00007 + C00001 <=> C00601 + C00014 + C00027
- `is_product_of` <-- [[molecule.C00027|molecule.C00027]] `KEGG` `database` - C05332 + C00007 + C00001 <=> C00601 + C00014 + C00027
- `is_product_of` <-- [[molecule.C00601|molecule.C00601]] `KEGG` `database` - C05332 + C00007 + C00001 <=> C00601 + C00014 + C00027
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C05332 + C00007 + C00001 <=> C00601 + C00014 + C00027
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `KEGG` `database` - C05332 + C00007 + C00001 <=> C00601 + C00014 + C00027
- `is_substrate_of` <-- [[molecule.C05332|molecule.C05332]] `KEGG` `database` - C05332 + C00007 + C00001 <=> C00601 + C00014 + C00027

## External IDs

- `KEGG:R02613`

## Notes

EQUATION: C05332 + C00007 + C00001 <=> C00601 + C00014 + C00027
