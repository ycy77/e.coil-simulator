---
entity_id: "reaction.R03132"
entity_type: "reaction"
name: "O-acetyl-L-serine:thiosulfate 2-amino-2-carboxyethyltransferase"
source_database: "KEGG"
source_id: "R03132"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03132"
---

# O-acetyl-L-serine:thiosulfate 2-amino-2-carboxyethyltransferase

`reaction.R03132`

## Static

- Type: `reaction`
- Source: `KEGG:R03132`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

O-Acetyl-L-serine + Thiosulfate S-Sulfo-L-cysteine + Acetate

## Biological Role

Catalyzed by cysM (protein.P16703). Substrates: Thiosulfate (molecule.C00320), O-Acetyl-L-serine (molecule.C00979). Products: Acetate (molecule.C00033), S-Sulfo-L-cysteine (molecule.C05824).

## Annotation

O-Acetyl-L-serine + Thiosulfate <=> S-Sulfo-L-cysteine + Acetate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P16703|protein.P16703]] `KEGG` `database` - via EC:2.5.1.144
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `KEGG` `database` - C00979 + C00320 <=> C05824 + C00033
- `is_product_of` <-- [[molecule.C05824|molecule.C05824]] `KEGG` `database` - C00979 + C00320 <=> C05824 + C00033
- `is_substrate_of` <-- [[molecule.C00320|molecule.C00320]] `KEGG` `database` - C00979 + C00320 <=> C05824 + C00033
- `is_substrate_of` <-- [[molecule.C00979|molecule.C00979]] `KEGG` `database` - C00979 + C00320 <=> C05824 + C00033

## External IDs

- `KEGG:R03132`

## Notes

EQUATION: C00979 + C00320 <=> C05824 + C00033
