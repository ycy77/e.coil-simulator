---
entity_id: "reaction.R03665"
entity_type: "reaction"
name: "L-valine:tRNAVal ligase (AMP-forming)"
source_database: "KEGG"
source_id: "R03665"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03665"
---

# L-valine:tRNAVal ligase (AMP-forming)

`reaction.R03665`

## Static

- Type: `reaction`
- Source: `KEGG:R03665`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + L-Valine + tRNA(Val) AMP + Diphosphate + L-Valyl-tRNA(Val)

## Biological Role

Catalyzed by valS (protein.P07118). Substrates: ATP (molecule.C00002), L-Valine (molecule.C00183). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), L-Valyl-tRNA(Val) (molecule.C02554).

## Annotation

ATP + L-Valine + tRNA(Val) <=> AMP + Diphosphate + L-Valyl-tRNA(Val)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P07118|protein.P07118]] `KEGG` `database` - via EC:6.1.1.9
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00183 + C01653 <=> C00020 + C00013 + C02554
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00183 + C01653 <=> C00020 + C00013 + C02554
- `is_product_of` <-- [[molecule.C02554|molecule.C02554]] `KEGG` `database` - C00002 + C00183 + C01653 <=> C00020 + C00013 + C02554
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00183 + C01653 <=> C00020 + C00013 + C02554
- `is_substrate_of` <-- [[molecule.C00183|molecule.C00183]] `KEGG` `database` - C00002 + C00183 + C01653 <=> C00020 + C00013 + C02554

## External IDs

- `KEGG:R03665`

## Notes

EQUATION: C00002 + C00183 + C01653 <=> C00020 + C00013 + C02554
