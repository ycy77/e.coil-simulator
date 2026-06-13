---
entity_id: "reaction.R01154"
entity_type: "reaction"
name: "acetyl-CoA:putrescine N-acetyltransferase"
source_database: "KEGG"
source_id: "R01154"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01154"
---

# acetyl-CoA:putrescine N-acetyltransferase

`reaction.R01154`

## Static

- Type: `reaction`
- Source: `KEGG:R01154`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acetyl-CoA + Putrescine CoA + N-Acetylputrescine

## Biological Role

Catalyzed by speG (protein.P0A951). Substrates: Acetyl-CoA (molecule.C00024), Putrescine (molecule.C00134). Products: CoA (molecule.C00010), N-Acetylputrescine (molecule.C02714).

## Annotation

Acetyl-CoA + Putrescine <=> CoA + N-Acetylputrescine

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A951|protein.P0A951]] `KEGG` `database` - via EC:2.3.1.57
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00024 + C00134 <=> C00010 + C02714
- `is_product_of` <-- [[molecule.C02714|molecule.C02714]] `KEGG` `database` - C00024 + C00134 <=> C00010 + C02714
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00024 + C00134 <=> C00010 + C02714
- `is_substrate_of` <-- [[molecule.C00134|molecule.C00134]] `KEGG` `database` - C00024 + C00134 <=> C00010 + C02714

## External IDs

- `KEGG:R01154`

## Notes

EQUATION: C00024 + C00134 <=> C00010 + C02714
