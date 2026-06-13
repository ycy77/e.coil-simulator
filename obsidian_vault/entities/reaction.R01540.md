---
entity_id: "reaction.R01540"
entity_type: "reaction"
name: "D-altronate hydro-lyase (2-dehydro-3-deoxy-D-gluconate-forming)"
source_database: "KEGG"
source_id: "R01540"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01540"
---

# D-altronate hydro-lyase (2-dehydro-3-deoxy-D-gluconate-forming)

`reaction.R01540`

## Static

- Type: `reaction`
- Source: `KEGG:R01540`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Altronate 2-Dehydro-3-deoxy-D-gluconate + H2O

## Biological Role

Catalyzed by uxaA (protein.P42604). Substrates: D-Altronate (molecule.C00817). Products: H2O (molecule.C00001), 2-Dehydro-3-deoxy-D-gluconate (molecule.C00204).

## Annotation

D-Altronate <=> 2-Dehydro-3-deoxy-D-gluconate + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P42604|protein.P42604]] `KEGG` `database` - via EC:4.2.1.7
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00817 <=> C00204 + C00001
- `is_product_of` <-- [[molecule.C00204|molecule.C00204]] `KEGG` `database` - C00817 <=> C00204 + C00001
- `is_substrate_of` <-- [[molecule.C00817|molecule.C00817]] `KEGG` `database` - C00817 <=> C00204 + C00001

## External IDs

- `KEGG:R01540`

## Notes

EQUATION: C00817 <=> C00204 + C00001
