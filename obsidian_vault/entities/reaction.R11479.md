---
entity_id: "reaction.R11479"
entity_type: "reaction"
name: "acetyl-CoA:2-aminoethylphosphonate N-acetyltransferase"
source_database: "KEGG"
source_id: "R11479"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R11479"
---

# acetyl-CoA:2-aminoethylphosphonate N-acetyltransferase

`reaction.R11479`

## Static

- Type: `reaction`
- Source: `KEGG:R11479`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acetyl-CoA + 2-Aminoethylphosphonate 2-Acetamidoethylphosphonate + CoA

## Biological Role

Catalyzed by phnO (protein.P16691). Substrates: Acetyl-CoA (molecule.C00024), 2-Aminoethylphosphonate (molecule.C03557). Products: CoA (molecule.C00010), 2-Acetamidoethylphosphonate (molecule.C21403).

## Annotation

Acetyl-CoA + 2-Aminoethylphosphonate <=> 2-Acetamidoethylphosphonate + CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P16691|protein.P16691]] `KEGG` `database` - via EC:2.3.1.280
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00024 + C03557 <=> C21403 + C00010
- `is_product_of` <-- [[molecule.C21403|molecule.C21403]] `KEGG` `database` - C00024 + C03557 <=> C21403 + C00010
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00024 + C03557 <=> C21403 + C00010
- `is_substrate_of` <-- [[molecule.C03557|molecule.C03557]] `KEGG` `database` - C00024 + C03557 <=> C21403 + C00010

## External IDs

- `KEGG:R11479`

## Notes

EQUATION: C00024 + C03557 <=> C21403 + C00010
