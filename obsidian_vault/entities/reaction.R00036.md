---
entity_id: "reaction.R00036"
entity_type: "reaction"
name: "5-aminolevulinate hydro-lyase (adding 5-aminolevulinate and cyclizing; porphobilinogen-forming)"
source_database: "KEGG"
source_id: "R00036"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00036"
---

# 5-aminolevulinate hydro-lyase (adding 5-aminolevulinate and cyclizing; porphobilinogen-forming)

`reaction.R00036`

## Static

- Type: `reaction`
- Source: `KEGG:R00036`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2 5-Aminolevulinate Porphobilinogen + 2 H2O

## Biological Role

Catalyzed by hemB (protein.P0ACB2). Substrates: 5-Aminolevulinate (molecule.C00430). Products: H2O (molecule.C00001), Porphobilinogen (molecule.C00931).

## Annotation

2 5-Aminolevulinate <=> Porphobilinogen + 2 H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0ACB2|protein.P0ACB2]] `KEGG` `database` - via EC:4.2.1.24
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - 2 C00430 <=> C00931 + 2 C00001
- `is_product_of` <-- [[molecule.C00931|molecule.C00931]] `KEGG` `database` - 2 C00430 <=> C00931 + 2 C00001
- `is_substrate_of` <-- [[molecule.C00430|molecule.C00430]] `KEGG` `database` - 2 C00430 <=> C00931 + 2 C00001

## External IDs

- `KEGG:R00036`

## Notes

EQUATION: 2 C00430 <=> C00931 + 2 C00001
