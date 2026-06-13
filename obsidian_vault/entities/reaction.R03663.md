---
entity_id: "reaction.R03663"
entity_type: "reaction"
name: "L-threonine:tRNA(Thr) ligase (AMP-forming)"
source_database: "KEGG"
source_id: "R03663"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03663"
---

# L-threonine:tRNA(Thr) ligase (AMP-forming)

`reaction.R03663`

## Static

- Type: `reaction`
- Source: `KEGG:R03663`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + L-Threonine + tRNA(Thr) AMP + Diphosphate + L-Threonyl-tRNA(Thr)

## Biological Role

Catalyzed by thrS (protein.P0A8M3). Substrates: ATP (molecule.C00002), L-Threonine (molecule.C00188). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), L-Threonyl-tRNA(Thr) (molecule.C02992).

## Annotation

ATP + L-Threonine + tRNA(Thr) <=> AMP + Diphosphate + L-Threonyl-tRNA(Thr)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A8M3|protein.P0A8M3]] `KEGG` `database` - via EC:6.1.1.3
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00188 + C01651 <=> C00020 + C00013 + C02992
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00188 + C01651 <=> C00020 + C00013 + C02992
- `is_product_of` <-- [[molecule.C02992|molecule.C02992]] `KEGG` `database` - C00002 + C00188 + C01651 <=> C00020 + C00013 + C02992
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00188 + C01651 <=> C00020 + C00013 + C02992
- `is_substrate_of` <-- [[molecule.C00188|molecule.C00188]] `KEGG` `database` - C00002 + C00188 + C01651 <=> C00020 + C00013 + C02992

## External IDs

- `KEGG:R03663`

## Notes

EQUATION: C00002 + C00188 + C01651 <=> C00020 + C00013 + C02992
