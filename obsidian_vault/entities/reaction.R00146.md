---
entity_id: "reaction.R00146"
entity_type: "reaction"
name: "alpha-amino acid:NADP+ oxidoreductase (deaminating)"
source_database: "KEGG"
source_id: "R00146"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00146"
---

# alpha-amino acid:NADP+ oxidoreductase (deaminating)

`reaction.R00146`

## Static

- Type: `reaction`
- Source: `KEGG:R00146`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

alpha-Amino acid + H2O + NADP+ 2-Oxo acid + Ammonia + NADPH + H+

## Biological Role

Catalyzed by gdhA (protein.P00370). Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006). Products: NADPH (molecule.C00005), Ammonia (molecule.C00014), H+ (molecule.C00080).

## Annotation

alpha-Amino acid + H2O + NADP+ <=> 2-Oxo acid + Ammonia + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P00370|protein.P00370]] `KEGG` `database` - via EC:1.4.1.4
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C05167 + C00001 + C00006 <=> C00161 + C00014 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C05167 + C00001 + C00006 <=> C00161 + C00014 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C05167 + C00001 + C00006 <=> C00161 + C00014 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C05167 + C00001 + C00006 <=> C00161 + C00014 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C05167 + C00001 + C00006 <=> C00161 + C00014 + C00005 + C00080

## External IDs

- `KEGG:R00146`

## Notes

EQUATION: C05167 + C00001 + C00006 <=> C00161 + C00014 + C00005 + C00080
