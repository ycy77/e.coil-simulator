---
entity_id: "reaction.R00103"
entity_type: "reaction"
name: "NAD+ phosphohydrolase"
source_database: "KEGG"
source_id: "R00103"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00103"
---

# NAD+ phosphohydrolase

`reaction.R00103`

## Static

- Type: `reaction`
- Source: `KEGG:R00103`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD+ + H2O AMP + Nicotinamide D-ribonucleotide

## Biological Role

Catalyzed by mazG (protein.P0AEY3), nudC (protein.P32664). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003). Products: AMP (molecule.C00020), Nicotinamide D-ribonucleotide (molecule.C00455).

## Annotation

NAD+ + H2O <=> AMP + Nicotinamide D-ribonucleotide

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AEY3|protein.P0AEY3]] `KEGG` `database` - via EC:3.6.1.9
- `catalyzes` <-- [[protein.P32664|protein.P32664]] `KEGG` `database` - via EC:3.6.1.22
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00003 + C00001 <=> C00020 + C00455
- `is_product_of` <-- [[molecule.C00455|molecule.C00455]] `KEGG` `database` - C00003 + C00001 <=> C00020 + C00455
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00003 + C00001 <=> C00020 + C00455
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00003 + C00001 <=> C00020 + C00455

## External IDs

- `KEGG:R00103`

## Notes

EQUATION: C00003 + C00001 <=> C00020 + C00455
