---
entity_id: "reaction.R00212"
entity_type: "reaction"
name: "acetyl-CoA:formate C-acetyltransferase"
source_database: "KEGG"
source_id: "R00212"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00212"
---

# acetyl-CoA:formate C-acetyltransferase

`reaction.R00212`

## Static

- Type: `reaction`
- Source: `KEGG:R00212`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acetyl-CoA + Formate CoA + Pyruvate

## Biological Role

Catalyzed by pflB (protein.P09373), tdcE (protein.P42632). Substrates: Acetyl-CoA (molecule.C00024), Formate (molecule.C00058). Products: CoA (molecule.C00010), Pyruvate (molecule.C00022).

## Annotation

Acetyl-CoA + Formate <=> CoA + Pyruvate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P09373|protein.P09373]] `KEGG` `database` - via EC:2.3.1.54
- `catalyzes` <-- [[protein.P42632|protein.P42632]] `KEGG` `database` - via EC:2.3.1.54
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00024 + C00058 <=> C00010 + C00022
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `KEGG` `database` - C00024 + C00058 <=> C00010 + C00022
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `KEGG` `database` - C00024 + C00058 <=> C00010 + C00022
- `is_substrate_of` <-- [[molecule.C00058|molecule.C00058]] `KEGG` `database` - C00024 + C00058 <=> C00010 + C00022

## External IDs

- `KEGG:R00212`

## Notes

EQUATION: C00024 + C00058 <=> C00010 + C00022
