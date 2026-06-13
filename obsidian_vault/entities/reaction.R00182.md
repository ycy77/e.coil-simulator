---
entity_id: "reaction.R00182"
entity_type: "reaction"
name: "AMP phosphoribohydrolase"
source_database: "KEGG"
source_id: "R00182"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00182"
---

# AMP phosphoribohydrolase

`reaction.R00182`

## Static

- Type: `reaction`
- Source: `KEGG:R00182`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

AMP + H2O Adenine + D-Ribose 5-phosphate

## Biological Role

Catalyzed by amn (protein.P0AE12). Substrates: H2O (molecule.C00001), AMP (molecule.C00020). Products: D-Ribose 5-phosphate (molecule.C00117), Adenine (molecule.C00147).

## Annotation

AMP + H2O <=> Adenine + D-Ribose 5-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AE12|protein.P0AE12]] `KEGG` `database` - via EC:3.2.2.4
- `is_product_of` <-- [[molecule.C00117|molecule.C00117]] `KEGG` `database` - C00020 + C00001 <=> C00147 + C00117
- `is_product_of` <-- [[molecule.C00147|molecule.C00147]] `KEGG` `database` - C00020 + C00001 <=> C00147 + C00117
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00020 + C00001 <=> C00147 + C00117
- `is_substrate_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00020 + C00001 <=> C00147 + C00117

## External IDs

- `KEGG:R00182`

## Notes

EQUATION: C00020 + C00001 <=> C00147 + C00117
