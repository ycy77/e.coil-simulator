---
entity_id: "reaction.R00235"
entity_type: "reaction"
name: "acetate:CoA ligase (AMP-forming)"
source_database: "KEGG"
source_id: "R00235"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00235"
---

# acetate:CoA ligase (AMP-forming)

`reaction.R00235`

## Static

- Type: `reaction`
- Source: `KEGG:R00235`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Acetate + CoA AMP + Diphosphate + Acetyl-CoA

## Biological Role

Catalyzed by acs (protein.P27550). Substrates: ATP (molecule.C00002), CoA (molecule.C00010), Acetate (molecule.C00033). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), Acetyl-CoA (molecule.C00024).

## Annotation

ATP + Acetate + CoA <=> AMP + Diphosphate + Acetyl-CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P27550|protein.P27550]] `KEGG` `database` - via EC:6.2.1.1
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00033 + C00010 <=> C00020 + C00013 + C00024
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00033 + C00010 <=> C00020 + C00013 + C00024
- `is_product_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00002 + C00033 + C00010 <=> C00020 + C00013 + C00024
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00033 + C00010 <=> C00020 + C00013 + C00024
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00002 + C00033 + C00010 <=> C00020 + C00013 + C00024
- `is_substrate_of` <-- [[molecule.C00033|molecule.C00033]] `KEGG` `database` - C00002 + C00033 + C00010 <=> C00020 + C00013 + C00024

## External IDs

- `KEGG:R00235`

## Notes

EQUATION: C00002 + C00033 + C00010 <=> C00020 + C00013 + C00024
