---
entity_id: "reaction.R00160"
entity_type: "reaction"
name: "FAD nucleotidohydrolase"
source_database: "KEGG"
source_id: "R00160"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00160"
---

# FAD nucleotidohydrolase

`reaction.R00160`

## Static

- Type: `reaction`
- Source: `KEGG:R00160`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FAD + H2O AMP + FMN

## Biological Role

Catalyzed by mazG (protein.P0AEY3). Substrates: H2O (molecule.C00001), FAD (molecule.C00016). Products: AMP (molecule.C00020), FMN (molecule.C00061).

## Annotation

FAD + H2O <=> AMP + FMN

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AEY3|protein.P0AEY3]] `KEGG` `database` - via EC:3.6.1.9
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00016 + C00001 <=> C00020 + C00061
- `is_product_of` <-- [[molecule.C00061|molecule.C00061]] `KEGG` `database` - C00016 + C00001 <=> C00020 + C00061
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00016 + C00001 <=> C00020 + C00061
- `is_substrate_of` <-- [[molecule.C00016|molecule.C00016]] `KEGG` `database` - C00016 + C00001 <=> C00020 + C00061

## External IDs

- `KEGG:R00160`

## Notes

EQUATION: C00016 + C00001 <=> C00020 + C00061
