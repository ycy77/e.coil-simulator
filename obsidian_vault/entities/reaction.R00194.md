---
entity_id: "reaction.R00194"
entity_type: "reaction"
name: "S-adenosyl-L-homocysteine homocysteinylribohydrolase"
source_database: "KEGG"
source_id: "R00194"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00194"
---

# S-adenosyl-L-homocysteine homocysteinylribohydrolase

`reaction.R00194`

## Static

- Type: `reaction`
- Source: `KEGG:R00194`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-Adenosyl-L-homocysteine + H2O S-Ribosyl-L-homocysteine + Adenine

## Biological Role

Catalyzed by mtnN (protein.P0AF12). Substrates: H2O (molecule.C00001), S-Adenosyl-L-homocysteine (molecule.C00021). Products: Adenine (molecule.C00147), S-Ribosyl-L-homocysteine (molecule.C03539).

## Annotation

S-Adenosyl-L-homocysteine + H2O <=> S-Ribosyl-L-homocysteine + Adenine

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AF12|protein.P0AF12]] `KEGG` `database` - via EC:3.2.2.9
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `KEGG` `database` - C00021 + C00001 <=> C03539 + C00147
- `is_product_of` <-- [[molecule.C03539|molecule.C03539]] `KEGG` `database` - C00021 + C00001 <=> C03539 + C00147
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00021 + C00001 <=> C03539 + C00147
- `is_substrate_of` <-- [[molecule.C00021|molecule.C00021]] `KEGG` `database` - C00021 + C00001 <=> C03539 + C00147

## External IDs

- `KEGG:R00194`

## Notes

EQUATION: C00021 + C00001 <=> C03539 + C00147
