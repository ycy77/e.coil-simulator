---
entity_id: "reaction.R03661"
entity_type: "reaction"
name: "L-proline:tRNA(Pro) ligase (AMP-forming)"
source_database: "KEGG"
source_id: "R03661"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03661"
---

# L-proline:tRNA(Pro) ligase (AMP-forming)

`reaction.R03661`

## Static

- Type: `reaction`
- Source: `KEGG:R03661`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + L-Proline + tRNA(Pro) AMP + Diphosphate + L-Prolyl-tRNA(Pro)

## Biological Role

Catalyzed by proS (protein.P16659). Substrates: ATP (molecule.C00002), L-Proline (molecule.C00148). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), L-Prolyl-tRNA(Pro) (molecule.C02702).

## Annotation

ATP + L-Proline + tRNA(Pro) <=> AMP + Diphosphate + L-Prolyl-tRNA(Pro)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P16659|protein.P16659]] `KEGG` `database` - via EC:6.1.1.15
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00148 + C01649 <=> C00020 + C00013 + C02702
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00148 + C01649 <=> C00020 + C00013 + C02702
- `is_product_of` <-- [[molecule.C02702|molecule.C02702]] `KEGG` `database` - C00002 + C00148 + C01649 <=> C00020 + C00013 + C02702
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00148 + C01649 <=> C00020 + C00013 + C02702
- `is_substrate_of` <-- [[molecule.C00148|molecule.C00148]] `KEGG` `database` - C00002 + C00148 + C01649 <=> C00020 + C00013 + C02702

## External IDs

- `KEGG:R03661`

## Notes

EQUATION: C00002 + C00148 + C01649 <=> C00020 + C00013 + C02702
