---
entity_id: "reaction.R02918"
entity_type: "reaction"
name: "L-tyrosine:tRNA(Tyr) ligase (AMP-forming)"
source_database: "KEGG"
source_id: "R02918"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02918"
---

# L-tyrosine:tRNA(Tyr) ligase (AMP-forming)

`reaction.R02918`

## Static

- Type: `reaction`
- Source: `KEGG:R02918`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + L-Tyrosine + tRNA(Tyr) AMP + Diphosphate + L-Tyrosyl-tRNA(Tyr)

## Biological Role

Catalyzed by tyrS (protein.P0AGJ9). Substrates: ATP (molecule.C00002), L-Tyrosine (molecule.C00082). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), L-Tyrosyl-tRNA(Tyr) (molecule.C02839).

## Annotation

ATP + L-Tyrosine + tRNA(Tyr) <=> AMP + Diphosphate + L-Tyrosyl-tRNA(Tyr)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AGJ9|protein.P0AGJ9]] `KEGG` `database` - via EC:6.1.1.1
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00082 + C00787 <=> C00020 + C00013 + C02839
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00082 + C00787 <=> C00020 + C00013 + C02839
- `is_product_of` <-- [[molecule.C02839|molecule.C02839]] `KEGG` `database` - C00002 + C00082 + C00787 <=> C00020 + C00013 + C02839
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00082 + C00787 <=> C00020 + C00013 + C02839
- `is_substrate_of` <-- [[molecule.C00082|molecule.C00082]] `KEGG` `database` - C00002 + C00082 + C00787 <=> C00020 + C00013 + C02839

## External IDs

- `KEGG:R02918`

## Notes

EQUATION: C00002 + C00082 + C00787 <=> C00020 + C00013 + C02839
