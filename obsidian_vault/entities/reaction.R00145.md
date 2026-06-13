---
entity_id: "reaction.R00145"
entity_type: "reaction"
name: "alpha-amino acid:NAD+ oxidoreductase (deaminating)"
source_database: "KEGG"
source_id: "R00145"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00145"
---

# alpha-amino acid:NAD+ oxidoreductase (deaminating)

`reaction.R00145`

## Static

- Type: `reaction`
- Source: `KEGG:R00145`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

alpha-Amino acid + H2O + NAD+ 2-Oxo acid + Ammonia + NADH + H+

## Biological Role

Catalyzed by gdhA (protein.P00370). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003). Products: NADH (molecule.C00004), Ammonia (molecule.C00014), H+ (molecule.C00080).

## Annotation

alpha-Amino acid + H2O + NAD+ <=> 2-Oxo acid + Ammonia + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P00370|protein.P00370]] `KEGG` `database` - via EC:1.4.1.4
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C05167 + C00001 + C00003 <=> C00161 + C00014 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C05167 + C00001 + C00003 <=> C00161 + C00014 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C05167 + C00001 + C00003 <=> C00161 + C00014 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C05167 + C00001 + C00003 <=> C00161 + C00014 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C05167 + C00001 + C00003 <=> C00161 + C00014 + C00004 + C00080

## External IDs

- `KEGG:R00145`

## Notes

EQUATION: C05167 + C00001 + C00003 <=> C00161 + C00014 + C00004 + C00080
