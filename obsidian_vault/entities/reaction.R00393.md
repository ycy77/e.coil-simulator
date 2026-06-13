---
entity_id: "reaction.R00393"
entity_type: "reaction"
name: "acyl-CoA:acetate CoA-transferase"
source_database: "KEGG"
source_id: "R00393"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00393"
---

# acyl-CoA:acetate CoA-transferase

`reaction.R00393`

## Static

- Type: `reaction`
- Source: `KEGG:R00393`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acyl-CoA + Acetate Fatty acid anion + Acetyl-CoA

## Biological Role

Catalyzed by ydiF (protein.P37766), atoD (protein.P76458), atoA (protein.P76459). Substrates: Acetate (molecule.C00033), Acyl-CoA (molecule.C00040). Products: Acetyl-CoA (molecule.C00024).

## Annotation

Acyl-CoA + Acetate <=> Fatty acid anion + Acetyl-CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P37766|protein.P37766]] `KEGG` `database` - via EC:2.8.3.8
- `catalyzes` <-- [[protein.P76458|protein.P76458]] `KEGG` `database` - via EC:2.8.3.8
- `catalyzes` <-- [[protein.P76459|protein.P76459]] `KEGG` `database` - via EC:2.8.3.8
- `is_product_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00040 + C00033 <=> C02403 + C00024
- `is_substrate_of` <-- [[molecule.C00033|molecule.C00033]] `KEGG` `database` - C00040 + C00033 <=> C02403 + C00024
- `is_substrate_of` <-- [[molecule.C00040|molecule.C00040]] `KEGG` `database` - C00040 + C00033 <=> C02403 + C00024

## External IDs

- `KEGG:R00393`

## Notes

EQUATION: C00040 + C00033 <=> C02403 + C00024
