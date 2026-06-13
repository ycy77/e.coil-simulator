---
entity_id: "reaction.R06893"
entity_type: "reaction"
name: "aryl-ester hydrolase"
source_database: "KEGG"
source_id: "R06893"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R06893"
---

# aryl-ester hydrolase

`reaction.R06893`

## Static

- Type: `reaction`
- Source: `KEGG:R06893`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

4-Hydroxyphenyl acetate + H2O Hydroquinone + Acetate

## Biological Role

Catalyzed by tesA (protein.P0ADA1). Substrates: H2O (molecule.C00001). Products: Acetate (molecule.C00033), Hydroquinone (molecule.C00530).

## Annotation

4-Hydroxyphenyl acetate + H2O <=> Hydroquinone + Acetate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0ADA1|protein.P0ADA1]] `KEGG` `database` - via EC:3.1.1.2
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `KEGG` `database` - C13636 + C00001 <=> C00530 + C00033
- `is_product_of` <-- [[molecule.C00530|molecule.C00530]] `KEGG` `database` - C13636 + C00001 <=> C00530 + C00033
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C13636 + C00001 <=> C00530 + C00033

## External IDs

- `KEGG:R06893`

## Notes

EQUATION: C13636 + C00001 <=> C00530 + C00033
