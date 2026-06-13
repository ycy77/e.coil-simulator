---
entity_id: "reaction.R00999"
entity_type: "reaction"
name: "O-succinyl-L-homoserine succinate-lyase (deaminating; 2-oxobutanoate-forming)"
source_database: "KEGG"
source_id: "R00999"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00999"
---

# O-succinyl-L-homoserine succinate-lyase (deaminating; 2-oxobutanoate-forming)

`reaction.R00999`

## Static

- Type: `reaction`
- Source: `KEGG:R00999`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

O-Succinyl-L-homoserine + H2O 2-Oxobutanoate + Succinate + Ammonia

## Biological Role

Catalyzed by metB (protein.P00935). Substrates: H2O (molecule.C00001), O-Succinyl-L-homoserine (molecule.C01118). Products: Ammonia (molecule.C00014), Succinate (molecule.C00042), 2-Oxobutanoate (molecule.C00109).

## Annotation

O-Succinyl-L-homoserine + H2O <=> 2-Oxobutanoate + Succinate + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P00935|protein.P00935]] `KEGG` `database` - via EC:2.5.1.48
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C01118 + C00001 <=> C00109 + C00042 + C00014
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `KEGG` `database` - C01118 + C00001 <=> C00109 + C00042 + C00014
- `is_product_of` <-- [[molecule.C00109|molecule.C00109]] `KEGG` `database` - C01118 + C00001 <=> C00109 + C00042 + C00014
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01118 + C00001 <=> C00109 + C00042 + C00014
- `is_substrate_of` <-- [[molecule.C01118|molecule.C01118]] `KEGG` `database` - C01118 + C00001 <=> C00109 + C00042 + C00014

## External IDs

- `KEGG:R00999`

## Notes

EQUATION: C01118 + C00001 <=> C00109 + C00042 + C00014
